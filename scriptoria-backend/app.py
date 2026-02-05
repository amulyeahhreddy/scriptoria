from flask import Flask
from flask_cors import CORS


from routes.story import story_bp
from routes.characters import characters_bp
from routes.sound import sound_bp
from routes.export import export_bp

app = Flask(__name__)
CORS(app)

# app.register_blueprint(story_bp, url_prefix="/api")
# app.register_blueprint(characters_bp)
# app.register_blueprint(sound_bp)
# app.register_blueprint(export_bp)

app.register_blueprint(story_bp, url_prefix="/api/story")
app.register_blueprint(characters_bp, url_prefix="/api/characters")
app.register_blueprint(sound_bp, url_prefix="/api/sound")
app.register_blueprint(export_bp, url_prefix="/api/export")


@app.route("/")
def health():
    return {"status": "Scriptoria backend running"}


if __name__ == "__main__":
    app.run(debug=True)