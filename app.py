from  flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "gettimjiggywithit9999999"
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG'] = True

connect_db(app)



@app.route("/")
def root():
    """Render homepage."""

    return render_template("index.html")

# API GET Routes ############################################################# 
@app.route("/api/cupcakes")
def list_cupcakes():
    """ API get all cupcakes """
    all_cupacakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupacakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    """ get single cupcake """
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

# API POST Route ##############################################################

@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    """ create new cupcake """
    new_cupcake =  Cupcake(
        flavor=request.json["flavor"],
        size=request.json["size"],
        rating=request.json["rating"],
        image=request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    res_json = jsonify(cupcake=new_cupcake.serialize())
    return (res_json, 201) 

# API PATCH Route ############################################################# 

@app.route("/api/cupcakes/<int:id>",methods=["PATCH"])
def Update_cupcake(id):
    """ update cupcake by id """
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

# API DELETE Route ############################################################# 

@app.route("/api/cupcakes/<int:id>",methods=["DELETE"])
def Delete_cupcake(id):
    """ Delete cupcake by id """
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Eaten")


