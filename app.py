from flask import Flask, render_template
from config import Config
import threading, webbrowser


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/home/', methods=['GET','POST'])
def renderHome():
    '''
    Renders a viewable web application on your port:
    http://127.0.0.1:5000/home
    '''

    return (render_template('index.html') )

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/home'
    threading.Timer(2, lambda: webbrowser.open(url, new=1)).start()
    app.run()
