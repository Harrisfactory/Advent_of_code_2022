

with open('d2p1.txt') as f:
    lines = f.readlines()

score = 0

elf_to_me = {'A':'X', 'B':'Y', 'C':'Z'}

elf_beats_me = {'A':'Z', 'B':'X', 'C':'Y'}

elf_loses_to_me = {'C':'X', 'A':'Y', 'B':'Z'}

me_beats_elf = {'X':'C', 'Y':'A', 'Z':'B'}

moves = {'X':1, 'Y': 2, 'Z':3, 'A':1, 'B':2, 'C':3}

round_score = {'loss':0, 'draw':3, 'win':6}

for line in lines:
    elf_me = line.split()
    elf = elf_me[0]
    me = elf_me[1]

    if me == 'X':
        #need to lose
        score += round_score['loss'] + moves[elf_beats_me[elf]]
        print('you lost: elf had ' + elf + ' you had ' + me + ' score ' + str(round_score['loss'] + moves[elf_beats_me[elf]]))
    elif me == 'Y':
        #need to draw
        score += round_score['draw'] + moves[elf_to_me[elf]]
        print('you tied: elf had ' + elf + ' you had ' + me + ' score ' + str(round_score['draw'] + moves[elf_to_me[elf]]))
    elif me == 'Z':
        #need to win
        score += round_score['win'] + moves[elf_loses_to_me[elf]]
        print('you won: elf had ' + elf + ' you had ' + me + ' score ' + str(round_score['win'] + moves[elf_loses_to_me[elf]]))


print(score)