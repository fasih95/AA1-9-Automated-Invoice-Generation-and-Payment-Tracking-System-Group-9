# Vue.js Frontend for AA1-9 Invoice System

This is the Vue.js frontend application for the AA1-9 Automated Invoice Generation and Payment Tracking System.

## 🚀 Tech Stack

- **Vue.js 3** - Progressive JavaScript framework with Composition API
- **Vite** - Next generation frontend tooling
- **Vue Router 4** - Official router for Vue.js
- **Pinia** - Intuitive, type safe state management
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API communication
- **Chart.js** - Data visualization library
- **Headless UI** - Unstyled, accessible UI components

## 📁 Project Structure

```
src/
├── assets/          # Static assets (images, styles)
├── components/      # Reusable Vue components
├── services/        # API services and HTTP client
├── stores/          # Pinia state management stores
├── views/           # Page-level components (routes)
│   ├── auth/        # Authentication pages
│   ├── clients/     # Client management pages
│   ├── invoices/    # Invoice management pages
│   ├── payments/    # Payment tracking pages
│   ├── reports/     # Reporting and analytics pages
│   └── users/       # User management pages
├── router/          # Vue Router configuration
├── App.vue          # Main application component
└── main.js          # Application entry point
```

## 🛠️ Development

### Prerequisites

- Node.js 18+ and npm 8+
- Backend API running on `http://localhost:8000`

### Getting Started

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```

3. **Access the application:**
   - Frontend: http://localhost:3000
   - API Proxy: http://localhost:3000/api (proxies to backend)

### Available Scripts

- `npm run dev` - Start development server with hot reload
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint for code linting
- `npm run format` - Format code with Prettier
- `npm test` - Run unit tests with Vitest
- `npm run test:coverage` - Run tests with coverage report

## 🔧 Configuration

### API Proxy

The development server is configured to proxy API requests to the backend:
- `/api/*` → `http://localhost:8000/api/*`

## 🏗️ Architecture

### State Management

- **Pinia stores** for global state management
- **Auth store** for user authentication and permissions
- **Modular stores** for different features (invoices, clients, etc.)

### Routing

- **Protected routes** with authentication guards
- **Permission-based access** control
- **Role-based routing** for different user types

### Components

- **Composition API** for better code organization
- **Reusable components** with props and slots
- **Tailwind CSS** for styling

## 🚢 Deployment

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up frontend
```

### Production Build

```bash
npm run build
```

## 🔗 Integration

### Backend Integration

The frontend integrates with the Django REST API:

- **JWT authentication** with automatic token refresh
- **Axios interceptors** for request/response handling
- **Error handling** with user-friendly messages

### Key Features

- **Dashboard** with analytics and quick actions
- **Invoice Management** with PDF generation
- **Client Management** with contact information
- **Payment Tracking** with status updates
- **User Management** with role-based access
- **Responsive Design** for desktop and mobile

---

**Note:** This frontend is part of the AA1-9 Invoice Generation and Payment Tracking System. Make sure the backend API is running before starting frontend development.
