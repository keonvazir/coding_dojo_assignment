from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='lkjhfdfsdfs'



@app.route('/')
def index():

    if 'count' not in session:
        session['count']=0
        #else
    session['count']+=1
    return render_template("index.html", count= session['count'])

@app.route('/addtwo')
def addtwo():
    session['count']+=1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)