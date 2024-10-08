from flask import Flask, jsonify

import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models import db, Message
from models import Like

app = Flask(__name__)

app.config.from_object('config.Config')
db.init_app(app)
@app.route('/feed', methods=['GET'])
def get_feed():
    res = []
    messages = Message.query.order_by(Message.created_at.desc()).limit(10).all()
    for message in messages:
        num_of_likes = Like.query.filter_by(message_id=message.id).count()
        res.append({'user_id': message.user_id, 'content': message.content, 'created_at': message.created_at, 'message_id':message.id, 'num_of_likes': num_of_likes})

    return jsonify(res), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5001)