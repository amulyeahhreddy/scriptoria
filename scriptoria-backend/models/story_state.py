class StoryState:
    def __init__(self, data, ai_output):
        self.genre = data["genre"]
        self.tone = data["tone"]
        self.runtime = data["runtime"]
        self.budget = data["budget"]
        self.logline = data["logline"]
        self.structure = ai_output

    def to_dict(self):
        return self.__dict__
