import random

player_pos = 1
npc_pos = 1
def board():
    print('.'*(player_pos-1) + '[P]' + '.'*(30-player_pos) + 'Goal')
    print('.'*(npc_pos-1) + '[C]' + '.'*(30-npc_pos) + 'Goal')

board()
print('##### Game Start!! #####')

while True:
    input('Press Enter to advance your piece >>')
    player_pos = player_pos + random.randint(1,6)
    if player_pos > 30:
        player_pos = 30
    board()

    if player_pos == 30:
        print('You win!!')
        break

    input('Press Enter to advance NPC piece >>')
    npc_pos = npc_pos + random.randint(1,6)
    if npc_pos > 30:
        npc_pos = 30
    board()

    if npc_pos == 30:
        print('You lose...')
        break
