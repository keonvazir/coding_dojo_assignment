from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

# dbs = "Users"

@app.route("/")
def root():
    return redirect("/users")

@app.route('/users')
def users():
    mysql = connectToMySQL("Users")
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    print(users)
    return render_template("index.html", users=users)

@app.route('/users/new', methods=['GET'])
def new():
    return render_template("new.html")

@app.route('/users/create', methods=["POST"])
def create():
    print(request.form['fname'])
    print(request.form['lname'])
    print(request.form['email'])
    mysql = connectToMySQL("Users")
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());"

    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"],
    }
 
    # users_id = connectToMySQL("Users")
    user_id = mysql.query_db(query, data)
    return redirect("/users/"+str(user_id))

@app.route('/users/<user_id>', methods=["GET"])
def show(user_id):
    mysql = connectToMySQL("Users")
    query = "SELECT * FROM users WHERE id = %(uid)s;"
    data = {
        "uid": user_id,
    }
   
    user = mysql.query_db(query, data)
    print(user)
    return render_template("show.html", user=user[0])


@app.route("/users/<user_id>/destroy")
def delete(user_id):
     mysql = connectToMySQL("Users")
     query = "DELETE from users WHERE id = %(uid)s"
     data = {
         "uid": user_id
     }
     mysql.query_db(query, data)
     return redirect("/users")

@app.route("/users/<user_id>/edit", methods=["GET"])
def edit(user_id):
    mysql = connectToMySQL("Users")
    query = "SELECT * from users WHERE id = %(uid)s"
    data = {
        "uid": user_id
    }

    user = mysql.query_db(query, data)
    return render_template("edit.html", user=user[0])

@app.route("/users/<user_id>/edit", methods=["POST"])
def edit_user(user_id):
    mysql = connectToMySQL("Users")
    query = "UPDATE users SET first_name = %(fn)s, last_name = %(ln)s, email = %(em)s WHERE id = %(uid)s"

    data = {
        "fn": request.form['fname'],
        "ln": request.form['lname'],
        "em": request.form['email'],
        "uid": user_id
    }

    mysql.query_db(query, data)
    return redirect("/users"+str(user_id))

if __name__ == "__main__":
    app.run(debug=True)