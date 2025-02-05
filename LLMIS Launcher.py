# Kim T. DIAZ, Mara T. CHUA, Camille VENTOSO
from flask import Flask, render_template
import webview

app = Flask(__name__, static_folder='./static', template_folder='./templates')

@app.route('/')
def home():
    title = "Home"
    return render_template('home.html', title=title)

@app.route('/document')
def document():
    title = "Documentation"
    return render_template('document.html', title=title)

@app.route('/manual')
def video():
    title = "User Manual"
    return render_template('manual.html', title=title)

@app.route('/demovids')
def webapp():
    title = "Demo Videos"
    return render_template('demovids.html', title=title)

webview.create_window('LLMIS Launcher', app)

if __name__ == "__main__":
    #app.run(debug=True) FOR TEST ENVIRONMENT
    webview.start()