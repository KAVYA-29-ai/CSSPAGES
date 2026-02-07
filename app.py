from flask import Flask 
from flask import render_template

app = Flask(__name__)
@app.route('/home')
def home():
    return render_template('home.html')
    #return "Hello, World! This is home page"

@app.route('/about')
def about(): 
    return render_template('about.html')
    #return "This page is about page !" 

@app.route('/submit') 
def submit():
    return render_template('submit.html')
    #return "This page is about page !" 

if __name__ == '__main__':
    app.run(debug=True)
