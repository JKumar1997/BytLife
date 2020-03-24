import random

#   To do next:
#   - Birthday/Star Sign
#   - Emotions [Done] that update each time you age [Done]
#   - Parents
#   - Location where you were concieved.
#   - Grab names from an API vs. making them manually.
#   - Reduce repetitive code


class Person:
    def __init__(self, sex, first_name, last_name, age, ethnicity, happiness, health, smarts, looks):
        self.sex = sex
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ethnicity = ethnicity
        self.happiness = happiness
        self.health = health
        self.smarts = smarts
        self.looks = looks

    def determine_sex(self):
        if random.randint(0, 1) == 0:
            self.sex = "male"
        else:
            self.sex = "female"
        return self.sex

    def determine_name(self):
        if self.sex == "male":
            first = ("Robert", "Sam", "Joe")
            self.first_name = random.choice(first)
        if self.sex == "female":
            first = ("Joanne", "Laura", "Aubry")
            self.first_name = random.choice(first)
        return self.first_name

    def determine_surname(self):
        last = ("Jones", "Peterson", "Smith")
        self.last_name = random.choice(last)
        return self.last_name

    def determine_age(self):
        self.age = 0
        return self.age

    def determine_ethnicity(self):
        countries = {
            "Australia": "Australian",
            "Germany": "German",
            "Italy": "Italian",
            "France": "French",
            "China": "Chinese",
            "Sweden": "Swedish"
        }
        self.ethnicity = random.choice(list(countries.values()))
        return self.ethnicity

    def determine_happiness(self):
        self.happiness = random.randint(0, 100)
        return self.happiness

    def determine_health(self):
        self.health = random.randint(0, 100)
        return self.health

    def determine_smarts(self):
        self.smarts = random.randint(0, 100)
        return self.smarts

    def determine_looks(self):
        self.looks = random.randint(0, 100)
        return self.looks

    def determine_emotion(self):
        self.happiness = self.happiness + random.randint(-1, 1)
        self.health += random.randint(-1, 2)
        self.smarts += random.randint(-1, 2)
        self.looks += random.randint(-1, 2)
        return f"Happiness: {self.happiness} | Health: {self.health} | Smarts: {self.smarts}, Looks: {self.looks}"
