from flask import Blueprint, jsonify
from services.character_engine import generate_characters

characters_bp = Blueprint("characters", __name__, url_prefix="/characters")

@characters_bp.route("/generate/<project_id>")
def generate(project_id):
    characters = generate_characters(project_id)
    return jsonify({"characters": characters})
