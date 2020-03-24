import random

print("Welcome to BytLife! A Python clone based on the popular App, BitLife! All rights to the original owners, "
      "CandyCane LLC")
year = 0


#   To do next:
#   - Birthday/Star Sign
#   - Emotions [Done] that update each time you age
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
        self.age = year
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


#   Underline the word so it will always be equal to the length of it.
#   Use: u_word("=", "Hello") or the word param w/ a function that returns a string.
def underline_word(placeholder, word):
    word = placeholder * len(word)
    return word


#  Instantiate the class Person and start playing.
def client():
    #   Uh. . .
    p = Person("", "", "", "", "", "", "", "", "")
    sex = p.determine_sex()
    name = p.determine_name()
    surname = p.determine_surname()
    ethnicity = p.determine_ethnicity()
    age = p.determine_age()

    #   Emotions
    happiness = p.determine_happiness()
    health = p.determine_health()
    looks = p.determine_looks()
    smarts = p.determine_smarts()

    begin = input("Age? Press A\n")

    start = 0
    if start <= 0 and (begin == "a" or begin == "A"):
        display_age = "Age: {} Years".format(str(int(age) + 1))
        print(display_age)
        print(underline_word("=", display_age))
        print(f'I am a {ethnicity} {sex}. I was conceived at a [LOCATION].\n'
              f'\n'
              f'            My birthday is MONTH DAY. I am a STAR SIGN.\n'
              f'\n'
              f'            My name is {name} {surname}.\n'
              f'            My father is FATHER {surname}, a JOB (age (AGE))\n'
              f'            My mother is MOTHER {surname}, a JOB (age (AGE))')

    print(f"Happiness: {happiness}/100 | Health {health}/100 | Looks {looks}/100 | Smarts {smarts}/100")


client()
