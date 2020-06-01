import random

gameType = input("What win type: 1-Dom 2-Culture 3-Science 4-Diplomatic 5-Religion?")

civs = []

if gameType == "1":
        civs = ["Robert The Bruce", "Lautaro", "Shaka", "Genghis Khan", "Amanitore", "Alexander", "Gilgamesh", "Frederick Barbarossa", "Montezuma", "Cyrus", "Pedro II (Naval)", "Phillip II (Religious)", "Tomyris", "Suleiman", "Dido (Naval)", "Kupe", "Matthias Corvinus", "Eleanor of Aquitaine (France)", "Eleanor of Aquitaine (England)", "Simon Bolivar"]
        index = random.randint(1, len(civs))
        print(civs[index])
elif gameType == "2":
        civs = ["Wilhelmina", "PoundMaker", "Lataro", "Seondeok", "Cleopatra", "Peter", "Gorgo", "Theodore Roosevelt", "Trajan", "Catherine de Medici", "Mvemba a Nzinga", "Cyrus", "Hojo Tokimune", "Pedro II", "Victoria", "Pericles", "Wilfrid Laurier", "Kupe", "Kristina", "Eleanor of Aquitaine (France)", "Eleanor of Aquitaine (England)"]
        index = random.randint(1, len(civs))
        print(civs[index])
elif gameType == "3":
        civs = ["Wilhelmina", "Robert The Bruce", "PoundMaker", "Seondeok", "Shaka", "Genghis Khan", "Amanitore", "Gilgamesh", "Saladin", "Peter", "Trajan", "Qin Shi Huang", "Frederick Barbarossa", "Montezuma", "John Curtain", "Hojo Tokimune", "Pedro II", "Suleiman", "Pachacuti", "Dido", "Matthias Corvinus", "Mansa Mansa", "Simon Bolivar", "Lady Six Sky"]
        index = random.randint(1, len(civs))
        print(civs[index])
elif gameType == "4":
        civs = ["Tamar", "Peter", "Jadwiga", "Harald Hardrada", "Qin Shi Huang", "Gitarja", "Catherine de Medici", "Mvemba a Nzinga", "Jayavarman", "Victoria", "Pericles", "Ghandi", "Pachacuti", "Wilfrid Laurier", "Kristina", "Lady Six Sky"]
        index = random.randint(1, len(civs))
        print(civs[index])
elif gameType == "5":
        civs = ["Lautaro", "Tamar", "Chandragupta", "Amanitore", "Cleopatra", "Saladin", "Peter", "Jadwiga", "Tragan", "Gitarja", "John Curtain", "Phillip II", "Tomyris", "Ghandi", "Kupe", "Mansa Mansa"]
        index = random.randint(1, len(civs))
        print(civs[index])
else:
        print("You didn't type a valid number")


