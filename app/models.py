from app import db

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    desp = db.Column(db.String(length=1500), nullable=False)

    def __repr__(self):
        #override default storage name in database
        return f'Product {self.name}'