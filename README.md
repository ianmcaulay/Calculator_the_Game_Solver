# Calculator_the_Game_Solver
This is a solver for the app Calculator: The Game (links at bottom). It should be able to solve levels up to and including level 131 (although it hasn't been extensively tested). This is about as high a level as I've reached in the game so there are probably more operations that I'm missing. Feel free to submit an issue describing other operations if you know of more. 

## Example
For level 25 of the game, you have 4 moves to get from 40 to 2020. You have the buttons 0, +4, and /2. To run the solver on this, call the solve function as follows:  
solve(4, 40, 2020, ["0", "+4", "/2"])  
The program should print out:  
Use button 0  
Use button +4  
Use button 0  
Use button /2

## Links
App store: https://itunes.apple.com/us/app/calculator-the-game/id1243055750?mt=8  
Google Play: https://play.google.com/store/apps/details?id=com.sm.calculateme&hl=en

