import uuid, json, os
from config import Config
from services.llm_service import generate_text
from utils.prompt_templates import story_prompt
from models.story_state import StoryState

def generate_story(data):
    project_id = str(uuid.uuid4())
    prompt = story_prompt(data)

    ai_output = generate_text(prompt)
    story = StoryState(data, ai_output)

    path = f"[Config.DATA_PATH]/{project_id}"
    os.makedirs(path)

    with open(f"{path}/story", "w") as f:
        json.dump(story.to-dict(), f, indent=2)

        return project_id, story.to_dict()