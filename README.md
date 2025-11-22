# little-lemon-backend
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Little Lemon Backend API", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", '', 12)
content = """
Project Overview:
This project is a backend API for the Little Lemon restaurant.
It allows:
- Viewing and creating menu items
- Booking tables (authenticated users only)
- User registration and JWT authentication
Built with Django REST Framework and MySQL database.

Setup Instructions:
1. Clone the repository:
   git clone <your-github-repo-url>
   cd little_lemon

2. Activate virtual environment:
   .\\venv\\Scripts\\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Make migrations and migrate:
   python manage.py makemigrations
   python manage.py migrate

5. Run the server:
   python manage.py runserver

API Endpoints:

1. User Registration
POST /api/registration/
Body:
{
  "username": "testuser",
  "password": "TestPassword123",
  "email": "testuser@example.com"
}

2. JWT Token
POST /api/token/
Body:
{
  "username": "testuser",
  "password": "TestPassword123"
}

3. Menu API (Public)
GET /api/menu/
POST /api/menu/
Body Example:
{
  "name": "Spaghetti Carbonara",
  "description": "Classic Italian pasta with creamy sauce",
  "price": 12.50
}

4. Booking API (Requires JWT)
GET /api/bookings/
POST /api/bookings/
Header: Authorization: Bearer <access_token>
POST Body Example:
{
  "user": 1,
  "date": "2025-12-01",
  "time": "18:30",
  "num_guests": 4,
  "special_request": "Window seat"
}

5. JWT Refresh Token
POST /api/token/refresh/
Body:
{
  "refresh": "<refresh_token>"
}

Notes:
- Menu API does not require authentication.
- Booking API requires JWT token in header.
- Use Postman or Insomnia to test APIs.
"""

pdf.multi_cell(0, 8, content)

pdf.output("Little_Lemon_API.pdf")
print("PDF generated successfully!")
