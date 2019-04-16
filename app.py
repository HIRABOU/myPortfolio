from flask import Flask, request, render_template, redirect, url_for, flash, session

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/works')
def works():
    return render_template('photograph.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
