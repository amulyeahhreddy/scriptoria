def validate_character_action(character, action):
    traits = character["psychology"]
    # simple logic now, expandable later
    if "fear" in traits and "contradict" in action:
        return False
    return True
