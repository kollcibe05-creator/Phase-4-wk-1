from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)



###models ~ must import serializermixin, have serialization-proxy, serialize_rules, cascades

class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

class HeroPower(db.model, SerializerMixin):
    __tablename__ == "hero_powers"

    serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeinKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeinKey("powers.id"))
    



