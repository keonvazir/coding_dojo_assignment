from flask import Flask, request, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    return render_template('index.html', test='This works')

@app.route('/a')
def pagea():
    return render_template('a.html', test="a works")

@app.route('/b')
def pageb():
    return render_template('b.html', test="b works")

@app.route('/a1')
def pagea1():
        return render_template('a1.html', test="a1 works")

@app.route('/a2')
def pagea2():
    return render_template('a2.html', test="a2 works")

@app.route('/b1')
def pageb1():
    return render_template('b1.html', test="b1 works")

@app.route('/b2')
def pageb2():
    return render_template('b2.html', test="b2 works")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  
