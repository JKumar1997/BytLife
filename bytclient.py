#  Instantiate the class Person and start playing.
from person import Person


print("Welcome to BytLife! A Python clone of the popular app BitLife!")


#   Underline age
def underline(underlined_by, word_underlined):
    underlined = underlined_by * len(word_underlined)
    return underlined


def client():
    #   Initialisation
    p = Person("", "", "", 0, "", 0, 0, 0, 0, [])
    #   General
    sex = p.determine_sex()
    name = p.determine_name()
    surname = p.determine_surname()
    ethnicity = p.determine_ethnicity()
    age = p.determine_age()
    alive = True
    play_count = 0

    #   Emotions
    happiness = p.determine_happiness()
    health = p.determine_health()
    looks = p.determine_looks()
    smarts = p.determine_smarts()
    birthday = p.determine_birthday()

    begin = input("Exist? Press A\n")
    while alive is True:
        #   Start = 0, if over 0, it's the next turn.
        display_age = "Age: {} Years".format(str(int(age)))
        print(display_age)
        print(underline("=", display_age))
        if play_count <= 0 and (begin == "a" or begin == "A"):
            print(f'I am a {ethnicity} {sex}. I was conceived at a [LOCATION].\n'
                  f'\n'
                  f'            My birthday is {birthday[0]} {birthday[1]}. I am a {birthday[2]}.\n'
                  f'\n'
                  f'            My name is {name} {surname}.\n'
                  f'            My father is FATHER {surname}, a JOB (age (AGE))\n'
                  f'            My mother is MOTHER {surname}, a JOB (age (AGE))\n')
            print(p.determine_emotion())
            age += 1
            play_count += 1
            begin = input("Age? Press A\n")
        elif play_count >= 1 and (begin == "a" or begin == "A"):
            play_count += 1
            age += 1
            print(p.determine_emotion())
            begin = input("Age? Press A\n")
        else:
            print("Invalid input")
            alive = False

client()
