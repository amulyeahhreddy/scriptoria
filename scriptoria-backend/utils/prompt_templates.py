# def story_prompt(data):
#     return f"""
# You are a professional screenwriter.

# Genre: {data['genre']}
# Tone: {data['tone']}
# Runtime: {data['runtime']}
# Budget: {data['budget']}
# Logline: {data['logline']}

# Generate:
# 1. 3-Act Structure
# 2. Major Plot Beats
# 3. Core Theme
# 4. Ending Direction

# Return in structured JSON format.
# """

def story_prompt(data):
    return f"""
You are a professional screenwriter.

Inputs:
- Genre: {data.get('genre', 'N/A')}
- Tone: {data.get('tone', 'N/A')}
- Runtime: {data.get('runtime', 'N/A')}
- Budget: {data.get('budget', 'N/A')}
- Logline: {data.get('logline', 'N/A')}

Generate the following strictly in JSON format:

{{
  "three_act_structure": {{
    "act_1": "",
    "act_2": "",
    "act_3": ""
  }},
  "major_plot_beats": [],
  "core_theme": "",
  "ending_direction": ""
}}

Do not include explanations or extra text.
"""


# def character_prompt(story, count=3):
#     return f"""
# Based on the following story:

# {story}

# Create {count} characters with:
# - Name
# - Role
# - Psychological traits
# - Character arc
# - Relationships

# Return JSON.
# """

def character_prompt(story, count=3):
    return f"""
You are a character development expert.

Story Context:
{story}

Create exactly {count} characters.

Return STRICT JSON in the following format:

{{
  "characters": [
    {{
      "id": "char_1",
      "name": "",
      "role": "",
      "psychological_traits": [],
      "character_arc": "",
      "relationships": []
    }}
  ]
}}

No extra commentary.
"""


# def sound_prompt(story):
#     return f"""
# Based on the story below, design sound cues for each act:

# {story}

# Return act-wise sound design notes.
# """

def sound_prompt(story):
    return f"""
You are a cinematic sound designer.

Story Context:
{story}

Return sound design cues in STRICT JSON:

{{
  "act_1": [],
  "act_2": [],
  "act_3": []
}}

Each entry should describe mood, instruments, and intensity.
"""
