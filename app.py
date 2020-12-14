"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/api/cupcakes')
def list_all_cupcakes():
    """ Get data about all cupcakes.
        Respond with JSON like: {cupcakes:
        [{id, flavor, size, rating, image}, ...]}
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>')
def show_cupcake_info(cupcake_id):
    """ Get data about a single cupcake.
        Respond with JSON like: {cupcake:
        {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """ creates cupcake with flavor, size, rating and image data from the body
        of the request.
        Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
    """

    cupcake = Cupcake(
        flavor=request.json["flavor"],
        size=request.json["size"],
        rating=request.json["rating"],
        image=request.json["image"],
    )

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """ Update a cupcake with the id passed in the URL and flavor, size, rating
        and image data from the body of the request.
        Respond with JSON of the newly-updated cupcake, like this:
        {cupcake: {id, flavor, size, rating, image}}
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake["flavor"] = request.json["flavor"]
    cupcake["size"] = request.json["size"]
    cupcake["rating"] = request.json["rating"]
    cupcake["image"] = request.json["image"]

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """ Delete cupcake with the id passed in the URL. Respond with JSON like
        {message: "Deleted"}
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    Cupcake.query.filter_by(id=cupcake_id).delete()

    db.session.commit()

    return jsonify(message="Deleted")
