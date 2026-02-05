import json
from services.llm_service import generate_text
from utils.prompt_templates import sound_prompt

def generate_sound(project_id):
    path = f"data/sessions/{project_id}"

    with open(f"{path}/story.json") as f:
        story = json.load(f)

    prompt = sound_prompt(story["structure"])
    ai_output = generate_text(prompt)

    with open(f"{path}/sound.json", "w") as f:
        json.dump({"sound_design": ai_output}, f, indent=2)

    return ai_output
