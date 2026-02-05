from flask import Blueprint, jsonify
import json, os

export_bp = Blueprint("export", __name__, url_prefix="/export")

@export_bp.route("/project/<project_id>")
def export(project_id):
    path = f"data/sessions/{project_id}"
    data = {}

    for file in os.listdir(path):
        with open(f"{path}/{file}") as f:
            data[file] = json.load(f)

    return jsonify(data)
