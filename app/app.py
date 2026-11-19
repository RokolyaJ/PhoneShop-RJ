import os
from flask import Flask, jsonify, request

from models import db, Phone
from database import init_db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:///phones.db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app)


@app.route("/")
def home():
    return jsonify({
        "project": "PhoneShop",
        "status": "running"
    })


@app.route("/phones")
def get_phones():
    phones = Phone.query.all()

    return jsonify([
        {
            "id": p.id,
            "brand": p.brand,
            "model": p.model,
            "price": p.price,
            "stock": p.stock
        }
        for p in phones
    ])


@app.route("/phones", methods=["POST"])
def add_phone():
    data = request.get_json()

    phone = Phone(
        brand=data["brand"],
        model=data["model"],
        price=data["price"],
        stock=data["stock"]
    )

    db.session.add(phone)
    db.session.commit()

    return jsonify({
        "id": phone.id,
        "brand": phone.brand,
        "model": phone.model,
        "price": phone.price,
        "stock": phone.stock
    }), 201


@app.route("/phones/<int:phone_id>", methods=["DELETE"])
def delete_phone(phone_id):
    phone = Phone.query.get(phone_id)

    if not phone:
        return jsonify({"message": "Phone not found"}), 404

    db.session.delete(phone)
    db.session.commit()

    return jsonify({"message": "Phone deleted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
