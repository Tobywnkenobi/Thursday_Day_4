pokedex = {}

class Pokedex:
    
    def __init__(self, username):
        self.username = username
        self.collection = {}
        
    def __repr__(self):
        return f'<Pokedex: {self.username}>'
        
    def add_pokemon(self):
        pokemon = input("What Pokemon are you catching?: ")
        self.collection[pokemon] = Pokemon(pokemon)
        
    def build_team(self):
        while len(self.collection) < 6:
            self.add_pokemon()
        print('Party is full')

            
            
        
        
pokedex = Pokedex('dsmith')

pokedex

# pokedex.add_pokemon()

pokedex.build_team()

pokedex.collection