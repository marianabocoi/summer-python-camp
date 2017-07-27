"""
Using for loop and list in 6. print all the names
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
    print(name)