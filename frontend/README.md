# Frontend - Vue.js Application

This directory will contain the Vue.js frontend application for the Invoice System.

## Planned Features

- **Modern Vue.js 3** with Composition API
- **Vue Router** for navigation
- **Pinia** for state management
- **Tailwind CSS** or **Vuetify** for UI components
- **Axios** for API communication
- **Authentication** with JWT tokens
- **Responsive Design** for mobile and desktop

## Planned Structure

```
frontend/
├── src/
│   ├── components/         # Reusable Vue components
│   ├── views/             # Page components
│   ├── router/            # Vue Router configuration
│   ├── stores/            # Pinia stores
│   ├── services/          # API service layer
│   ├── utils/             # Utility functions
│   └── assets/            # Static assets
├── public/                # Public assets
├── package.json           # Node.js dependencies
├── vite.config.js         # Vite configuration
└── README.md             # Frontend documentation
```

## Planned Pages

- **Login/Register** - User authentication
- **Dashboard** - Overview of invoices and payments
- **Clients** - Client management
- **Invoices** - Invoice creation and management
- **Payments** - Payment tracking
- **Reports** - Analytics and reporting
- **Settings** - User preferences

## Development Setup (Future)

```bash
cd frontend
npm install
npm run dev
```

## API Integration

The frontend will communicate with the Django backend API at:
- **Development**: `http://localhost:8000/api/v1/`
- **Production**: Configure in environment variables

This frontend will be developed in parallel with the backend features.
