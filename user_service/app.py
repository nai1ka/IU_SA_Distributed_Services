from flask import Flask, request, jsonify
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from models import db, User

app = Flask(__name__)
app.config.from_object("config.Config")
db.init_app(app)


# TODO change
@app.route("/users/register", methods=["POST"])
def register_user():
    data = request.json
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
