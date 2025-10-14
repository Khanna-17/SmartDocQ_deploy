# SmartDocQ with GenAI

This project is an intelligent document assistant that allows users to upload documents and ask questions about their content, powered by a React frontend and a Python (Flask) backend with Google's Gemini AI.

## 🌐 Live Demo

- **Frontend**: https://smartdocq-gfzj.onrender.com
- **Backend API**: https://smartdocq-backend.onrender.com

## 📋 Admin Access

- **Email**: admin@smartdocq.com
- **Password**: Admin@123

## 🚀 Deployment

### Production Environment Variables

#### Backend (Render)
```env
FRONTEND_URL=https://smartdocq-gfzj.onrender.com
SECRET_KEY=your_production_secret
GOOGLE_API_KEY=your_google_api_key
DATABASE_URL=your_postgres_connection_string
ADMIN_EMAIL=admin@smartdocq.com
ADMIN_PASSWORD=Admin@123
AI_ENABLED=true
```

#### Frontend (Render)
```env
VITE_API_BASE=https://smartdocq-backend.onrender.com
VITE_GOOGLE_CLIENT_ID=your_google_oauth_client_id
```

---

## API Documentation

This section details how to interact with the backend API.

### Authentication

**`POST /api/register`**
* **Description**: Creates a new user account.
* **Body (JSON)**:
    ```json
    {
      "name": "Test",
      "email": "test@gmail.com",
      "password": "1234"
    }
    ```
* **Success Response (201 Created)**:
    ```json
    { "message": "Registered successfully!" }
    ```

**`POST /api/login`**
* **Description**: Authenticates a user and returns a session token (JWT).
* **Body (JSON)**:
    ```json
    {
      "email": "test@gmail.com",
      "password": "1234"
    }
    ```
* **Success Response (200 OK)**:
    ```json
    { "token": "your_jwt_goes_here" }
    ```

### Core Functionality

**`POST /api/ask`**
* **Description**: Submits a user's question and a document's text to the AI model. **Requires authentication**.
* **Headers**:
    * `Authorization`: `Bearer <YOUR_JWT_TOKEN>`
* **Body (JSON)**:
    ```json
    {
      "question": "What is binary search?",
      "context": "Binary search is an efficient algorithm..."
    }
    ```
* **Success Response (200 OK)**:
    ```json
    {
      "answer": "Binary search is a fast search algorithm...",
      "citations": []
    }
    ```
---

## Configuration

To run this project, you will need to set up the following environment variables.

#### **Backend (`backend/.env`)**
* `SECRET_KEY`: A strong, random string used for signing secure session tokens (JWTs).
* `GOOGLE_API_KEY`: Your API key from Google AI Studio for accessing the Gemini model.
* `DATABASE_URL`: The full connection string for your PostgreSQL database (e.g., `postgresql://user:pass@host/db`).
* `VITE_GOOGLE_CLIENT_ID`: Your Google OAuth Client ID, used by the backend to verify tokens from the Google Sign-In flow.

#### **Frontend (`smartdoc-frontend/.env`)**
* `VITE_API_URL`: The full URL where the backend server is running (e.g., `http://localhost:5001` for development).
* `VITE_GOOGLE_CLIENT_ID`: Your Google OAuth Client ID, used by the frontend to display the Google Sign-In button.
