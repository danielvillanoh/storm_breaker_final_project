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
 

What we're planning to add: 
optional argument,
sequence unpacking, 
visualizing data????, 
conditional expressions, 
custom list sorting
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
        to choose numbers from 2 to 14. 
        """
       
        
        strike = 0 
        
        game_score = 0 
        while strike != 3:
            number = int(input("Choose a number from 1-3 to swing: "))
            random_number  = rand.randint(1,3)
            if number == random_number:
                game_score += 1
            else: 
                strike += 1
        
        self.score.append(game_score)
        print(f"The score of {self.name} is {self.score}.")       
            
        
        
        
        
        
class Opponent(Player):
    """ This class represents the opponent or the second player. 
    The opponent class will inherit the properites of the Player class.  
     
    """
    
    def botPlayer(self):
        """
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
            if number  == random_guess: 
                game_score += 1
            else: 
                strike += 1
        
        #Once it's there's three strike simply append the game_score to the 
        #score list
        self.score.append(game_score)

class Baseball:
    """ This class represents the game of Baseball. 
    
    """
