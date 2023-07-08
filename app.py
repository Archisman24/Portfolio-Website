# Importing necessary Libraries:
from flask import Flask, render_template, request

# Creating an instance of Flask class
app = Flask(__name__)   

# Creating a Home Page:
@app.route('/')
def home():
    return render_template('home.html')

# Running the Flask App:
if __name__ == '__main__':
    app.run( debug=True, port = 5000)