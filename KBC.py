list = [
        ["    1.who is richest man in the world?", 'elon musk', 'bill gates', 'mukesh ambani', 'jeff bezos', 1],

        ["    2.world's most populated city", 'mumbai', 'tokyo', 'new york', 'rio de jeneiro', 2],

        ["    3.what is the capital of india", 'delhi', 'mumbai', 'kolkata', 'bengluru', 1],

        ["    4.what is the capital of united states", 'san francisco', 'washington D.C.', 'new york', 'boston', 2],

        ["    5.which animal is called 'the king of the jungle' ", 'tiger', 'lion', 'beer', 'elephant', 2],

        ["    6.who was the first person to walk on the moon", 'fred haise', 'david scott', 'neil armstrong', 'aldrin', 3],

        ["    7.what is the capital of australia", 'melbourne', 'sydney', 'adelaide', 'perth', 2],

        ["    8.what is the largest river in the india", 'gangas', 'godavari', 'yamuna', 'narmada', 1],

        ["    9.what is the largest ocean in thge world", 'atlantic ocean', 'indian ocean', 'pacific ocean', 'arctic ocean', 3],

        ["    10.what is the national fruit of india", 'guvava', 'banana', 'apple', 'mango', 4],

        ["    who is the founder of oyo", 'ritesh agraval', 'sachin bansal', 'falguni nayar', 'kunal shah', 1],

        ["    who is the owner of spacex", 'jeff bezos', 'richard branson', 'elon musk', 'nasa', 3],

    ]

level= [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,750000,5000000,7500000]

for i in range(0, len(list)):
    question = list[i]
    print(f"question for Rs. {level[i]}")
    print(question[0])
    print(f"\na.{question[1]}         b.{question[2]}")
    print(f"c.{question[3]}       d.{question[4]}\n")

    reply = int(input("enter the answer:  "))
    if(reply == question[-1]):
        print(f"you just won....{level[i]}\n")
        if(i<4):
            amount = level[i] # benefit under 10000 mark //if u lose under 10000 mark u would surely get last winning
        elif(i == 4 ):
            amount=10000
            time.sleep(5)
        elif(i == 9):
            amount = 320000
            print(f"jackpot of {level[-1]} is just opened...")
        elif(i == 11):
            amount = 5000000

    else:
        print("u loose...")
        break
print(f"ur final amount is Rs.{amount}")