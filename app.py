import os
import subprocess
import sys
import threading
from flask import Flask
from flask import render_template, abort
app = Flask(__name__)
app.debug = True

# function to call netcap.py script to capture traffic
def run_script():
    theproc = subprocess.Popen(['python', 'netcap.py'])
    theproc.communicate()


@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/basics')
def basics():
    return render_template('basics.html')

@app.route('/about')
def about():
    return render_template('about.html')
  
@app.route('/generate')
def generate():
    threading.Thread(target=lambda: run_script()).start()
    return render_template('processing.html')

@app.route('/is_done')
def is_done():
     hfile = "templates\itworked.html"
     if os.path.isfile(hfile):
         return render_template('itworked.html')
     else:
         abort(404)

if __name__ == "__main__":
    app.run()
