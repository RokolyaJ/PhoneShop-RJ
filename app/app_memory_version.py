from flask import Flask, jsonify, request

app = Flask(__name__)

phones = [
    {
        "id": 1,
        "brand": "Samsung",
        "model": "Galaxy S24",
        "price": 350000,
        "stock": 5
    },
    {
        "id": 2,
        "brand": "Apple",
        "model": "iPhone 17",
        "price": 550000,
        "stock": 3
    }
]


@app.route("/")
def home():
    return jsonify({
        "project": "PhoneShop",
        "status": "running"
    })


@app.route("/phones")
def get_phones():
    return jsonify(phones)


@app.route("/phones", methods=["POST"])
def add_phone():
    data = request.get_json()

    new_phone = {
        "id": len(phones) + 1,
        "brand": data["brand"],
        "model": data["model"],
        "price": data["price"],
        "stock": data["stock"]
    }

    phones.append(new_phone)

    return jsonify(new_phone), 201


@app.route("/phones/<int:phone_id>", methods=["DELETE"])
def delete_phone(phone_id):
    global phones

    phones = [phone for phone in phones if phone["id"] != phone_id]

    return jsonify({
        "message": "Phone deleted"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
