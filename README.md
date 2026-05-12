💳 Django Installment Management System
A web-based application built with Django for managing customer installment payments. The system allows you to register customers, track payment plans, record installment payments, search by customer name, and print professional invoices.

✨ Features

Add Customers — Register customers with their name, phone number, total amount, and installment amount
Auto-Calculate Remaining Balance — The remaining amount is automatically computed from the total and installments paid
Search by Name — Quickly find any customer by searching their name
Update Installments — Add new installment payments by editing the customer record
Print Invoice — Generate a printable invoice showing customer name, date, total amount, installment paid, and remaining balance


🛠️ Tech Stack

Backend: Python 3.x, Django 4.x
Frontend: HTML5, CSS3, Bootstrap 5
Database: SQLite (default) / PostgreSQL (optional)
Other: Django Template Engine, Django ORM

⚙️ Installation & Setup
1. Clone the Repository
bashgit clone https://github.com/Firas-coder/installment-system.git
cd installment-system
2. Create a Virtual Environment
bashpython -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. Install Dependencies
bashpip install -r requirements.txt
4. Apply Migrations
bashpython manage.py makemigrations
python manage.py migrate
5. Create a Superuser (Optional)
bashpython manage.py createsuperuser
6. Run the Development Server
bashpython manage.py runserver
Visit: http://127.0.0.1:8000

📋 How to Use
➕ Add a Customer
Go to /customers/add/ and fill in:

Full Name
Phone Number
Total Amount
Installment Amount

The Remaining Balance is calculated automatically.
🔍 Search for a Customer
Go to /customers/search/ and type the customer's name. Results will appear instantly.
💸 Add an Installment Payment
Open the customer's detail page and click Edit to record a new installment. The remaining balance updates automatically.
🧾 Print Invoice
On the customer's detail page, click Print Invoice to open a printable invoice containing:

Customer Name
Date
Total Amount
Installment Amount Paid
Remaining Balance


🗃️ Database Model Overview
pythonclass Customer(models.Model):
    name         = models.CharField(max_length=100)
    phone        = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Remaining = models.FloatField(default=0)  
    status = models.CharField(max_length=100, default='Unpaid', choices=status_choices)
    paid_date = models.DateField(auto_now_add=True)

    @property
    def remaining(self):
        return self.total_amount - self.paid_amount

📸 Screenshots

(Add screenshots of your app here after deployment)

PageDescriptionCustomer ListView all registered customersAdd CustomerRegister a new customerSearchFind customers by nameInvoicePrintable payment summary


👨‍💻 Author
Firas

GitHub: @Firas-coder
