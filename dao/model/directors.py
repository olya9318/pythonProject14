from marshmallow import Schema, fields
from setup_db import db


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __str__(self):
        return self.name

