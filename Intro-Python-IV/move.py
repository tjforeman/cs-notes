class Room:
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

        r0 = Room('starting room,', "this is where you start")
        r1 = Room('Next room', 'this is where you go ')

        r0.n_to = r1
        r1.s_to = r0

        player_location = r0

        print(player_location.name)
        print(player_location.desc)


        dir = input("enter a direction to move")

        if dir == "n":
            player_location = player_location.n_to

        elif dir == 's':
            player_location = player_location.s_to
        elif dir == 'w':
            player_location = player_location.w_to
        elif dir == 'e':
            player_location = player_location.e_to
        else:
            print(f"{dir} is not a direction i'm aware of")