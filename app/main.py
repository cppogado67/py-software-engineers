class SoftwareEngineer:
    def __init__(self, name):
        self.name = name
        self.skills = []  
    
    def learn_skill(self, skill):
        self.skills.append(skill)

class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)  # calls parent's __init__
        self.skills.extend(["JavaScript", "HTML", "CSS"])
    
    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


