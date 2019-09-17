from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL("assign_pet")
    pets = mysql.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", all_pets=pets)

@app.route("/add", methods=["POST"])
def add_pet():
    print(request.form)
    mysql = connectToMySQL("assign_pet")
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(fn)s, %(gt)s, NOW(), NOW());"
    data = {
        "fn": request.form["fname"],
        "gt": request.form["gtype"],
    }
    db = connectToMySQL("assign_pet")
    new_pets_id = mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)