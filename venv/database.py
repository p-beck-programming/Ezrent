# database.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    account_type = db.Column(db.String(50), nullable=False)  # 'landlord' or 'renter'

class Buyer(User):
    age = db.Column(db.Integer)
    credit_score = db.Column(db.Integer)  # Visible only to landlord
    annual_income = db.Column(db.Float)   # Visible only to landlord
    occupation = db.Column(db.String(100))  # Optional
    years_rented = db.Column(db.Integer)

class Seller(User):
    real_estate_company = db.Column(db.String(150))
    name = db.Column(db.String(150))
    contact_info = db.Column(db.String(150))
    locations = db.Column(db.String(500))  # Comma-separated list for simplicity

def init_db(app):
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Tables created:", db.engine.table_names())