from sys import exit
from random import randint
from textwrap import dedent

class scene(object):

    def enter(self):
        print("This scene isn't yet configured")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene=self.scene_map.opening_scene()
        last_scene=self.scene_map.next_scene('finished')

        while current_scene!= last_scene:
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene_name) 

        current_scene.enter()


class death(scene):
    quips=["you died.  you kinda suck at this.",
           "your mom would be proud ....if she were smarter",
           "you such a luser",
           "I have asmaller puppy better at this.",
           "you're worse than your dad jokes"]

    def enter (self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Centralcoridoor(scene):

    def enter(self):
        print(dedent("""
                    The Gothans of planet percal #25 have invaded your ship and 
                    destroyed your entire crew.you are the last surviving
                    members of your last mission is to get nuetron destruct bomb
                    from the weapons Armory. put it to the bridge and blows the 
                    ship up after getting into an escape pod.

                    you 're running down the central corridoor to the weapons
                    Armory when gothons jump out ,red scaly skin,dark grimy teeth
                    and evil clown costume flowing around his hate filled body
                    He's blocking the door to the Armory and about to pull a
                    weapon to blast you.
                    """))    
                    
        action =input(">")

        if action =="shoot":
            print(dedent("""
                  Quick on the draw you yank out your blaster and fire
                  it at the Gothon. His clown costume is flowing and moving
                  around his body,which gthrows of your aim .your laser 
                  hits his costume but misses him entirely.This completely
                  ruins his band new costume,his mother brought him.which 
                  makes him flys into an insane range and blast you 
                  repletedly in the face until  you are dead .then he eats 
                  you."""))

        elif action =="dodge!":
            print(dedent("""
                  like a world class boxer you dodge, weave and slip and 
                  slide right as the gothon 's blaster cranks a laser
                  past your head . In the middle of your artful dodge
                  your footslip and you bang your head on the metal wall
                  and pass out.you wake up shortly after only to die as
                  gothon stomps and on your head on eats you
                   """))
            return death

        elif action =="tell a joke":
            print(dedent("""
                  Lucky for you they made learn Gothon insults in the 
                  acadamy. you tell the one Gothon joke you know:
                  lbhe zbgure vf fb sng , jura fur fvgf . Gothons tries 
                  not to laugh ,then bust out laughing and can't move
                  while he is laughing you run up and shoot you him square 
                  in the head putting him down ,and jump through the 
                  weapon armory door.
                  """))
            return laser_weapon_army

        else:
            print("DOESN'T COMPUTE !")
            return 'central_corridoor' 

class LaserWeapoArmory(scene):

    def enter(self):
        print(dedent("""
              you do dive roll into the weapon armory,crouch and scan
              the room for more Gothons that might be hiding.it's died
              quiet,too quiet .you stand up and run  to the far side 
              of the room and find a nuetron bomb in its container.
              there is a keypad lock on box and you need the code to 
              get the bomb out. if you get the code wrong 10 times
              and the lock closes forever and you can't get the bomb. 
              the code is 3 digits
               """))

        code=f"{radiant(1,9)}{radiant(1,9)}{radiant(1,9)}"
        guess=input("[keypad]>")
        guess=0

        while guess != code and guess<10:
            print("BZZEDD!")
            guess+=1
            guess=input("[keypad]>")

        if guess == code:
            print(dedent("""The container clicks open and seal breaks,
                         letting gas out.you grab the nuetron bomb run as 
                         fast as you can to the bridge where you must place
                         it in the right spot.
                         """)
            return 'the_bridge'

        else:
            print(dedent("""print the lock buzzes one last time and you 
                         hear a sickening and meltening sound as the mechanism
                         fused together.you decide to sit there,and finally
                         the Gothons blow up the ship from their ship and 
                         you die """))

            return 'death'

class TheBridge(scene):

    def enter(self):
        print(dedent("""you burst on to the Bridge with nuetron destructing 
                     bomb under your arm surprise 5 Gothons who are trying 
                     to take control of the ship.Each of them has even uglier 
                     clown costume than the last.They haven't pull their 
                     weapons out yet.As they see the active bomb under your 
                     arm and don't want to set it off."""))

        action = input(">")

        if action == "throw the bomb":
            print(dedent("""
                         In panic you throw the bomb at the group of Gothons
                         and make a leap of the door.Right as you drop it Gothons
                         start shoots you right back in the killing you.As you die 
                         Gothons disarm the bomb.you knowing they will probably
                         blows up when it goes off"""))
            return 'death'

        elif action=="slowly place the bomb":
            print(dedent("""
                         you point your blaster at the bomb under your arm and
                         Gothons put their hands up and start to sweat.you inch 
                         backward to the door ,punch the close button and blast
                         the lock so the Gothons can't get out  and now the bomb 
                         is placed .you run to the escape pod to get off this tin 
                         can."""))

            return 'escape_pod'

        else:
            print("DOESN'T COMPUTE!")
            return "the_bridge"

class Escapepod(scene):

    def enter(self):
        print(dedent(""" 
                     you rush through the ship despertely trying to make it to
                     the escape pod before whole ship explodes.It seems likely
                     hard any Gothons are on the ship,so you run clear of 
                     interference . you get to the chamber with the escape pods
                     and you need to pick one to take .some of them could damaged 
                     but you don't have a time to look.there're 5pods 
                     which one do you take?"""))

        good_pod = radiant(1,5)
        guess= input("[pod#]>")        

        if int(guess) != good_pod:
            print(dedent("""you jump into pods {guess}and hit eject button
                         The pod escapes out into void of space,then impoldes
                         as a hull ruptures,crushing your body into jam jelly
                         """)) 
            return 'death'

        else:
            print(dedent("""you jump into pod {guess} and hit the ejection button
                         The pods easily slides out into space heading to the planet
                         below .As it flies to the planet,you look back your ship
                         implode and explode like a bright star taking out gothon ships
                         at same time . you won!
                         """)) 

            return 'finished'

class Finished(scene):

    def enter(self):
        print("You won, Good job!")
        return 'finished' 


class Map(object):
    scene ={
    'central_corridoor': Centralcoridoor()
    'laser_weapon_armory':LaserWeapoArmory()
    'the_bridge':TheBridge()
    'escape_pod':Escapepod()
    'death':death()
    'finished':Finished()
    }

    def __init__(self,start_scene):
        self.start_scene=start_scene

    def next_scene(self,scene_name):
        val=map.scene.get(scene_name)   
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map=map('central_coridoor')
a_game=Engine(a_map)
a_game.play()             


