@echo off
REM Invoice System Setup Script for Windows

echo 🚀 Setting up Invoice System...

REM Setup Backend
echo 📦 Setting up Backend...
cd backend

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo 📥 Installing backend dependencies...
pip install -r requirements.txt

REM Go back to main directory
cd ..

REM Copy environment file
if not exist ".env" (
    echo ⚙️ Creating environment file...
    copy .env.example .env
    echo 📝 Please edit .env file with your configuration
)

REM Create necessary directories
echo 📁 Creating directories...
if not exist "backend\logs" mkdir backend\logs
if not exist "backend\static" mkdir backend\static
if not exist "backend\media" mkdir backend\media

echo ✅ Backend setup complete!
echo.
echo Frontend setup will be added when Vue.js frontend is implemented.
echo.
echo Next steps:
echo 1. Edit .env file with your database credentials
echo 2. cd backend
echo 3. Run: python manage.py migrate
echo 4. Run: python manage.py createsuperuser
echo 5. Run: python manage.py runserver
echo.
echo Or use Docker:
echo docker-compose up --build

pause
