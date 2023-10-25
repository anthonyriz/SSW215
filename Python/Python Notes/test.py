import random
f = open("TEST1.txt", 'w')
for count in range (500):
    number = random.randint (1,500)
    f.write (str(number) + "\n")
f.close ()
