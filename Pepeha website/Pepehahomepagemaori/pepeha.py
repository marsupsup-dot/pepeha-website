dictionary = {
    "Maunga": "Mountain",
    "Roto": "Lake",
    "Awa": "River",
    "Waka": "Canoe",
    "Rohe": "District",
    "Iwi": "Tribe",
    "Hapū": "Subtribe",
    "Marae": "Marae",
    "Mātua": "Parents",
}

def translate_to_english(word):
    # Normalize input (capitalize first letter)
    normalized_word = word.capitalize()
    return dictionary.get(normalized_word, word)

def create_pepeha():
    mountain = input("What is your mountain (Maori)? ")
    lake = input("What is your lake (Maori)? ")
    river = input("What is your river (Maori)? ")
    canoe = input("What is your canoe (Maori)? ")
    district = input("What is your district (Maori)? ")
    tribe = input("What is your tribe (Maori)? ")
    subtribe = input("What is your subtribe (Maori)? ")
    marae = input("What is your marae (Maori)? ")
    parents = input("What are your parents' names (Maori)? ")
    name = input("What is your name? ")

    print("\n--- Your Pepeha ---\n")
    print(f"Ko {mountain} tōku maunga ({translate_to_english(mountain)})")
    print(f"Ko {lake} tōku roto ({translate_to_english(lake)})")
    print(f"Ko {river} tōku awa ({translate_to_english(river)})")
    print(f"Ko {canoe} tōku waka ({translate_to_english(canoe)})")
    print(f"Ko {district} tōku rohe ({translate_to_english(district)})")
    print(f"Ko {tribe} tōku iwi ({translate_to_english(tribe)})")
    print(f"Ko {subtribe} tōku hapū ({translate_to_english(subtribe)})")
    print(f"Ko {marae} tōku marae ({translate_to_english(marae)})")
    print(f"Ko {parents} ōku mātua (Parents)")
    print(f"Ko {name} tōku ingoa (Name)")

if __name__ == "__main__":
    create_pepeha()
