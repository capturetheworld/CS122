# ----------------------------------------------------------------------
# Name:        Restaurants
# Purpose:     Demonstrate web development with Flask and Alchemy
#
# Author:      Ian SooHoo
# ----------------------------------------------------------------------
""" Restaurants

A restaurant database that allows you to find the best place for the
price in the location where you are searching.
"""


from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///places.db'
db = SQLAlchemy(app)

class Places(db.Model):

    """
    Class to represent and access the places table.
    Attributes:
    id (integer)
    name (string)
    type (string)
    city (string)
    price (integer)
    """

    __tablename__ = "places"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    location = db.Column(db.String)
    price = db.Column(db.Integer)


@app.route('/')
@app.route('/home')
def welcome():
    places = ""
    if Places.query.all():
        places = Places.query.order_by(Places.id.desc()).limit(5)
    return render_template('home.html', places=places)

@app.route('/add',methods=["POST","GET"])
def add():
    if request.method == "POST":
        name_input = request.form.get("name")
        category_input = request.form.get("category")
        location_input = request.form.get("location")
        price_input = request.form.get("price")
        new_place = Places(name=name_input, category=category_input,
                           location=location_input, price=price_input)
        db.session.add(new_place)
        db.session.commit()

    # results = Places.query.all()
    return render_template('add.html')

@app.route('/view',methods=["POST","GET"])
def more():
    places = Places.query.all()
    category = ''
    location = ''
    price = ''

    if request.method == "POST":
        category = request.form.get("category")
        location = request.form.get("location")
        price = request.form.get("price")
        query = Places.query #start with all
        if category:
            query = Places.query.filter(Places.category == category)  # filter
        if location:
            query = query.filter(Places.location == location)
        if price:
            query = query.filter(Places.price <= price)
        places = query.all()
    return render_template('view.html', places=places, category=category,
                           location=location, price=price)



def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
