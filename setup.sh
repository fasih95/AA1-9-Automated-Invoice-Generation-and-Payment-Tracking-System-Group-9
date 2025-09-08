#!/bin/bash

# Invoice System Setup Script

echo "🚀 Setting up Invoice System..."

# Setup Backend
echo "📦 Setting up Backend..."
cd backend

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing backend dependencies..."
pip install -r requirements.txt

# Go back to main directory
cd ..

# Copy environment file
if [ ! -f ".env" ]; then
    echo "⚙️ Creating environment file..."
    cp .env.example .env
    echo "📝 Please edit .env file with your configuration"
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p backend/logs
mkdir -p backend/static
mkdir -p backend/media

echo "✅ Backend setup complete!"
echo ""
echo "Frontend setup will be added when Vue.js frontend is implemented."
echo ""
echo "Next steps:"
echo "1. Edit .env file with your database credentials"
echo "2. cd backend"
echo "3. Run: python manage.py migrate"
echo "4. Run: python manage.py createsuperuser"
echo "5. Run: python manage.py runserver"
echo ""
echo "Or use Docker:"
echo "docker-compose up --build"
