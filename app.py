
from flask import Flask, render_template
from extensions import db
from config import Config
import models

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def strona_glowna():
    return render_template("index.html")


with app.app_context():
    db.create_all()
    print("BAZA DANYCH UTWORZONA:")
    print(db.engine.url.database)


if __name__ == "__main__":
    app.run(debug=True)
