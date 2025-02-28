# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, User, Renter, Landlord, init_db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'equitrack.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Forms
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    account_type = SelectField('Account Type', choices=[('renter', 'Renter'), ('landlord', 'Landlord')], validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RenterProfileForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired()])
    credit_score = IntegerField('Credit Score', validators=[DataRequired()])
    annual_income = FloatField('Annual Income', validators=[DataRequired()])
    occupation = StringField('Occupation')  # Optional
    years_rented = IntegerField('Years Rented', validators=[DataRequired()])
    submit = SubmitField('Save Profile')

class LandlordProfileForm(FlaskForm):
    real_estate_company = StringField('Real Estate Company', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    contact_info = StringField('Contact Info', validators=[DataRequired()])
    locations = StringField('Locations (comma-separated)', validators=[DataRequired()])
    submit = SubmitField('Save Profile')

class PropertyForm(FlaskForm):
    address = StringField('Property Address', validators=[DataRequired()])
    rent = IntegerField('Rent', validators=[DataRequired()])
    submit = SubmitField('Add Property')

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, 
                    password=generate_password_hash(form.password.data), 
                    account_type=form.account_type.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Login failed. Check your credentials.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('logout'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if current_user.account_type == 'renter':
        renter = Renter.query.get(current_user.id)
        form = RenterProfileForm()
        if form.validate_on_submit() and not renter.age:  # Only if not already set
            renter.age = form.age.data
            renter.credit_score = form.credit_score.data
            renter.annual_income = form.annual_income.data
            renter.occupation = form.occupation.data
            renter.years_rented = form.years_rented.data
            db.session.commit()
            flash('Profile updated successfully!', 'success')
        return render_template('renter_dashboard.html', renter=renter, form=form)
    else:
        landlord = Landlord.query.get(current_user.id)
        form = LandlordProfileForm()
        property_form = PropertyForm()
        if form.validate_on_submit() and not landlord.real_estate_company:
            landlord.real_estate_company = form.real_estate_company.data
            landlord.name = form.name.data
            landlord.contact_info = form.contact_info.data
            landlord.locations = form.locations.data
            db.session.commit()
            flash('Profile updated successfully!', 'success')
        if property_form.validate_on_submit():
            # Placeholder for property logic (expand later)
            flash('Property added successfully!', 'success')
        return render_template('landlord_dashboard.html', landlord=landlord, form=form, property_form=property_form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    init_db(app)  # Initialize database
    with app.app_context():
        test_user = User(email='test@example.com', password=generate_password_hash('password123'), account_type='renter')
        db.session.add(test_user)
        db.session.commit()
        print("Database tables:", db.engine.table_names())
    app.run(debug=True)