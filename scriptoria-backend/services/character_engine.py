# import json, os
# from services.llm_service import generate_text
# from utils.prompt_templates import character_prompt

# def generate_characters(project_id):
#     path = f"data/sessions/{project_id}"

#     with open(f"{path}/story.json") as f:
#         story = json.load(f)

#     prompt = character_prompt(story["structure"])
#     ai_output = generate_text(prompt)

#     with open(f"{path}/characters.json", "w") as f:
#         json.dump({"characters": ai_output}, f, indent=2)

#     return ai_output
# import json
# from services.llm_service import generate_text
# from utils.prompt_templates import character_prompt

# def generate_characters(project_id):
#     path = f"data/sessions/{project_id}"

#     # Read story
#     with open(f"{path}/story.json", "r") as f:
#         story = json.load(f)

#     # Build prompt
#     prompt = character_prompt(story["structure"])

#     # Generate characters
#     ai_output = generate_text(prompt)

#     # Save characters
#     with open(f"{path}/characters.json", "w") as f:
#         json.dump({"characters": ai_output}, f, indent=2)

#     return ai_output

import json, os
from services.llm_service import generate_text
from utils.prompt_templates import character_prompt

def generate_characters(project_id):
    path = f"data/sessions/{project_id}"

    story_path = f"{path}/story.json"
    characters_path = f"{path}/characters.json"

    if not os.path.exists(story_path):
        raise FileNotFoundError("Story file not found") 

    with open(story_path, "r") as f:
        story = json.load(f)

    if "structure" not in story:
        raise KeyError("Story structure missing")

    prompt = character_prompt(story["structure"])
    ai_output = generate_text(prompt)

    # If LLM returns JSON text → parse it
    if isinstance(ai_output, str):
        try:
            ai_output = json.loads(ai_output)
        except json.JSONDecodeError:
            ai_output = {"raw_output": ai_output}

    with open(characters_path, "w") as f:
        json.dump({"characters": ai_output}, f, indent=2)

    return ai_output
