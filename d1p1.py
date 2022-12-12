with open ("d1p1.txt", "r") as myfile:
    
    data = myfile.read()

    cur_max = 0

    fin_max = 0

    with open('d1p1.txt') as f:
        lines = f.readlines()

    for line in lines:
        if line == '' or line == '\n':
            cur_max = 0
        else:
            cur_max+=int(line)
            fin_max = max(cur_max, fin_max)
    print(fin_max)
        
