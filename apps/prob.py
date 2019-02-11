def showInstructions():
    #print a main menu and the commands
    print("RPG Game")
    print("========")
    print("commands:")
    print("'go [direction]'")

def showStatus():
    #print the player's current status
    print("___________________")
    print("you are in the " + rooms[currentRoom]["name"])
    print("___________________")

#a dictionary linking a room to the other room positions
rooms = {
    1 : { "name" : "Hall" ,
          "east" :  2, 
          "south":3 } ,
          
    2 : {"name"  :"Bedroom" ,
          "west" :1 ,
          "south":4 } ,

    3 : {"name"  :"Kitchen" ,
         "north" :1 , }  ,

    4 : {"name"  : "Bathroom" ,
         "north" :2}   

        }
#start the player in room 1
currentRoom = 1

showInstructions()

#loop infinitely
while True:
    showStatus()

    #get the player's next 'move'
    #.split()breaks it up into a list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = input (">").lower().split()

    #if they type 'go' first
    if move[0] == "go":
        #check that they are allowed where they want to go
        if move[1] in rooms [currentRoom]:
            #set the current room to new room
            currentRoom = rooms[currentRoom][move[1]]
            #there is no door (link) to the new room
        else:
            print("you can't go that way!")


