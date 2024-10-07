from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

# Add more routes here as needed
# For example:
@app.route('/about')
def about():
    return "This is the about page."

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)

