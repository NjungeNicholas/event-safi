#!/bin/bash

echo "🎉 Setting up Event-Safi Platform..."

# Backend setup
echo "📦 Setting up Django backend..."
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
echo "Creating superuser (admin/admin)..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Seed database
python manage.py seed_data

echo "✅ Backend setup complete!"

# Frontend setup
echo "📦 Setting up React frontend..."
cd ../frontend

# Install Node dependencies
npm install

echo "✅ Frontend setup complete!"

echo "🚀 Setup complete! To start the application:"
echo "1. Backend: cd backend && python manage.py runserver"
echo "2. Frontend: cd frontend && npm start"
echo "3. Visit: http://localhost:3000"
