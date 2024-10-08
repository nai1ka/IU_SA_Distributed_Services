from flask import Flask, request, jsonify

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from models import db, Message, Like, User


app = Flask(__name__)
app.config.from_object("config.Config")
db.init_app(app)


@app.route("/messages", methods=["POST"])
def post_message():
    data = request.json
    username = data.get("username")
    content = data.get("content")

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    user_id = user.id

    if not content or len(content) > 400:
        return jsonify({"error": "Message content must be less than 400 characters"}), 400

    message = Message(user_id=user_id, content=content)
    db.session.add(message)
    db.session.commit()

    return jsonify({"message": "Message posted successfully"}), 201


@app.route("/messages/<int:id>/like", methods=["POST"])
def like_message(id):
    data = request.json
    username = data.get("username")

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    user_id = user.id

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    existing_like = Like.query.filter_by(user_id=user_id, message_id=id).first()

    if existing_like:
        db.session.delete(existing_like)
        db.session.commit()
        return jsonify({"message": "Like removed successfully"}), 200
    else:
        like = Like(user_id=user_id, message_id=id)
        db.session.add(like)
        db.session.commit()

        return jsonify({"message": "Message liked successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
