# Phase One

Make a number guessing game

It needs to support letting people know when the number is less than greater than or equal.
It should forcibly wait for the input to be valid before incrementing the number
The program should pick only a single number so it doesn't hop around
It needs to be configurable for min and maxes 
It should be able to configure your max amount of guesses
All output should let you know the state of the game i.e. it should be tell you what your lower and upper bounds are. 
Debugging output for the number before the game begins.

# Phase Two

Extend the number guessing game to calculate the difference to print a different message the closer you get to the number. 
Anything beyond 10% off it should say you are way off.

# Phase Three

Expose the number guessing game as an api.
It should expose a route to start a session and other to submit the different guesses

It should give back the same messages as the console app as responses but in a json payload with a message key containing the str
