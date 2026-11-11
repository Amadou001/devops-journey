import os
from flask import Flask

app = Flask(__name__)

# Read the environment name from an environment variable.
# If it's not set, default to "development".
APP_ENV = os.environ.get("APP_ENV", "development")

# Debug mode only in development, never in production.
DEBUG = APP_ENV == "development"

@app.route("/")
def home():
    return f"Running in: {APP_ENV} | Debug mode: {DEBUG}\n"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=DEBUG)
