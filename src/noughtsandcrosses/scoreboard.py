import os
import pygame


class Scoreboard:
    def __init__(self):
        self.HUMAN = {"W":0, "D":0, "L":0}
        self.COMPUTER = {"W":0, "D":0, "L":0}
        self.train_round = 0
        self.last_update = None
        self.no_games = 0

    def update_scores(self, winner):
        if winner=="HUMAN":
            self.HUMAN["W"] +=1
            self.COMPUTER["L"] +=1
        elif winner=="COMPUTER":
            self.COMPUTER["W"] +=1
            self.HUMAN["L"] +=1
        else:
            self.COMPUTER["D"] +=1
            self.HUMAN["D"] +=1
    
    def update_train_round(self, model_metadata):
        if model_metadata and self.last_update:
            if self.last_update < model_metadata["lastupdate"]:
                self.last_update = model_metadata
                self.train_round += 1
        elif model_metadata and not self.last_update:
             self.last_update = model_metadata
        else:
            # reset train round to 0 if model is None
            self.train_round=0        

            

def display_scoreboard(scoreboard, screen):
     WHITE = (255, 255, 255)
     score_font = pygame.font.SysFont('arial', 20)
     header = score_font.render( "PLAYER:      W   D   L", True, WHITE)
     screen.blit(header, (4,4))
     score_human = score_font.render(f'HUMAN:   {scoreboard.HUMAN["W"]} {scoreboard.HUMAN["D"]} {scoreboard.HUMAN["L"]}', True, WHITE)
     screen.blit(score_human , (4, 28))
     score_computer = score_font.render(f'COMPUTER:  {scoreboard.COMPUTER["W"]} {scoreboard.COMPUTER["D"]} {scoreboard.COMPUTER["L"]}', True, WHITE)
     screen.blit(score_computer , (4, 56))
     train_round = score_font.render(f' TRAIN ROUND: {scoreboard.train_round }', True, WHITE)
     screen.blit(train_round , (300, 4))
     pygame.display.update()

