from flask import Blueprint, request, jsonify, abort, current_app, render_template
from .models import Reptiles, db  # Import the Reptiles class and db instance directly
import os
import json

bp = Blueprint('reptile', __name__, url_prefix='/reptiles')

def load_reptiles():
    try:
        return Reptiles.query.all()
    except Exception as e:
        print(f"Error loading reptiles: {e}")  # Debug print or log
        return []

@bp.route('/')
def index():
    reptiles = load_reptiles()
    return jsonify([reptile.to_dict() for reptile in reptiles])

@bp.route('/<int:reptile_id>')
def show(reptile_id):
    reptile = Reptiles.query.get_or_404(reptile_id)
    return jsonify(reptile.to_dict())

@bp.route('/', methods=['POST'])
def create_reptile():
    data = request.get_json()
    if not data or 'name' not in data or 'reptile_type' not in data:
        abort(400, description="Missing name or reptile_type")

    reptile = Reptiles(name=data['name'], reptile_type=data['reptile_type'])
    db.session.add(reptile)
    db.session.commit()
    return jsonify(reptile.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_reptile(id):
    reptile = Reptiles.query.get_or_404(id)
    data = request.get_json()
    if 'name' in data:
        reptile.name = data['name']
    if 'reptile_type' in data:
        reptile.reptile_type = data['reptile_type']
    db.session.commit()
    return jsonify(reptile.to_dict())

@bp.route('/<int:id>', methods=['DELETE'])
def delete_reptile(id):
    reptile = Reptiles.query.get_or_404(id)
    db.session.delete(reptile)
    db.session.commit()
    return jsonify({'message': 'Reptile deleted successfully'}), 204
