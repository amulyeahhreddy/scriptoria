from flask import Blueprint, jsonify
from services.sound_engine import generate_sound

sound_bp = Blueprint("sound", __name__, url_prefix="/sound")

@sound_bp.route("/generate/<project_id>")
def generate(project_id):
    sound = generate_sound(project_id)
    return jsonify({"sound_design": sound})
