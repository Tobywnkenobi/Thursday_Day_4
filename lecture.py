Pokedex = {}

class Pokedex:

    def __init__(self, username):
        self.username = username
        self.collection = {}

    def __repr__(self):
        return f"<Poledex: {self.username}>"
    
    def add_pokemon(self):
        pokemon = input("What are you catching?: ")
        self.collection[pokemon] = Pokemon(pokemon)

    def build_team(self):
        while len(self.collection) < 6:
            pokemon = input("What Pokemon are you catching?")
            self.collection(pokemon) = Pokemon(pokemon)
            
