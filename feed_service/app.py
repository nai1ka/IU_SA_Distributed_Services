from flask import Flask, jsonify
from models import db, Message
import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(__name__)

app.config.from_object('config.Config')
db.init_app(app)
@app.route('/feed', methods=['GET'])
def get_feed():
    messages = Message.query.order_by(Message.created_at.desc()).limit(10).all()
    feed = [{'user_id': message.user_id, 'content': message.content, 'created_at': message.created_at} for message in messages]

    return jsonify(feed), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5001)