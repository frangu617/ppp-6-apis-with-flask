from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reptiles(db.Model):
    __tablename__ = 'reptiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    reptile_type = db.Column(db.String(80), nullable=False)

    def __init__(self, name, reptile_type):
        self.name = name
        self.reptile_type = reptile_type
        
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'reptile_type': self.reptile_type
        }