# Number Guessing Game

Simple Number Guessing Game I made to explore the idea of moving from a cli interface to one for the web. 
Currently still messing around with it but if you want to run it I used.

Uses Python 3.10.11

To Run
```bash
# Console app
python -m entrypoints.console

# Web API Server
python -m entrypoints.web
```

They both output messages in the same way but it is pretty cool to see the api work as a standalone thingy. 
I am considering improving the api by adding a requirement to expose all the actions done in the api in reverse order i.e. stack that gets each new action pushed onto it.
