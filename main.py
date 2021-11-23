from flask import Flask, render_template
import os
from dotenv import load_dotenv

import queries

app = Flask(__name__)
load_dotenv()


@app.route("/")
def index():

    users = queries.get_all_users()

    return render_template(
        "main.html",
        users=users,
    )


if __name__ == "__main__":
    app.run(debug=True)
