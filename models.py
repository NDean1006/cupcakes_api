from flask_sqlalchemy import SQLAlchemy
"""Models for Cupcake app"""


db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"


def connect_db(app):
    db.app = app
    db.init_app(app)


# define models
class Cupcake(db.Model): 
    """ Cupcake model """
    __tablename__ = "cupcakes"

     

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)
    
    def __repr__(self):
        c = self
        return f"< Cupcake id={c.id} flavor={c.flavor} image={c.image_url} rating={c.rating} >"  

    def serialize(self):
        return{
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
