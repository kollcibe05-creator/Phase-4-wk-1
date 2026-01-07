from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from models import ,,,


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = flask_migrate
app.json.compact = False


migrate = Migrate()

db.init_app(app)



###Routes###



if __name__ == "__main__":
    app.run(port=5555, debug=True)