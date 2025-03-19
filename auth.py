from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb+srv://manisaikunta2211:gBHzTK1T0Mw1gvbE@cluster0.jqmkv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Use your actual MongoDB connection string
db = client['Attandance_user']  # Replace with the database name
users_collection = db['att_user_data']  # Replace with your collection name

# Create a Blueprint for authentication routes
auth = Blueprint('auth', __name__)

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query MongoDB to check if the user exists
        user = users_collection.find_one({"username": username})

        if user and check_password_hash(user['password'], password):
            session['user'] = username  # Store the username in the session to track login
            return redirect(url_for('index'))  # Redirect to main page or another page after login
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

# Registration route (optional)
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('auth.register'))

        # Check if user already exists
        existing_user = users_collection.find_one({"username": username})
        if existing_user:
            flash('Username already exists', 'danger')
            return redirect(url_for('auth.register'))

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Insert new user into the database
        users_collection.insert_one({
            "username": username,
            "password": hashed_password
        })
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('reg.html')  # Ensure you have a register.html template
