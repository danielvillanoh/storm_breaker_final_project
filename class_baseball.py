"""Building a skeleton to better understand what we will implement for this 
final project. 

For this instance, we will create the baseball function, 
player and opponent class.

Typically, a full game of baseball consists of 9 innings, but for our final 
project, we will truncate it to 4 innings. The game will also be random based, 
meaning the scenarios of the baseball game will be random and we will import
random. 
"""


"""
What we have so far, 
f-strings, 
optional argument
conditional expressions,
magic methods


"""
import random as rand 

#Player Class by: Daniel Villano-Herrera
class Player():
    """ This class represents the player or the first player. 
    
    Attributes: 
        name(str): the name of the player 
        score(List): the list of the score for each game.

    """
    
    def __init__(self,name):
        """ Initalizing the Player object with name and score attributes. 
        Args: 
            name(str): the name of the player
            
        Side Effect:
            The name and score attributes are declared. 
        """
        self.name  = name 
        self.score = []
    def swing(self):
        """ The player swings the ball. Prompts the user 
        to choose numbers from 1 to 3. 
        
        Side Effects: 
            The score attribute changes as the player has 3 strikes. 
        """   
        strike = 0 
        
        game_score = 0 
        while strike != 3:
            number = int(input(f"""{self.name} you're up! Choose a number 
                               from 1-3 to swing: """))
            random_number  = rand.randint(1,3)
            if number == random_number:
                game_score += 1
                print(f"Home Run!")
            else: 
                strike += 1
                print("Strike!")
        
        print("Strike three, you're out!")
        
        self.score.append(game_score)   
    
    def __str__(self):
        """ The formal representation of the Player object. 
        Returns:
            str: The string representation of the Player object. 
        """
        return f"{self.name} has scored {sum(self.score)}"
     
            
# Opponent Class by: Daniel Villano-Herrera                
class Opponent(Player):
    """ This class represents the opponent or the second player or the bot. 
    The opponent class will inherit the properites and methods
    of the Player class.  
     
    """    
       
        
    def botSwing(self):
        """ The bot swings the ball. Bot will guess the number from 1-3. 
        
        Side Effects:
            The score attribute changes as the bot gets three strikes. 
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
        
            
        #Once it's three strikes simply append the game_score to the 
        #score list
        print("Bot is out!")
        self.score.append(game_score)

# base_ball function by: Daniel Villano-Herrera
def base_ball(innings = 4):
    """ This function represents the game of Baseball. Function will the user 
    for a name and another name if another user chooses to play. A bot will play
    if the other user chooses not to play and four innings of baseball game will
    start. 
    
    Args: 
        innings(int): The amount of innings played in baseball. 
            Default Value = 4 
    
    Side Effects: 
        Prints player one and player two (or bot) score.
        Prints whoever wins or it's a tie. 
        
    """
    innings_count = 0 
        
    play_one = input("Please enter the name of your player: ")
    player_one = Player(play_one)
    
    opp_play = input("Enter the name for the opposing player: ")
    opp_player = Opponent(opp_play)
         
    bot_or_manual = int(input(f"""If you would like a bot, press 0, press any
                              number if otherwise: """))
    
    while innings_count != innings:
        if bot_or_manual == 0:
            opp_player = Opponent("Bot") 
            player_one.swing()
            opp_player.botSwing()
        else:
            player_one.swing()
            opp_player.swing()

        innings_count += 1
    print (player_one.__str__() + " and " + opp_player.__str__())
    
    #Conditional Expression technique by: Matthew McManus
    print (f"{player_one.name} wins" if player_one.score > opp_player.score
    else f"{opp_player.name} wins" if opp_player.score > player_one.score
    else "it's a tie" )
    
        

        
        
if __name__ == "__main__":
    base_ball()      
        


        
