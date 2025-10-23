from rest_framework.decorators import api_view
from rest_framework.response import Response
from vendors.models import Vendor
from vendors.serializers import VendorSerializer
import re
import uuid

@api_view(['POST'])
def chat_message(request):
    message = request.data.get('message', '').lower()
    session_id = request.data.get('session_id', str(uuid.uuid4()))
    
    # Simple AI response logic
    if 'wedding' in message:
        if any(word in message for word in ['budget', 'cost', 'price']):
            # Extract budget if mentioned
            budget_match = re.search(r'(\d+)', message)
            budget = int(budget_match.group(1)) * 1000 if budget_match else 300000
            
            response = f"Great! For a wedding with {budget:,} KES budget, let me find available vendors..."
            
            # Get sample vendors for wedding
            wedding_vendors = []
            service_types = ['catering', 'photography', 'venue', 'decoration', 'mc', 'dj']
            
            for service in service_types:
                vendors = Vendor.objects.filter(
                    service_type=service, 
                    price__lte=budget//6
                ).order_by('-rating')[:1]
                
                if vendors:
                    wedding_vendors.extend(vendors)
            
            serializer = VendorSerializer(wedding_vendors, many=True)
            total_cost = sum(v.price for v in wedding_vendors)
            
            return Response({
                "response": response,
                "vendors": serializer.data,
                "total_cost": float(total_cost),
                "session_id": session_id
            })
        else:
            return Response({
                "response": "Wonderful! Congratulations! 🎉 What's your total budget for the wedding?",
                "session_id": session_id
            })
    
    elif 'birthday' in message:
        return Response({
            "response": "Awesome! Birthday parties are so much fun! 🎂 What's your budget and how many guests?",
            "session_id": session_id
        })
    
    elif 'corporate' in message:
        return Response({
            "response": "Perfect! Corporate events require professional vendors. What's the event type and budget?",
            "session_id": session_id
        })
    
    elif any(word in message for word in ['hi', 'hello', 'hey', 'start']):
        return Response({
            "response": "Hi there! 👋 I'm your Event-Safi planning assistant. What type of event are you planning?",
            "session_id": session_id
        })
    
    elif any(word in message for word in ['help', 'services', 'what']):
        return Response({
            "response": "I can help you plan weddings, birthdays, corporate events, graduations, and more! I'll find the best vendors within your budget. What type of event do you have in mind?",
            "session_id": session_id
        })
    
    else:
        return Response({
            "response": "I can help you plan any event! Just tell me the event type (wedding, birthday, corporate, etc.) and your budget, and I'll find perfect vendors for you.",
            "session_id": session_id
        })
