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
Make a .env file in the location you are running the code. To run the game first go  https://machinelearningforkids.co.uk/ make an account and set up a Noughts and Crosses projects. Go to Make > Python then copy the key in to the .env file. 
Then install the game inside your conda environment with
```
pip install setup.py
```
To start the game open a terminal and type:
```
noughtsandcrosses
```
The gameboard will appear. 