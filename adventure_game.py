from sys import exit
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("this room is not yet configured.")
        exit()


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #print out last scene
        current_scene.enter()


class FountainRoom(Scene):

    def enter(self):
        print(dedent("""
        You wake up in a courtyard.
        You try to sit up, but you have a headache and you can't feel your leg.
        To your left is a satchel bag.
        And to you right is a small bottle with clear liquid.
        What do you grab first? a) bottle or b) satchel.
        """))

        action = input("> (type a letter and press enter to submit) \n")

        if action == "a" or action == "A" or action == "a)":
            print(dedent("""
            You drink the strange liquid. Instantly, your headache eases.
            You find the strength to sit up, but your leg is still broken.
            You open the satchel next...
            """))

            input("> (press enter) ")

            print(dedent("""
            Inside the satchel is a small note and a bundle of bread. The note reads:
            \"Take this bread; it will heal all your current afflictions.
            You may save the potion for a later time; it will only heal one affliction.\"
            """))

        elif action == "b" or action == 'B' or action == "b)":
            print(dedent("""
            You reach for the satchel. Inside is a small note and a bundle of bread.
            The note reads:
            \"Take this bread; it will heal all your current afflictions.
            You may save the potion for a later time; it will only heal one affliction.\"
            """))

            input("> (press enter)")

            print(dedent("""
                You eat the bread, and instantly your headache is gone and your leg heals.
                You put the potion in the satchel for later.
                """))
        else:
            print("error.")
            exit(1)

        input("> ")

        print(dedent("""
            You stand up.
            In front of you is a large wooden door.
            Above it reads a sign:
            \"enter if you dare!\"
            You don't head the sign because you aren't very wise.
            """))

        input("> ")

        return 'throne_room'

class ThroneRoom(Scene):
    def enter(self):
        print(dedent("""
            You open the door and walk through it.
            Before you stands a presumed wizard.
            (He had a pointy hat and a wand)
            He speaks in a booming voice.
            """))

        boss_words = [
            "Ha Ha HAA",
            "You think you can beat me?",
            "That is hysterical. I laugh in your face.",
            "I learned all my wizard skills from an Obi-Wan-Kenobi/Gandalf-type figure.",
            "Therefore, I am invincible!",
        ]

        input("> ")

        for x in boss_words:
            print(x)
            input("> ")

        print(dedent("""
            How do you wish to proceed?
            a) attack with your lightning magic
            b) inquire after the wizard's mother's health
            """))

        action = input("> ")

        if action == "a" or action == "A" or action == "a)":
            print(dedent("""
                You are instantly knocked out by the force of a metal club.
                You don't notice your last breaths.
                You die.
                (although, once again, you are not aware of this)
                """))
            return 'death'
        if action == "b" or action == 'B' or action == "b)":
            return 'finished'



class Death(Scene):

    def enter(self):
        angel_voice = [
            "Welcome to death.",
            "Refreshments are in the back...",
            "...including my special raspberry scones.",
            "Please take a seat as you wait your final destination.",
            "...",
            "Or don't. It's not like your legs become fatigued anymore.",
            "(P.S. that's funny because you're dead)",
        ]
        for x in angel_voice:
            input("> ")
            print(x)

        input(" ")
        exit(0)

class Finished(Scene):
    def enter(self):
        print(dedent("""
            The wizard blushes. He assures you that his mother is in great health.
            You say that this is nice.
            He asks you if you would like to go out for coffee.
            The two of you enjoy lattes and raspberry scones.
            """))
        input(" ")
        exit(0)

class Map(object):

    scenes = {
        'fountain_room': FountainRoom(),
        'throne_room': ThroneRoom(),
        'death': Death(),
        'finished': Finished(),
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('fountain_room')
a_game = Engine(a_map)
a_game.play()
