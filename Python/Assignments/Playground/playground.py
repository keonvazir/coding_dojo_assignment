from flask import Flask, render_template  
app = Flask(__name__)    
@app.route('/')
def index():
    return render_template('index.html', num=2, color= "")

@app.route('/<num>/<color>')
def num_boxes(num, color):
    print("*"*80)
    print("in num_boxes function")
    return render_template("num.html", num = int(num), color = color)

if __name__ == "__main__":
    app.run(debug = True)