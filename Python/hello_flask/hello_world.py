from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')
def index():
    return render_template('index.html', phrase="Hello", times=5)
@app.route('/<name>/<times>')
def hello_person(name, times):
    print("*"*80)
    print("in hello_person function")
    return render_template("name.html", some_name = name, num_times = int(times))

@app.route('/lists')
def render_lists():
    student_info = [
        {'name': "Michael", "age": 35},
        {'name': "John", "age": 30},
        {'name': "Mark", "age": 25},
        {'name': "KB", "age": 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

@app.route('/users')
def render_users():
    person_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("users.html", persons = person_info)

if __name__ == "__main__":
    app.run(debug = True)