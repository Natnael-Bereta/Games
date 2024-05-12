guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input("Guess "))
    # print ("Guess ")
    guess_count +=1
    if guess == 8:
        print ('You won!')
        break
else:
    print("You fail. Try again!")