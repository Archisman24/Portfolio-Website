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
        email_id = request.form.get('email_id')
        name = request.form.get('name')
        if request.form.get('recruiter') == 'YES':
            recruiter = 'He is a Recruiter.'
        else:
            recruiter = 'He is not a Recruiter.'
            message = f"This message is from {name}.'\n{recruiter}. \n Message : {request.form.get('query')}"

        ezgmail.send('archismansengupta02@gmail.com', "Notification from Portfolio website", message)

        return render_template('contact.html')
        


# Creating the Projects page:
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html')
    
# Running the Flask App:
if __name__ == '__main__':
    app.run( debug=True, port = 5000)