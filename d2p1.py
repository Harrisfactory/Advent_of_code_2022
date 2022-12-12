with open ("d1p1.txt", "r") as myfile:
    
    data = myfile.read()

    with open('d2p1.txt') as f:
        lines = f.readlines()

    score = 0

    elf_to_me = {'A':'X', 'B':'Y', 'C':'Z'}

    elf_beats_me = {'A':'Z', 'B':'X', 'C':'Y'}

    me_beats_elf = {'X':'C', 'Y':'A', 'Z':'B'}

    moves = {'X':1, 'Y': 2, 'Z':3}

    round_score = {'loss':0, 'draw':3, 'win':6}

    for line in lines:
        elf_me = line.split()
        elf = elf_me[0]
        me = elf_me[1]
        
        if elf_to_me[elf] == me:
            score += round_score['draw'] + moves[me]
        elif elf_beats_me[elf] == me:
            score += round_score['loss'] + moves[me]
        elif me_beats_elf[me] == elf:
            score += round_score['win'] + moves[me]

    
    print(score)
        
    
