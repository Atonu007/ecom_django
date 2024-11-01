# 📚 Django E-commerce Project Documentation

This documentation provides an overview of the Django backend for the e-commerce project, including installation instructions, API endpoints, project structure, and features.


## ⚙️ Features
- **User Management**: Registration, login, and logout functionality.
- **Product Management**: CRUD operations for products (admin only).
- **Order Management**: Create and manage customer orders.
- **JWT Authentication**: Secure authentication for users.

## 📊 API Endpoints

### API Documentation
You can view the API documentation and test the endpoints using Swagger UI by visiting the following link:

- **Swagger API Documentation**: https://ecom-django.onrender.com/swagger/


---


## 🌐 Live Demo

You can try out the live demo of the e-commerce application at the following link:

- **Live Demo**: https://ecom-django.onrender.com/

Explore the features and functionality of the application, including user registration, product browsing, and order placement.


## 🛠️ Tech Stack

- **Backend Framework**: Django
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Token)
- **API Framework**: Django REST Framework
- **Containerization**: Docker
- **Hosted On**: Render (through docker) 

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed
- **pip** for package management
- **PostgreSQL** installed and running
- A code editor (e.g., Visual Studio Code, PyCharm)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Atonu007/ecom_django.git
   ```
    ```bash
   cd ecom
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

   ```
4. **Run the development server**:
   ```bash
   python manage.py runserver
    ```
Access the application at http://127.0.0.1:8000

## 🖼️ Note on Image Serving

Please note that if you are using free hosting services for this application, images may not be served correctly from the backend. This can happen due to restrictions on serving static files or due to CORS (Cross-Origin Resource Sharing) issues. 

For optimal performance and reliable image serving, consider using a dedicated cloud storage solution (e.g., AWS S3, Google Cloud Storage) for hosting images, and ensure your backend is configured to serve static files appropriately.






