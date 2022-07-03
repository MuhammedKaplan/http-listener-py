# Creating a Web server using Python and Flask

# Import Libraries
from concurrent.futures import thread
from flask import Flask
from threading import Thread

# Define variables
start_state = False

# Create a Flask application
app = Flask('app')

# Create a route
@app.route('/start')
# Define a function for message
def start_process():
    global start_state 
    start_state = True
    print('Started')
    return 'Started'

@app.route('/stop')
def stop_process():
    global start_state
    start_state = False
    print('Stopped')
    return 'Stopped'


# Define a function for run server
def run_server():
    app.run(host='0.0.0.0', port=8080)


# Define a function for start server
def start_server():
    # Initialize a thread for app
    thread = Thread(target=app.run)
    # Start the thread
    thread.start()


    
