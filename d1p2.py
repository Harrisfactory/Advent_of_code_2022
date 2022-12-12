with open ("d1p1.txt", "r") as myfile:
    
    data = myfile.read()

    cur_max = 0

    fin_max = 0

    elves = []

    top_elves = []

    with open('d1p1.txt') as f:
        lines = f.readlines()

    for line in lines:
        if line == '' or line == '\n':
            elves.append(cur_max)
            cur_max = 0
        else:
            cur_max+=int(line)

    elves_sorted = sorted(elves, reverse=True)

    elves_summed = elves_sorted[0] + elves_sorted[1] + elves_sorted[2]
    

            
    print(elves_summed)


 