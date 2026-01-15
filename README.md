Employee API – HabotConnect

I built this backend API to manage employees in a company. It’s simple but covers CRUD operations, JWT authentication, filtering, and pagination. This project helped me brush up on RESTful design, validation, and testing.

🌐 Live Demo

Check it out here:
Live URL Placeholder

"".

💻 Quick Setup

Clone the repo:

git clone https://github.com/<your-username>/employee-api-habot.git
cd employee-api-habot


Create & activate virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create superuser (optional, for admin panel):

python manage.py createsuperuser


Run the server:

python manage.py runserver


Admin panel: http://127.0.0.1:8000/admin/ — handy to check employees created via API.

📌 API Overview

Auth (JWT)

POST /api/token/ → get access & refresh tokens

POST /api/token/refresh/ → refresh access token

Employees

GET /api/employees/ → list employees (supports filtering & pagination)

POST /api/employees/ → create a new employee

GET /api/employees/{id}/ → retrieve a single employee

PUT /api/employees/{id}/ → update employee

DELETE /api/employees/{id}/ → delete employee

All endpoints require JWT access token in the Authorization header.

📸 Postman Demo Placeholders

JWT Authentication


Create Employee


List Employees (Pagination & Filtering)


Retrieve Employee


Update Employee


Delete Employee


Replace the placeholders with your actual screenshots before sharing.

🧪 Running Tests
python manage.py test


Tests cover:

Authenticated CRUD operations

Duplicate email and validation errors

Employee not found errors

Pagination & filtering

⚡ Notes / Pro Tips

Include JWT access token in Authorization: Bearer <token> header for all requests.

Filter employees: /api/employees/?department=HR&role=Developer

Pagination example: /api/employees/?page=2

Optional: Add ordering = ['id'] in view for consistent pagination results.

Quick personal note: I learned a lot about handling JWT auth in DRF and filtering/pagination quirks while building this.