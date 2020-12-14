from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_CUPCAKE_IMAGE = 'https://tinyurl.com/demo-cupcake'


def connect_db(app):
    """ connect this database to provided flask app """

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """ Class for creating instances of a cupcake """

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_CUPCAKE_IMAGE)

    def serialize(self):
        """ return serialized instance data """

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }
