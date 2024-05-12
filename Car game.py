command = "Hey"
started = False
while True :
    command = input ('>') .lower()
    if command == "start":
        if started:
            print ("Car is already started!")
        else: 
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car already stopped!")
        else: 
         started = False 
         print("Car stopped!")
    elif command == "help":
        print ( """ Start - To start the car
 Stop - To stop the car
 quit - To quit""")
    elif command == "quit" :
        print("You quit....")
        break
    else:
        print ("Sorry, I don't understand this!")

        
