# Importing necessary Libraries:
from flask import Flask, render_template, request
import ezgmail

# Creating an instance of Flask class
app = Flask(__name__, template_folder='templates')   

# Creating a Home Page:
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

# Creating the Contact Us page:
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    else:
        ezgmail.send('archismansengupta2403@gmail.com', 'Test Subject', 'This is just a sample text.')


# Creating the Projects page:
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html')

# Running the Flask App:
if __name__ == '__main__':
    app.run( debug=True, port = 5000)