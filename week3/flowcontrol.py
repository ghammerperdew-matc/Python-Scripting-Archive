#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: This is a chooose your own adventure game.

If you haven't watched Black Mirror: Bandersnatch on Netflix yet, you really should.
Interactive TV is an interesting concept.
"""

print(
"""
You are walking through the woods and notice a small cave.
Do you venture into the cave?
""")

cave = input("Y/N? -> ")

if cave.upper() == "Y":

    print(
    """
    You walk into the cave and are met with three paths.
    Which path do you choose?
    """)

    # gets input for path selection
    path = input("Enter 1, 2 or 3 >>")


    #########################
    ## Path Number 1 logic ##
    #########################

    if path == "1":

        print(
        """
        You start walking down the first path.

        You come to a round room with a small clay cup on a pedestal in the middle.
        The room is lit from an opening in the ceiling shining directly on the pedestal.
        The cup is filled with what appears to be red wine.

        What do you do?

        1. Pick up the cup and drink the wine
        2. Empty the wine onto the floor and take the cup home
        3. Leave the cave and continue your walk
        """)

        cup = input("Enter 1, 2 or 3 >>")

        if cup == "1":

            print(
            """
            The wine is actually poison. You die.
            Why would you drink strange liquids you found in a random cave?
            """)

        elif cup == "2":

            print(
            """
            The wine started reacting with the cave floor when you dumped it out.
            It was probably poison.
            But hey at least you have neat cup to use when you go home for dinner.
            Speaking of which, dinner's probably ready, so it's time to go. 
            """)

        else:

            print(
            """
            That's a good call.
            A cup filled with wine on a pedestal in a cave sounds like a trap.
            Dinner's probably ready, so it's time to head home anyway.
            """)


    #########################
    ## Path Number 2 Logic ##
    #########################

    elif path == "2":

        print(
        """
        A short distance down the second path, you meet the edge of a cliff.
        There is a relatively new rope tied around a rock formation that leads down the cliff.
        Your flashlight is broken, and you can barely see past the edge.
        You hear a shuffling noise in the darkness
        What do you do?

        1. Climb down the cliff using the rope
        2. Yell at whatever is moving around in the darkness
        3. Leave and continue your walk

        """)

        rope = input ("Enter 1, 2 or 3 >> ")

        if rope == "1":

            print(
            """
            About 30 feet down the cliff your arms give out and you fall.
            Fortunately, you only fell 6 inches before you hit solid ground.
            Unfortunately, there was something waiting for you at the bottom of the cliff...
            You are never seen again.
            """)

        elif rope == "2":

            print(
            """
            The shuffling sounds stop and the rope starts to move.
            Before you can even blink a monstrous, hairy arm is reaching over the side of the cliff.
            It grabs your ankle and you fall into the darkness without another sound.
            Maybe you shouldn't yell at things in caves.
            """)

        else:

            print(
            """
            It looks like you've learned it isn't the dark you should be afraid of.
            The things that live in it, though, obviously make you think twice about your actions.
            Dinner is probably ready by now, so you should probably head home anyway.
            """)


    #########################
    ## Path Number 3 Logic ##
    #########################

    elif path == "3":

        print(
        """
        The third path continues on for what feels like miles.
        Finally, you see light around a bend in the path. 
        You walk into the light to find yourself in front of a small pool of crystal clear water.
        It appears that it is fed by a natural spring.
        What do you do?

        1. Take a drink from it
        2. Toss a coin into it
        3. Leave and continue your walk

        """)

        water = input("Enter 1, 2 or 3 >> ")

        if water == "1":

            print(
            """
            Nothing extraordinary happens after taking a drink.
            The water is pretty tasty though.
            You decide to head home after taking one more drink.
            10 years later when you realize you haven't aged at all, you start to wonder if that pool
            was magical....
            """)

        elif water == "2":

            print(
            """
            You make a silent wish and toss your last penny into the water.
            The wish had something to do with being rich.
            You leave the cave and walk home, and nothing else happens.
            It wasn't a wishing well after all - just a waste of a penny.
            """)

        else:

            print("That water looks clear, but it's probably not safe to drink.")
            print("It's probably time to head home for dinner anyway.")


    #######################
    ## Choice not listed ##
    #######################

    else:

       print("Yeah coming in here probably wasn't a good idea. Good call on leaving.")


else:

     print("Caves are pretty dangerous, so you're probably smart to not go in.")
