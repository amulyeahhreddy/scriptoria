class CharacterMemory:
    def __init__(self, name, role, psychology, arc, relationships):
        self.name = name
        self.role = role
        self.psychology = psychology
        self.arc = arc
        self.relationships = relationships

    def to_dict(self):
        return self.__dict__
