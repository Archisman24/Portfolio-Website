# Importing necessary Libraries:
from flask import Flask, render_template, request

# Creating an instance of Flask class
app = Flask(__name__, template_folder='templates')   

## Basic Pages:

# Creating a Home Page:
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

# Creating the Contact Us page:
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

# Creating the Projects page:
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html')

## Pages related to Projects:

# Creating the Students.com page:
@app.route('/students')
def students():
    return render_template('students.html')

# Creating the Kitting Project page:
@app.route('/kitting')
def kitting():
    return render_template('kitting.html')

## Pages related to Blog Page:


    
# Running the Flask App:
if __name__ == '__main__':
    app.run( debug=True, port = 5000)