def snakes (player):
    x = {16:6,46:25,49:11,62:19,64:60,74:53,89:68,92:88,95:75,99:80}
    return player if player not in x else x[player]
def ladders (player):
    x = {2:38,7:14,8:31,15:26,21:42,28:84,36:44,51:67,71:91,78:98,87:94}
    return player if player not in x else x[player]

class SnakesLadders(): 
    def __init__(self, tom=0):
        self.tom = tom
    def play(self, die1, die2):
        global player_1, player_2, Round
        if self.tom == 0:
            player_1 = 0
            player_2 = 0
            Round = 1
            self.tom += 1
        if player_1 == 100 or player_2 == 100:
            return 'Game over!'
        if Round % 2 == 0:
            player_2 += die1 + die2 
            if player_2 > 100:
                player_2 = 100 - player_2%100
            player_2 = snakes(player_2)  
            player_2 = ladders(player_2)
            p, player = 'Player 2' , player_2 
        else:
            player_1 += die1 + die2 
            if player_1 > 100:
                player_1 = 100 - player_1%100
            player_1 = snakes(player_1)
            player_1 = ladders(player_1)
            p, player = 'Player 1' , player_1     
        
        if player == 100:
            return str(p) + ' Wins!'
        if die1 == die2:
            Round == Round
        else:
            Round += 1     
        return str(p) +' is on square ' +str(player)