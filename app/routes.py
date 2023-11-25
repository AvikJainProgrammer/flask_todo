from app import app, db
from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import User, Todo
from datetime import timedelta

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username', '')
    password = request.json.get('password', '')

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already taken"}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        expires = timedelta(hours=1)
        access_token = create_access_token(identity=username, expires_delta=expires)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid username or password"}), 401

@app.route('/todo', methods=['POST'])
@jwt_required()
def add_todo():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    title = request.json.get('title', '')
    description = request.json.get('description', '')
    if not title:
        return jsonify({"msg": "Missing title"}), 400
    todo = Todo(title=title, description=description, user_id=user.id)
    db.session.add(todo)
    db.session.commit()
    return jsonify({"msg": "Todo created successfully", "todo": todo.id}), 201
