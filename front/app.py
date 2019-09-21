from flask import Flask, render_template
from config import Config
import threading, webbrowser
from forms import AccountCreationForm


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/home/', methods=['GET','POST'])
def renderHome():
    '''
    Renders a viewable web application on your port:
    http://127.0.0.1:5000/home
    '''

    return (render_template('home.html') )

@app.route('/register/', methods=['GET', 'POST'])
def renderAccountCreation():
    form = AccountCreationForm()

    return (render_template('accountCreation.html', form = form))


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/home'
    threading.Timer(2, lambda: webbrowser.open(url, new=1)).start()
    app.run()
