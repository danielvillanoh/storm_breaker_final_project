# storm_breaker_final_project
INST326-102 Storm Breaker

## Files

### class_baseball.py
The purpose of the file is where the main contribution of the final project 
comes from. The classes and function are in this file. This is where you run
the program from. 

### exercise.py 
This file was only used for our Collaborating Programming exercise. 

## Running the Program 

To run the program, simply type: 
`python class_baseball.py`
Replace python, with
python3 if you're running on Mac. 

## Using the Program 
When running the program, the program will ask for a name. After typing the 
name, the program will again ask for a name, only for the second user.
The program will ask if the user would like a bot to play in place of 
the second user. Typing 0 will prompt the user to play against the bot. 
Typing any other number will let the user play against the second user. 
User will type a number from 1 to 3 until they met with strike three. The 
second user will do the same until they get a third strike. This step is
repeated four times. The program will calculate the total score for both users 
and print them out. The winner will be declared. 

## Attribution 

### class Player()
This class was created by Daniel Villano-Herrera. The techniques used for the 
class was f-strings and magic methods other than init. 

### class Opponent(Player)
This class was created by Daniel Villano-Herrera. The technique used for the 
class was inheritance. 

### def base_ball(innings = 4)
This function was created by Daniel Villano-Herrera. Optional argument was used 
and Matthew McManus created a conditional expression to declare a winner. 