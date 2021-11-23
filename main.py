from flask import Flask
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


@app.route("/")
def index():

    user = os.environ.get("UTILIZAATOR")
    parola = os.environ.get("PAROLA")

    return f"""
    <p>Date de conectare:</p>
    <p>User: {user}</p>
    <p>Parola: {parola}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
