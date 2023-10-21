from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250))
    coffee_price = db.Column(db.String(250))

@app.route('/')
def get_all_cafes():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes)

@app.route('/add_cafe', methods=['POST', 'GET'])
def add_cafe():
    if request.method == 'POST':
        data = request.form
        new_cafe = Cafe(
            name=data['name'],
            map_url=data['map_url'],
            img_url=data['img_url'],
            location=data['location'],
            has_sockets=bool(data.get('has_sockets')),
            has_toilet=bool(data.get('has_toilet')),
            has_wifi=bool(data.get('has_wifi')),
            can_take_calls=bool(data.get('can_take_calls')),
            seats=data['seats'],
            coffee_price=data['coffee_price']
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("get_all_cafes"))
    return render_template("add_cafe.html")

@app.route('/delete_cafe/<int:cafe_id>')
def delete_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
    return redirect(url_for("get_all_cafes"))

if __name__ == "__main__":
    app.run(debug=True, port=5003)
