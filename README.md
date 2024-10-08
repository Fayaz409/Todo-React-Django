# ToDo App

This project is a ToDo application with a Django backend and a React frontend. The backend handles user authentication, note creation, and deletion, while the frontend provides a user interface for interacting with these features.

## Project Structure

- **Backend (Django)**
  - Handles user registration, authentication, note creation, and deletion.
  - API endpoints are created using Django REST framework.

- **Frontend (React)**
  - Provides a user interface to interact with the Django backend.
  - Uses Vite for development and build processes.
  - Includes features for registration, login, and note management.

## Getting Started

### Backend Setup

1. **Install Dependencies**

   Make sure you have Python installed. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Environment Variables**

   Create a `.env` file in the root directory of the backend with the following content:

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   ```

3. **Run Migrations**

   Apply the migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

4. **Run the Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The backend will be available at `http://localhost:8000`.

### Frontend Setup

1. **Install Node.js**

   Make sure you have Node.js and npm installed. Then, navigate to the frontend directory and install the required packages:

   ```bash
   cd frontend
   npm install
   ```

2. **Setup Environment Variables**

   Create a `.env` file in the `frontend` directory with the following content:

   ```env
   VITE_API_URL=http://localhost:8000
   ```

3. **Run the Development Server**

   Start the Vite development server:

   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`.

## Backend API Endpoints

- **User Registration**
  - `POST /api/user/register/`
  - Request Body: `{ "username": "your_username", "password": "your_password" }`

- **User Login**
  - `POST /api/token/`
  - Request Body: `{ "username": "your_username", "password": "your_password" }`
  - Response: `{ "access": "your_access_token", "refresh": "your_refresh_token" }`

- **Note List & Create**
  - `GET /api/notes/`
  - `POST /api/notes/`
  - Request Body: `{ "title": "Note Title", "content": "Note Content" }`

- **Note Delete**
  - `DELETE /api/notes/delete/<int:pk>/`

## Frontend Features

- **Registration**: Create a new user account.
- **Login**: Authenticate and obtain access tokens.
- **Notes Management**: Create and delete notes.

## Dependencies

### Backend

- Django
- Django REST Framework
- djangorestframework-simplejwt

### Frontend

- React
- Vite
- Axios
- React Router DOM
- Tailwind CSS

## Troubleshooting

- **Validation Errors**: Ensure all required fields are included and correctly named.
- **500 Internal Server Error**: Check server logs for detailed error messages. Ensure that `queryset` or `get_queryset` is defined in views where needed.

## Contributing

Feel free to open issues or submit pull requests to improve this project. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
