"""Building a skeleton to better understand what we will implement for this 
final project. 

For this instance, we will create the baseball class, player and opponent class.
"""


class Player():
    """ This class represents the player or the first player. 
    
    Attributes: 
        name(str): the name of the player 
        score(List): the list of the score for each game.

    """
    
    def __init__(self,name):
        """ 
        Arguments: 
            name(str): the name of the player
        
        We will also the add 'score' attribute in the init magic method. 
        """
    def swing(self, pitch_and_catch = False):
        """ The player swings the ball.
        Arguments:
            pitch_and_catch(boolean): This will determine on whether the player
            is pitching and catching the ball, false by default. 
        """

    def pitch(self,pitch_and_catch = True):
        """ The player pitches the ball. Only possible if the player isn't 
        swinging. 
        
        """
        
    def catch(self, pitch_and_catch = True):
        """ 
        """
        
    def player_score(self):
        """
        """
        
class Opponent(Player):
    """ This class represents the opponent or the second player. 
    The opponent class will inherit the properites of the Player class.  
    """

class Baseball:
    """ This class represent the game of Baseball. 
    
    """
    


    
    