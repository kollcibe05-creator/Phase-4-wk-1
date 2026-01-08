from flask import Flask, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, HeroPower, Power, Hero


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


migrate = Migrate(app, db)

db.init_app(app)



###Routes###
@app.route("/")
def index():
    return "<h1>Welcome to the main route</h1>"

@app.route("/heroes")
def heroes():
    heroes = []  
    for hero in Hero.query.all():
        response_body = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        }
        heroes.append(response_body)
    response = make_response(jsonify(heroes), 200)
    return response

@app.route("/heroes/<int:id>")
def get_heroes(id):
    hero = Hero.query.filter(Hero.id == id).first()

    if hero:
        hero_dict = hero.to_dict()
        response = make_response(jsonify(hero_dict), 200)
        return response
    else:
        response_body = {
            "error": "Hero not found"
        }    
        response = make_response(jsonify(response_body), 404)
        return response



@app.route("/powers")
def powers():
    powers  = []
    for power in Power.query.all():
        response_body = {
            "description": power.description,
            "id": power.id,
            "name": power.name
        }
        powers.append(response_body)
    response = make_response(jsonify(powers), 200)
    return response


@app.route("/powers/<int:id>", methods=["GET", "PATCH"])
def get_powers(id):
    power = Power.query.filter(Power.id == id).first()
    if request.method == "GET":
        if power:
            response_body = {
            "description": power.description,
            "id": power.id,
            "name": power.name
        }
            response = make_response(jsonify(response_body), 200)
            return response
        else:
            response_body = {
                "error": "Power not found"
            }    
            response = make_response(jsonify(response_body), 404)
            return response
    elif request.method == "PATCH":
        if power:
            # instead of request.form.get()
            data = request.get_json()   
            for attr in data:
                setattr(power, attr, data.get(attr))
            db.session.add(power)
            db.session.commit()
            power_dict = {
                "description": power.description,
                "id": power.id,
                "name": power.name
            }       

            response = make_response(jsonify(power_dict), 200) #, {"Content-Type": "application/json"}
            return response
        elif not power:
            response_body = {
                "error": "Power not found"
            }
            response = make_response(jsonify(response_body), 404)
            return response
        else:
            response_body = {
                "errors": ["validation errors"]
            }
            response = make_response(jsonify(response_body), 404)
            return response

@app.route("/hero_powers", methods=["GET", "POST"])
def post_hp():
    if request.method == "POST":
        data = request.get_json()
        try:
            new_hp = HeroPower(
                strength = data.get("strength"),
                power_id = data.get("power_id"),
                hero_id = data.get("hero_id"),
            )

            db.session.add(new_hp)
            db.session.commit()
            return make_response(jsonify(new_hp.hero.to_dict()), 201, {"Content-Type": "application/json"})
        except Exception as e:
            print(e)
            return make_response(jsonify({"errors": ["validation errors"]}), 400)








if __name__ == "__main__":
    app.run(port=5555, debug=True)