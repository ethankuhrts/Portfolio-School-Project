from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    gallery = [
        {'title': 'project1', 'img': 'andr2.png'},
        {'title': 'project2', 'img': 'andr2.png'},
        {'title': 'project3', 'img': 'andr2.png'},
        {'title': 'project4', 'img': 'andr2.png'},
        {'title': 'project5', 'img': 'andr2.png'},
        {'title': 'project6', 'img': 'andr2.png'},
    ]
    return render_template('portfolio.html', gallery=gallery)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)