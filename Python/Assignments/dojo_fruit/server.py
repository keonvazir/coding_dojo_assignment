from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_from_form = request.form['strawberry']
    raspberry_from_form = request.form['raspberry']
    apple_from_form = request.form['apple']
    return render_template("fruits.html", strawberry_on_template=strawberry_from_form, raspberry_on_template=raspberry_from_form, apple_on_template=apple_from_form)
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    