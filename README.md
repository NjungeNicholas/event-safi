# Event-Safi 🎉

**Plan Any Event, Book Every Service — Effortlessly**

Event-Safi is an AI-powered event planning platform that helps users find and book vendors for any type of event through an intelligent chat interface.

## Features

- 🤖 **AI Chat Assistant** - Natural conversation to understand event requirements
- 🔍 **Smart Vendor Search** - Find vendors by service type, budget, date, and location
- ⭐ **Rated Vendors** - See reviews and ratings before booking
- 📅 **Real-time Availability** - Check vendor availability instantly
- 💰 **Budget Optimization** - Get recommendations within your budget
- 📱 **Mobile Friendly** - Works seamlessly on all devices

## Tech Stack

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - API development
- **SQLite** - Database (easily switchable to PostgreSQL)
- **Django CORS Headers** - Cross-origin requests

### Frontend
- **React 18** - User interface
- **Modern CSS** - Responsive design
- **Fetch API** - Backend communication

## Quick Start

1. **Clone and Setup**
   ```bash
   git clone <repository-url>
   cd event-safi
   ./setup.sh
   ```

2. **Start Backend**
   ```bash
   cd backend
   python manage.py runserver
   ```

3. **Start Frontend** (new terminal)
   ```bash
   cd frontend
   npm start
   ```

4. **Visit Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin (admin/admin)

## API Endpoints

### Vendors
- `GET /api/vendors/` - List all vendors
- `GET /api/vendors/{id}/` - Get vendor details
- `POST /api/vendors/search/` - Search vendors
- `POST /api/vendors/check-availability/` - Check availability
- `POST /api/vendors/book/` - Create booking

### Chat
- `POST /api/chat/message/` - Send chat message

## Sample Chat Flow

```
User: "I'm planning a wedding on December 15th"
AI: "Wonderful! Congratulations! 🎉 What's your total budget for the wedding?"

User: "300,000 shillings"
AI: "Great! For a wedding with 300,000 KES budget, let me find available vendors..."

[AI returns vendor recommendations with pricing]
```

## Database Models

### Vendor
- Basic info (name, service_type, rating, price, location)
- Contact details (phone, email)
- Portfolio and description

### VendorAvailability
- Tracks vendor availability by date
- Prevents double bookings

### Booking
- Links users to vendors for specific dates
- Tracks booking status and costs

## Deployment Options

### Free Hosting
- **Backend**: Railway, Render, PythonAnywhere
- **Frontend**: Vercel, Netlify
- **Database**: Railway PostgreSQL, Supabase

### Production Setup
1. Update `ALLOWED_HOSTS` in settings.py
2. Set `DEBUG = False`
3. Configure PostgreSQL database
4. Set up static file serving
5. Configure CORS for production domains

## Service Categories

- 🍽️ Catering
- 📸 Photography
- 🏛️ Venues
- 🎨 Decoration
- 🎤 MC Services
- 🎵 DJ Services
- 🚐 Transport

## Sample Vendors (Seeded Data)

1. **Mama's Kitchen** - Catering (KES 80,000)
2. **Lens Masters** - Photography (KES 50,000)
3. **Garden Paradise** - Venue (KES 60,000)
4. **Blooms & Drapes** - Decoration (KES 45,000)
5. **Joe the Host** - MC (KES 30,000)
6. **SoundWave Pro** - DJ (KES 35,000)

## Future Enhancements

- Payment gateway integration
- Vendor dashboard
- Advanced AI with GPT integration
- Mobile app (React Native)
- Email notifications
- Review system
- Multi-language support

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

## License

MIT License - feel free to use for personal or commercial projects.

---

**Event-Safi** - Making event planning effortless with AI! 🎉
# event-safi
