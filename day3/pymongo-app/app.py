from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

# Flask app
app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and insert data into MongoDB
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    age = int(request.form['age'])

    # Insert user data into MongoDB
    collection.insert_one({"name": name, "age": age})

    # Redirect to the home page after successful insertion
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
