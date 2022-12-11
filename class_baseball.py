"""Building a skeleton to better understand what we will implement for this 
final project. 

For this instance, we will create the baseball class, player and opponent class.

Typically, a full game of baseball consists of 9 rounds, but for our final 
project, we will truncate it to 4 rounds. The game will also be random based, 
meaning the scenarios of the baseball game will be random and we will import
random. 
"""


"""
What we have so far, 
f-strings, 
optional argument
magic methods


What we're planning to add: 


visualizing data????, 
conditional expressions, 
custom list sorting
ArgumentParser??

"""
import random as rand 


class Player():
    """ This class represents the player or the first player. 
    
    Attributes: 
        name(str): the name of the player 
        score(List): the list of the score for each game.

    """
    
    def __init__(self,name):
        """ 
        Argument: 
            name(str): the name of the player
        
        We will also the add 'score' attribute in the init magic method. 
        """
        self.name  = name 
        self.score = []
    def swing(self):
        """ The player swings the ball. We will prompt the user 
        to choose numbers from 1 to 3. 
        """
       
        
        strike = 0 
        
        game_score = 0 
        while strike != 3:
            number = int(input("Choose a number from 1-3 to swing: "))
            random_number  = rand.randint(1,3)
            if number == random_number:
                game_score += 1
                print(f"Home Run!")
            else: 
                strike += 1
                print("Stike!")
        
        print("Strike three, you're out!")
        
        self.score.append(game_score)   
    
    def __str__(self):
        return f"{self.name} has scored {sum(self.score)}"
     
            
        
        
        
        
        
class Opponent(Player):
    """ This class represents the opponent or the second player. 
    The opponent class will inherit the properites of the Player class.  
     
    """    
       
        
    def botSwing(self):
        """
        """
        
        strike = 0
        
        game_score = 0 
        
        #While the strike is not equals to three 
        while strike != 3: 
            #The bot will have a random number variable
            #And the guessing number is a seperate variable. 
            number = rand.randint(1,3)
            random_guess = rand.randint(1,3)
            
            #If the bot correctly guesses the guessing number
            #The score will be added otherwise it's a strike.
            if number == random_guess: 
                game_score += 1
                print("Bot has scored!")
            else: 
                print("Bot has a strike!")
                strike += 1
        
            
        #Once it's there's three strike simply append the game_score to the 
        #score list
        print("Bot is out!")
        self.score.append(game_score)

def baseBall(games = 4):
    """ This function represents the game of Baseball. 
    
    """
    game_count = 0 
        
    play_one = input("Please enter the name of your player: ")
    player_one = Player(play_one)
    
    opp_play = input("Enter the name for the opposing player: ")
    opp_player = Opponent(opp_play)
         
    bot_or_manual = int(input("If you would like a bot, press 0, press any number if otherwise: "))
    while game_count != games:
        if bot_or_manual == 0: 
            player_one.swing()
            opp_player.botSwing()
        else:
            player_one.swing()
            opp_player.swing()

        game_count += 1
    print (player_one.__str__() + " and " + opp_player.__str__())
    
if __name__ == "__main__":
    baseBall()      
        
    
        
        
