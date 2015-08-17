"""app.py: Create a web app that will run locally on port 5000 by default.
           Will provide info and monitoring functionality on the web pages."""

# Import os, subprocess and sys libraries to call other scripts.
# Import threading to do multi-threading.
# Import Flask to use the micro framework for the app. 
import os
import subprocess
import sys
import threading
from flask import Flask
from flask import render_template, abort

# Initiliaze Flask app and use debugging.
app = Flask(__name__)
app.debug = True

# Function to call netcap.py script for traffic capturing.
def run_script():
    theproc = subprocess.Popen(['python', 'netcap.py'])
    theproc.communicate()

# Display index.html template under the root level. 
@app.route('/')
def index():
    return render_template('index.html')
 
# Display basics.html under basics.
@app.route('/basics')
def basics():
    return render_template('basics.html')

# Display about.html under about.
@app.route('/about')
def about():
    return render_template('about.html')

# Display processing.html under generate.  
@app.route('/generate')
def generate():
    threading.Thread(target=lambda: run_script()).start()
    return render_template('processing.html')

# Display itworked.html under is_done.
# Check to see if path of file is valid.
@app.route('/is_done')
def is_done():
     hfile = "templates\itworked.html"
     if os.path.isfile(hfile):
         return render_template('itworked.html')
     else:
         abort(404)

# Start the web app locally on the default port (5000).
if __name__ == "__main__":
    app.run()
