from flask import Flask, render_template, request
from config import Config
import threading, webbrowser
from forms import AccountCreationForm, DemographicForm


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/home/', methods=['GET','POST'])
def renderHome():
    '''
    Renders a viewable web application on your port:
    http://127.0.0.1:5000/home
    '''

    return (render_template('home.html') )

@app.route('/accountcreation/', methods=['GET', 'POST'])
def renderAccountCreation():
    if request.method == "GET":
        form = AccountCreationForm()
        return (render_template('accountcreation.html', form = form))
    elif request.method == "POST":

        return(redirect("http://127.0.0.1:5000/demographics/"))

@app.route('/demographics/', methods=["GET", "POST"])
def renderDemographicForm():
    if request.method == "GET":
        form = DemographicForm()
        return(render_template('demographic.html', form = form))



if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/home'
    threading.Timer(2, lambda: webbrowser.open(url, new=1)).start()
    app.run()
