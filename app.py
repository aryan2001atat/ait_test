from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
