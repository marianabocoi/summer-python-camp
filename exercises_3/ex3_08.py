"""
Using for loop and if/else statements print something like this
“<Participant name> is a participant”
“<Teacher/Organizer> is a teacher/organizer”
“<Your friend’s name> is my friend”

"""

participants = ["Elsa", "Alice", "Maja", "Agnes", "Lilly", "Olivia", "Julia", "Ebba", "Linnea", "Molly", "Ella",
                "Wilma", "Klara", "Stella"]
print(participants)

t_o = ["Sara", "Lisa", "Mariana", "Nadia"]
print(t_o)

all_people = t_o + participants
print(all_people)

all_people.append("Alva")
print(all_people)

for name in all_people:
    if name in participants:
        print(name, "is a participant")
    elif name in t_o:
        print(name, "is a teacher/organizer")
    else:
        print(name, "is my friend")
