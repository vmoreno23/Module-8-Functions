class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses
        
    def get_model(self):
        return self.nickname
    
    def get_year(self):
        return self.weapons
    
    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses

    
player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
                    
def check_character(self):
        print("Checking Character")

        player_task = input("Which task do you want to perform? (Type exactly: Climb a mountain, Cook a meal, Write a book): ")

        if player_task == "Climb a mountain":
            if 'slow' in player1.weaknesses:
                print("You are slow. You cannot climb a mountain.")
            elif ('rope'in player1.weapons) and ('coat' in player1.weapons) and ('first aid kit' in player1.weapons):
                print("You can climb a mountain")
            else:
                print("Player will not climb mountain")
                    

        elif player_task == "Cook a meal":
            if 'small' in player1.weaknesses:
                print("You are small. You cannot cook a meal")
            elif ('pan' in player1.weapons) and ('groceries' in player1.weapons):
                print("You can cook a meal")
            else:
                print("Player will not cook")
                    

        elif player_task == "Write a book":
            if 'confusion' in player1.weaknesses:
                print("You are confused. You cannot write a book")
            elif ('pen', 'paper', 'idea' in player1.weapons):
                print("You can write a book")
            else:
                print("Player will not write a book")

check_character(player1)

# Victor Moreno
# 3/7/24

# Function that checks whether your game character has picked up all the items needed to perform certain tasks and checks against any status debuffs.
