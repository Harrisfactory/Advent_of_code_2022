

with open('d3p1.txt') as f:
    lines = f.readlines()


in_both = []

letters = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
upper_letters = {'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}

for line in lines:
    compartment_one = line[:(len(line)//2)]
    compartment_two = line[(len(line)//2):]

    for letter in compartment_one:
        if letter in compartment_two:
            if letter.isupper():
                in_both.append(upper_letters[letter])
                break
            else:
                in_both.append(letters[letter])
                break
    

print(sum(in_both))
    
