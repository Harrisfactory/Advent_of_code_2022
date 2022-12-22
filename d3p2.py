

with open('d3p1.txt') as f:
    lines = f.readlines()


badge = []

letters = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
upper_letters = {'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}

k = 3

breaker = False

i = 0

while i < len(lines):
    if breaker == True:
        break
    for j in range(len(lines[i])):

        if i + 2 < len(lines):
            if lines[i][j] in lines[i+1] and lines[i][j] in lines[i+2] and lines[i][j] != '\n':
                if lines[i][j].isupper():
                    badge.append(upper_letters[lines[i][j]])
                else:
                    badge.append(letters[lines[i][j]])
                
                if i + 3 >= len(lines):
                    breaker = True
                    break
                else: 
                    i = i + 3
                    print("next line is: " + str(i))
                    break
    
print(badge)
print(sum(badge)) #30438 is too high #7242 is too high
    