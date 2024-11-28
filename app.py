from flask import Flask
from routes import register_routes

# Initialize Flask app
app = Flask(__name__)

# Register all routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
