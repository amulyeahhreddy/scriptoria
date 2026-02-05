from flask import Blueprint, request, jsonify
from services.story_engine import generate_story

story_bp = Blueprint("story", __name__, url_prefix="/story")

# @story_bp.route("/generate", methods=["POST"])
# def generate():
#     project_id, story = generate_story(request.json)
#     return jsonify({"project_id": project_id, "story": story})
@story_bp.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    try:
        project_id, story = generate_story(data)
        return jsonify({
            "project_id": project_id,
            "story": story
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
