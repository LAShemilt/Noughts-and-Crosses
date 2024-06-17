# Noughts and Crosses

Welcome to noughts and crosses, this game has been forked from the wonderful project by `danlane`, where you can train a model to play noughts-and-crosses against you see https://machinelearningforkids.co.uk/#!/worksheets.

Here I wanted to make this more "science fair" ready for our open day, but having a build that was installable, and a game that continued to play without needing to be restarted each time. 

## Installation
To install the program first create a conda environment with 
```
conda env create -f environment.yml
```
Activate the environment with:
```
conda activate noughtsandcrosses
```
Make a .env file in the location you are running the code. Use the `.env_example` file as a template. To run the game first go  https://machinelearningforkids.co.uk/ make an account and set up a Noughts and Crosses projects. Go to Make > Python then copy the key in to the .env file. 
Then install the game inside your conda environment with
```
pip install setup.py
```
## Playing the game

To start the game open a terminal and type:
```
noughtsandcrosses
```
The gameboard will appear. 
To continue playing press the green button "Play Again". To quit the game press the small x icon at the top right of the screen, if this doesn't quit, move to the terminal and press `Ctrl + C`. You may have to wait a few moments for the game to quit. 

## Importing your model

When you first start playing the game the computer will be playing randomly as we need to send games back to Machine Leanring For Kids to train our model. Once you have enough games you can navigate to the Learn & Test part of your project and create a model. Once this has been done go to the Make section , click python and then you will see your model URL listed. Copy and paste this into your `.env` file and restart the game. The computer will now have a trained model behind it. 

By setting the `UPDATE_AFTER` variable the game will automatically try and pull in a new model after these number of games. It is up to the demonstrator to manually re run the models through the Machine Learning for kids platform. The game will update the model if there has been an update and increase the training round on the game board. 

After several rounds the computer should win more and draw more, the ultimate result is the game always ends in a draw. 

