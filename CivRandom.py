import random

gameType = input("What win type: 1-Dom 2-Culture 3-Science 4-Diplomatic 5-Religion?")

if gameType == "1":
        print(1)
elif gameType == "2":
        print(2)
elif gameType == "3":
        print(3)
elif gameType == "4":
        print(4)
elif gameType == "5":
        print(5)
else:
        print("You didn't type a valid number")

civs = ["Teddy Roosevelt", "Saladin", "John Curtain", "Montezuma", "Pedro II",
        "Wilfrid Laurier", "Qin Shi Huang", "Poundmaker", "Wilhelmina", "Cleopatra",
        "Victoria", "Eleanor of Aquitaine (England)", "Catherine de Medici",
        "Eleanor of Aquitaine (French)", "Tamar", "Frederick Barbossa", "Pericles",
        "Gorgo", "Matthias Corvinus", "Pachacuti", "Ghandi", "Chandragupta",
        "Gitarja", "Hojo Tokimune", "Jayavarman VII", "Mvemba a Nzinga", "Seodeok",
        "Alexander", "Mansa Musa", "Kupe", "Lautaro", "Genghis Khan", "Harald Hardrada",
        "Amanitore", "Suleiman", "Cyrus", "Dido", "Jadwiga", "Trajan", "Peter",
        "Robert the Bruce", "Tomyris", "Philip II", "Gilgamesh", "Kristina", "Shaka"]
i = random.randint(1, 42)

print(civs[i])
