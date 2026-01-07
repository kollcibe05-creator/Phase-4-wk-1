from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemyimport CheckConstraint

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)



###models ~ must import serializermixin, have serialization-proxy, serialize_rules, cascades

class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    serialize_rules = ("-hero_powers.hero",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    hero_powers = db.relationship("HeroPower", back_populates="hero", cascade="all, delete-orphan")
    powers = association_proxy(
        "hero_powers", "power", creator=lambda power_obj: HeroPower(power=power_obj)
    )
    def __repr__(self):
        return f"<Hero {self.id}, {self.name}, {self.super_name}>"
class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    serialize_rules = ("-hero_powers.power",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String(>=20))

    __table_args__ = (
        db.CheckConstraint("length(description) >= 20", name = "minimum_length")
    ) 

    hero_powers = db.relationship("HeroPower", back_populates="power", cascade="all, delete-orphan")
    heroes = association_proxy(
        "hero_powers", "hero", creator=lambda hero_obj: HeroPower(hero=hero_obj)
    )
    def __repr__(self):
        return f"<Power {self.id}, {self.name}, {self.description}>"

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"

    serialize_rules = ("-hero.hero_powers","-power.hero_powers",)

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))
    __table_args__ = (
        db.CheckConstraint("strength IN ('Strong', 'Weak', 'Average')", name = "valid_level_of_strength")
    ) 

    power = db.relationship('Power', back_populates="hero_powers")
    
    hero = db.relationship("Hero", back_populates="hero_powers")

    def __repr__(self):
        return f"<HeroPower {self.id}, {self.strength}, {self.hero_id}, {self.power_id}>" 



