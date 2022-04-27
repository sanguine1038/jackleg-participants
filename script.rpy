
# yo yo yo! this is how you make a note in rpy

# define e = Character("Eileen")
# define sh = Character("Shoddy")


#tutorials and shit
# THIS IS IMPORTANT ->>>>> https://www.renpy.org/doc/html/text.html
# "An example of {b}bold test{/b}."
# "{color=#f00}Red{/color}" * #ff784c for important text, #99ccff for thinking text, #66cc40 for narrator text
# {size=-10}Smaller{/size}
# with hpunch makes the screenshake left and right, with vpunch makes the screenshake up and down
# {cps=10}This makes text slowly appear, dont know how to make it default so just have this everywhere ITS IN OPTIONS YOU DOOFUS

#transitions
define fade = Fade(0.5, 0.0, 0.5)

#sounds1!
define sounds = ['audio/BEEP.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            #THANKS Aquapaulo

        elif event == "interact" or event == "interact": #RANDOM BS FIX LATER!!
            renpy.sound.stop()


#example of a character with the typing sound
#   define Type = Character("Character with typing", callback=type_sound)
#just don't add the character callback if you don't want that ound
#   define NoType = Character("Character without typing")
#regular narration that doesn't have a character attached to it, add an # to it if you don't want that
#   define narrator = Character("", callback=type_sound)

#bad guys LMAO
define b = Character("Botsun", callback=type_sound)
define so = Character("Sou")
define who1 = Character("??? (A)", callback=type_sound)
define who2 = Character("??? (B)", callback=type_sound)
define who3 = Character("??? (C)", callback=type_sound)

#alt names
define who = Character("???", callback=type_sound)
define b2 = Character("Weird Guy", callback=type_sound)
define so2 = Character("Green-haired Man", callback=type_sound)

define s = Character("Strange Woman", callback=type_sound)
define k2 = Character("Blue-haired Man", callback=type_sound)
define h2 = Character("Pink-haired Girl", callback=type_sound)
define m2 = Character("Woman with big hat", callback=type_sound)
define a2 = Character("Hooded Girl", callback=type_sound)
define ha2 = Character("Man with glasses", callback=type_sound) #bryan
define me2 = Character("Woman in uniform", callback=type_sound)
define ku2 = Character("Girl in uniform", callback=type_sound)
define sh2 = Character("Beanie Man", callback=type_sound)

#main characters
define r = Character("Ranmaru", callback=type_sound)
define k = Character("Kurumada", callback=type_sound)
define h = Character("Hinako", callback=type_sound)
define m = Character("Mai", callback=type_sound)
define a = Character("Anzu", callback=type_sound)
define ha = Character("Hayasaka", callback=type_sound)
define ku = Character("Kugie", callback=type_sound)
define sh = Character("Shin", callback=type_sound)
define me = Character("Megumi", callback=type_sound)

define config.debug_text_overflow = False

init:
#    image bg road = "test.png"

    $ flash = Fade(.15, 0, .15, color="#fff")

init:

    $ despair = Fade(.1, 0, .1, color="#ff0000")



#    play music "audio/seme-KS-ZN.ogg"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
label start:

    stop music fadeout 1.0

    menu:
        "go to game":
            jump start2
        "Go to editor":
            jump BLAHBLAHBLAH

#label anzu_death:
#
#    show anzu death3:
#            xzoom 0.36 yzoom 0.35
#
#    a "Thank you for having me as a sacrifice, please don’t hurt anyone else."

label start2:

    scene blackbg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    who "{color=#66cc40}I love prodigies.{/color}"

    who "{color=#66cc40}Natural-born talent. A point the common person can never approach. The most radiant of anomalies.{/color}"

    who "{color=#66cc40}But sometimes I ask myself ‘Is this really what I want?’ normally in a midst of panic wondering what I really need.{/color}"

    who "{color=#66cc40}Just for this one time, I’m going to throw away what I want. See the opposite side in the spectrum.{/color}"

    who "{color=#66cc40}What do they want?{/color}"

    who "{color=#99ccff}(...){/color}"

    who "What do you think?"

    show sara-1
    with dissolve

    s "Delete everything. Restart it, take as much time as you need."

    hide sara-1
    with dissolve

    who "{color=#99ccff}(...){/color}"

    who "Urk.."

    who "Ugh..."

    who "What...what happened?"

    who "W-Where am I?!"

    who "What's going on?!"

    who "{color=#99ccff} (Let me just think a bit.) {/color}"

    who "{color=#99ccff} (I am...) {/color}"

    show ranmaru-21
    with dissolve
    play sound "audio/Accent21-1.ogg"
    with flash

    r "{color=#99ccff} (I am Ranmaru Kageyama. I’m just some High Schooler. That goes to…) {/color}"

    hide ranmaru-21
    show ranmaru-24

    r "{color=#99ccff} (...) {/color}"

    hide ranmaru-24
    show ranmaru-23

    r "{color=#99ccff} (Come on..think! Think!) {/color}"

    r "{color=#99ccff} (...) {/color}"

    play sound "audio/surprise.ogg"
    with hpunch

    r "{color=#99ccff} (Shit! I can’t remember what school I go to…) {/color}"

    hide ranmaru-23
    show ranmaru-24

    r "Let me try to calm down first..."

    r "{color=#66cc40}(...){/color}"

    hide ranmaru-24
    with dissolve


    r "{color=#66cc40}(Am I..){/color}"

    scene test
    play sound "audio/Accent21-1.ogg"
    with flash


    r "{color=#66cc40}Sitting down..?{/color}"

    r "{color=#66cc40}I quickly stand up to see where I am.{/color}"

    r "{color=#66cc40}Everything is blurry…I can’t see a thing.{/color}"

    play sound "audio/button04a.ogg"

    "{color=#66cc40}*Beep Beep!*{/color}"

    r "..."

    play sound "audio/Accent21-1.ogg"
    with flash

    r "Huh?"
    play sound "audio/Accent21-1.ogg"
    with flash

    who1 "…Beginning voiced guidance. "

    who1 "The First Trial will now begin."

    r "{color=#66cc40}First Trial?{/color}"
    play sound "audio/Accent21-1.ogg"
    with flash

    who1 "In front of you will is a plate of food. One course is completely normal and delicious while the other is…"

    who1 "Well it’s still quite delicious, it just has a razor blade in it."

    r "{color=#99ccff}(!?){/color}"

    play sound "audio/surprise.ogg"
    with hpunch
    who2 "Bastard! Stick to the script!"

    play sound "audio/surprise.ogg"
    with hpunch
    who1 "Derr, Sorry!"

    who1 "Eat one of the courses, if you pick the correct one you’ll have a good meal however if you eat the wrong one!"

    who1 "It’ll cut up your insides!"

    who1 "It’s also timed so you can’t put it to your ear to hear the blades moving. It’ll only activate once moisture is applied to it."

    who1 "The time limit is just a couple seconds, which I forgot. So hurry up! Don’t keep the others waiting!"

    who1 "..."

    who1 "Did I do good, boss!?"

    who3 "Duhhh..Sure you did."

    who3 "Wait a second… Turn that thing off!"

    play sound "audio/button04a.ogg"

    "{color=#66cc40}*Beep Beep!*{/color}"

    r "..."

    play sound "audio/Accent21-1.ogg"
    with flash

    r "What..?"

    r "Excuse me?!"

    play sound "audio/surprise.ogg"
    with hpunch
    play music "audio/pani.ogg"

    r "Uhhh! Uhh! Dear god!"

    r "What do I do??"

    r "The recorder told me to eat one of the plates… but which one?!"

    r "What the hell is going on here!?"

    r "{color=#99ccff}(I rubbed my eyes a bit to clear up my still blurred vision.){/color}"

    scene test2
    with dissolve

    r "{color=#99ccff}(Everything is a bit more clear.){/color}"

    r "{color=#99ccff}(In front of me is a full course dinner. Just gotta follow what the recording said...){/color}"

    r "{color=#99ccff} (I can’t see any way out of this!) {/color}"

    show ranmaru-23
    with dissolve

    play sound "audio/ding.ogg"
    with despair
    r "{color=#99ccff}(I have to..risk my life here…){/color}"

    hide ranmaru-23 with dissolve

    label test2:
    r "{color=#99ccff}I gotta look around!{/color}"
    window hide dissolve
    show screen gameUI
    jump test2

label door_pressed:
    hide screen gameUI
    r "{color=#99ccff}(Agh! I can't open the stupid door!){/color}"
    jump after_choice

label meal_pressed:
    hide screen gameUI
    r "Alright! Here goes nothing!"
    r "{color=#99ccff}(I hesitate a bit before I eat any of the meals.){/color}"
    r "{color=#99ccff}(Which one do I pick!?){/color} "

menu:
    "Eat the Rotisserie Chicken":
        r   "Alright! Here goes nothing!"
        r   "{color=#99ccff}(I hesitate a bit before I eat the Rotisserie Chicken.){/color}"
        r   "{color=#99ccff}(Is it really this meal I want to eat?){/color}"
    "Eat the Sashimi":
        r   "Alright! Here goes nothing!"
        r   "{color=#99ccff}(I hesitate a bit before I eat the Sashimi.){/color}"
        r   "{color=#99ccff}(Is it really this meal I want to eat?){/color}"
        jump after_bad_choice
    "Don't eat anything":
        r "I-I..."
        r "I- can't do it!"
        jump after_choice
menu:
    "Yes":
        jump after_right_choice
    "No":
        r  "I-I..."
        r  "I can't bring myself to do it!"
        jump after_choice


label after_choice:
    hide screen gameUI
    with hpunch
    r "God damnit!"
    jump test2

label after_bad_choice:

menu:
    "Yes": #FISH IS DISGUSTING LET ME HOMEBOY FREEEEE

        r "Ok! Here I go!"
        stop music fadeout 1.0
        r "{color=#99ccff}(I shut my eyes as I’m chewing.){/color}"
        scene black
        with dissolve
        r "{color=#99ccff}(It just dawned on me that I’m chewing a meal that might have a razor blade to save my life.){/color}"
        r "{color=#99ccff}(...){/color}"
        r "{color=#99ccff}(The 'meal' was anything but delicious…){/color}"
        r "I… I did it?"
        play sound "audio/Accent09-1.ogg"
        with flash
        r "I did it! Yes!"
        play sound "audio/surprise.ogg"
        with flash
        r "Can I go home now?!"
        r "{color=#99ccff}(I ask that as if anyone is watching.){/color}"
        r "{color=#99ccff}(I skim the room real quick.){/color}"
        pause 0.7
        with hpunch
        with despair
        play music "audio/tense.ogg"
        r "{color=#ff0000}(There were no cameras.){/color}"
        r "{color=#ff0000}(Didn’t I just…put my life at risk?){/color}"
        r "{color=#99ccff}(I can't think straight!!){/color}"
        r "{color=#99ccff}(What's going on?!){/color}"
        r "Is my neck tightening?!"
        r "*Huff* *Huff*"
        r "{color=#99ccff}(Am I...){/color}"
        with despair
        play sound "audio/horror_piano chord3.ogg"
        r "{color=#99ccff}(Dying..?!){/color}"
        scene black
        with fade                                   #JUST REALIZED THAT SCENE GOES FIRST THEN TRANSITION
        stop music fadeout 1.0
        play sound "audio/correct2.ogg"
        r "..."
        scene test3
        with flash
        r "{color=#99ccff}(...huh?){/color}"
        r "{color=#99ccff}(I skim the room one last time to see a large open door.){/color}"
        r "Maybe that’s the exit…"
        scene black
        with fade
        r "{color=#66cc40}I close my eyes.{/color}"
        r "{color=#66cc40}Or at least I think I did. Everything is so dark, I can’t see a single thing.{/color}"
        r "{color=#66cc40}After sometime I feel my stomach go numb. After that my legs, my arms… everything.{/color}"
        r "{color=#66cc40}My eyes got heavier. Maybe…?{/color}"
        r "{color=#66cc40}Maybe I make the wrong decision..?{/color}"
        r "{color=#66cc40}No, no, no, no..that couldn’t have happened.. {/color}"
        r "{color=#66cc40}Please no, that can't...{/color}"
        r "{color=#66cc40}...{/color}"
        r "Shit!"
        r "{color=#ff0000}I don’t wanna die.{/color}"
        r "..."

        scene ranmaru death1
        with fade
        play music "audio/Horror-ginen_loop.ogg"
        r "Urgh..." #TAKEN FROM THE WIKI
        r "Dammit... This is awful..."
        r "Why did this... happen to me..."
        r ".........."
        r "Is there... someone there?"
        r "...There is, right...? Answer me..."
        r "Am I... gonna die...?"
        r ".........."
        r "Ahh, this sucks ass... Seriously...?"
        r "Sure, my life was pretty boring, and I didn't care about the future..."
        r "But now...?"
        r ".........."
        r "Ain't it strange...? It doesn't hurt at all..."
        r "When I'm bleeding this much from my gut? Why doesn't it hurt..."
        r "Doesn't feel like... I'm really dyin'..."
        r ".........."
        r "Hey..."
        r "Am I... still alive...?"
        r "Hey..."
        r ".........."
        r "..............."
        r "...................."


        jump game_over
    "No":
        r  "I-I..."
        r  "I can't bring myself to do it!"
        jump after_choice

label after_right_choice:
    hide screen gameUI

    r "Ok! Here I go!"
    stop music fadeout 1.0
    r "{color=#99ccff}(I shut my eyes as I’m chewing.){/color}"
    scene black
    with dissolve
    r "{color=#99ccff}(It just dawned on me that I’m chewing a meal that might have a razor blade to save my life.){/color}"
    r "{color=#99ccff}(...){/color}"
    r "{color=#99ccff}(The 'meal' was anything but delicious…){/color}"
    r "I… I did it?"
    play sound "audio/Accent09-1.ogg"
    scene test2
    with dissolve
    r "I did it! Yes!"
    play sound "audio/surprise.ogg"
    with flash
    r "Can I go home now?!"
    r "{color=#99ccff}(I ask that as if anyone is watching.){/color}"
    r "{color=#99ccff}(I skim the room real quick.){/color}"
    pause 0.7
    with hpunch
    with despair
    play music "audio/tense.ogg"
    r "{color=#ff0000}(There were no cameras.){/color}"
    r "{color=#ff0000}(Didn’t I just…put my life at risk?){/color}"
    r "{color=#99ccff}(I can't think straight!!){/color}"
    r "{color=#99ccff}(What's going on?!){/color}"
    r "Is my neck tightening?!"
    r "*Huff* *Huff*"
    r "{color=#99ccff}(Am I...){/color}"
    play sound "audio/ding.ogg"
    with despair
    r "{color=#99ccff}(Dying..?!){/color}"
    scene black
    with dissolve
    pause 1.0
    r "..."
    play sound "audio/correct2.ogg"
    stop music fadeout 1.0
    scene test3
    with flash
    r "{color=#99ccff}(...huh?){/color}"
    r "{color=#99ccff}(I skim the room one last time to see a large open door.){/color}"
    r "Maybe that’s the exit…"
    scene black
    with fade
    r "{color=#66cc40}I close my eyes.{/color}"
    r "{color=#66cc40}Or at least I think I did. Everything is so dark, I can’t see a single thing.{/color}"
    r "{color=#66cc40}After sometime I feel my stomach go numb. After that my legs, my arms… everything.{/color}"
    r "{color=#66cc40}My eyes got heavier. Maybe…?{/color}"
    r "{color=#66cc40}Maybe I make the wrong decision..?{/color}"
    r "{color=#66cc40}No, no, no, no..that couldn’t have happened.. {/color}"
    r "{color=#66cc40}Please no, that can't...{/color}"
    r "{color=#66cc40}...{/color}"
    r "Shit!"
    r "{color=#ff0000}I don’t wanna die.{/color}"

    return


label game_over:
    with despair
    stop music fadeout 1.0
    scene dead
    pause 1.0
    scene blackbg
    with fade

    return

label testing:

    stop music fadeout 1.0

    #blah blah with the renpy action editor


    window auto hide
    scene room1
    show screen disscussion

    #the code below makes it so that characters slowly pop up from the bottom until they reach the screen
    #this makes it look weird when they're supposed to slowly pop back up after being able to talk
    #can be easily changed, just dont force the characters off screen and make them appear
    #at a different time

    #should be good for now but change for chapter 1-2 when the main game pops up

    show anzu-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'anzu-p'
        parallel:
            xpos 0.1
            linear 0.37 xpos 0.1
            linear 0.63 xpos 0.1
            linear 1.99 xpos 0.1
        parallel:
            ypos 0.07
            linear 0.39 ypos 0.2
            linear 2.14 ypos 0.2
            linear 0.46 ypos 0.16
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 2.61 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.38 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show alice-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'alice-p' with dissolve
            2.2
            'alice-p' with dissolve
        parallel:
            xpos 0.3
            linear 0.54 xpos 0.3
            linear 0.84 xpos 0.3
            linear 1.68 xpos 0.3
        parallel:
            ypos 0.07
            linear 0.54 ypos 0.2
            linear 2.06 ypos 0.2
            linear 0.46 ypos 0.16
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 2.59 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.47 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show haya-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'haya-p' with dissolve
        parallel:
            xpos 0.5
            linear 0.57 xpos 0.5
            linear 2.7 xpos 0.5
        parallel:
            ypos 0.07
            linear 0.57 ypos 0.2
            linear 2.25 ypos 0.2
            linear 0.45 ypos 0.16
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 2.93 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.34 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show hinako-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'hinako-p' with dissolve
            0.630074739456
            'hinako-p' with dissolve
        parallel:
            xpos 0.7
            linear 0.62 xpos 0.7
            linear 2.59 xpos 0.7
        parallel:
            ypos 0.05
            linear 0.62 ypos 0.2
            linear 2.56 ypos 0.2
            linear 0.32 ypos 0.16
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 3.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.55 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show kugie-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'kugie-p' with dissolve
        parallel:
            xpos 0.9
            linear 0.85 xpos 0.9
            linear 2.81 xpos 0.9
        parallel:
            ypos 0.05
            linear 0.83 ypos 0.2
            linear 2.42 ypos 0.2
            linear 0.41 ypos 0.16
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 3.38 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.28 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show kurumada-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'kurumada-p' with dissolve
            0.702317714691
            'kurumada-p' with dissolve
            0.0928289890289
            'kurumada-p' with dissolve
        parallel:
            xpos 0.1
            linear 0.08 xpos 0.1
            linear 1.02 xpos 0.1
            linear 2.86 xpos 0.1
        parallel:
            ypos 1.34
            linear 1.23 ypos 1.0
            linear 2.36 ypos 1.0
            linear 0.37 ypos 1.06
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 3.73 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.23 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show mai-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'mai-p' with dissolve
            'mai-p' with dissolve
        parallel:
            xpos 0.3
            linear 0.02 xpos 0.31
            linear 0.03 xpos 0.3
            linear 0.945966672897 xpos 0.3
            linear 0.984033327103 xpos 0.3
            linear 2.33 xpos 0.3
        parallel:
            ypos 1.12
            linear 0.02 ypos 1.52
            linear 1.44 ypos 1.0
            linear 2.45 ypos 1.0
            linear 0.4 ypos 1.06
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 4.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show megumi-p:
        default subpixel True xpos 0.5
        parallel:
            Null(162.0, 122.0)
            'megumi-p' with dissolve
        parallel:
            ypos 1.5
            linear 1.59 ypos 1.0
            linear 2.59 ypos 1.0
            linear 0.27 ypos 1.06
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 4.22 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.23 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show ranmaru-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'ranmaru-p' with dissolve
            0.630074739456
            'ranmaru-p' with dissolve
        parallel:
            xpos 0.7
            linear 0.62 xpos 0.7
            linear 2.59 xpos 0.7
        parallel:
            ypos 1.47 # FIX LATER!!!
            linear 1.62 ypos 1.0
            linear 2.56 ypos 1.0
            linear 0.32 ypos 1.06 # RANMARU'S PORTRAIT WAS ALWAYS A BIT FUCKY
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 3.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.55 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show shin-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'shin-p' with dissolve
            'shin-p' with dissolve
        parallel:
            xpos 0.89
            linear 2.15 xpos 0.9
        parallel:
            ypos 1.47 # FIX LATER!!!
            linear 1.62 ypos 1.0
            linear 2.56 ypos 1.0
            linear 0.32 ypos 1.06
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 4.52 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 0.3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    with Pause(4.94)

    show anzu-p:
        pos (0.1, 0.16) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show alice-p:
        pos (0.3, 0.16) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show haya-p:
        pos (0.5, 0.16) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show hinako-p:
        pos (0.7, 0.16) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show kugie-p:
        pos (0.9, 0.16) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show kurumada-p:
        pos (0.1, 1.06) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show mai-p:
        pos (0.3, 1.06) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show megumi-p:
        pos (0.5, 1.06) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show ranmaru-p:
        pos (0.7, 1.06) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show shin-p:
        pos (0.9, 1.06) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

#    imagebutton:
    play sound "audio/poka01.ogg"
    show megumi-p:
        default subpixel True xpos 0.5
        parallel:
            Null(162.0, 122.0)
            'megumi-p'
        parallel:
            ypos 1.5
            linear 0.2 ypos 1.0
            linear 0.2 ypos 1.0
#            linear 0.27 ypos 1.06
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
#            linear 4.22 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
#            linear 0.23 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    play sound "audio/poka01.ogg"
    show ranmaru-p:
        default subpixel True xpos 0.7
        parallel:
            Null(162.0, 122.0)
            'ranmaru-p'
        parallel:
            xpos 0.7
            linear 2.15 xpos 0.7
        parallel:
            ypos 1.5
            linear 0.2 ypos 1.0
            linear 0.2 ypos 1.0
#            linear 0.27 ypos 1.06
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    play sound "audio/poka01.ogg"
    show anzu-p:
        default subpixel True
        parallel:
            Null(162.0, 122.0)
            'anzu-p'
        parallel:
            xpos 0.1
            linear 0.37 xpos 0.1
            linear 0.63 xpos 0.1
            linear 1.99 xpos 0.1
        parallel:
            ypos 0.07
            linear 0.39 ypos 0.2
            linear 2.14 ypos 0.2
#            linear 0.46 ypos 0.16
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
#            linear 2.61 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
#            linear 0.38 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

    play music "audio/bgm/sin0.ogg"
    show megumi-1
    me "Ready to interogate some people?"
    r "Well I wouldn't call it that."
    r "Here we go..."
    show screen characters
    hide megumi-1
    label repeat:
    "{color=#66cc40} Select Extract to get information from people. {/color}"
    show screen disscussion
    jump repeat


label Anzu_Pressed:

    a "Introductions? I'm pretty good at that!"
    menu:
        "Choose this topic":
            jump anzu_pressed2
        "Cancel":
            jump repeat

label anzu_pressed2:
    show anzu-6
    a "Hi! My name’s Anzu Kinashi!"
    hide anzu-6
    show anzu-2
    a "I’m a highschooler that has a job on the side."
    hide anzu-2
    show anzu-12
    a "On my way home I saw this couple being followed by some sweaty guy!"
    hide anzu-12
    show ranmaru-13
    r "Was it the kidnapper?!"
    hide ranmaru-13
    show anzu-12
    a "Don’t know. But I can definitely say they had something to do with all of this!"
    hide anzu-12
    show megumi-3
    me "A suspect, huh? What did they look like?"
    hide megumi-3
    show anzu-2
    a "Well it was night time so I didn’t get a lot of their details but I can tell they wore dark clothing and had dark hair."
    hide anzu-2
    show megumi-6
    me "Maybe some more specific details?"
    hide megumi-6
    show anzu-5
    a "They were pretty slender and it looked like they were really distressed. I heard them screaming something, can't quite remember it though."
    hide anzu-5
    show megumi-2
    me "Was there anything special about the couple?"
    hide megumi-2
    show anzu-5
    a "Nothing out of the ordinary."
    hide anzu-5
    show anzu-4
    a "I did recognize the girl from my classes, her boyfriend is pretty loud so I just stay away from them."
    hide anzu-4
    show ranmaru-36
    r "I see…"
    hide ranmaru-36
    with dissolve
    r "{color=#99ccff}(Hang on a second…) {/color}"
    r "{color=#99ccff}(Is she talking about…){/color}"

#    show screen gameUI MAKE A NEW ONE FOR DISUCSSIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!

    hide screen disscussion
#    window auto show

    play sound "audio/poka01.ogg"
    show kugie-p:
        default subpixel True xpos 0.9
        parallel:
            Null(162.0, 122.0)
            'kugie-p'
        parallel:
            xpos 0.9
            linear 2.81 xpos 0.9
        parallel:
            ypos 0.07
            linear 0.39 ypos 0.2
            linear 2.14 ypos 0.2
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

    jump repeat



label Kugie_Pressed:

    show kugie-2
    ku "..."
    hide kugie-2
    show ranmaru-1
    r "..."
    hide ranmaru-1
    show kugie-5
    ku "The names Kugie Kizuchi. I’m a highschooler."
    hide kugie-5
    show kugie-7
    ku "I was walking home with my little sister until some men in black suits came out of a car and kidnapped us."
    hide kugie-7
    show kugie-8
    ku "You said you were a police officer, right Miss Sasahara?"
    hide kugie-8
    show megumi-3
    me "Correct."
    hide megumi-3
    show kugie-5
    ku "How often do you take murder cases?"
    r "M-Muder case?!"
    r "{color=#99ccff}(I wonder…){/color}"
    r "{color=#99ccff}(Is it possible that…){/color}"
    hide kugie-5
    show megumi-6
    me "Quite often, I'm the chief of my police station so it's pretty common..."
    hide megumi-6
    show kugie-2
    ku "Is it ok if we talk a bit more?"
    ku "I have certain businesses to bring up with you."
    hide kugie-2
    show megumi-1
    me "Of course."
    hide megumi-1
    show megumi-2
    me "Ranmaru could you give us some privacy?"
    r "Huh? Oh, yeah that’s fine."


    jump repeat

label Haya_Pressed:

    show haya-4
    ha "M-My name is Shunsuke Hayasaka… I work for a generic intelligence company… "
    r "Intelligence company?"
    hide haya-4
    show haya-6
    ha "Y-Yeah.. We take consumer feedback and provide extra options to said consumers to create a positive internet experience!"
    r "…"
    hide haya-6
    show megumi-6
    me "Simply put it, he collects your data."
    hide megumi-6
    r "Ohhh… "
    r "Wait!"
    r "Not cool dude!"
    show haya-12
    ha "Eek! Don’t yell, I'm just doing my job!"
    r "You joined it! It’s your own fault!"
    hide haya-12
    show haya-13
    ha "I didn’t have a choice!"
    hide haya-13
    r "!"
    show megumi-3
    me "What do you mean by that?"
    hide megumi-3
    show haya-7
    ha "Aah!"
    ha "..."
    ha "W-Well you see…"
    hide haya-7
    show haya-8
    play sound "audio/feed1.ogg" #sound comes first then transition
    with flash
    ha "It’s a family business, I was forced into it…"
    hide haya-8
    show megumi-8
    me "Makes sense."
    r "…"
    r "{color=#99ccff}(Just saying it makes sense doesn’t do anything…){/color}"
    hide megumi-8
    show haya-2
    ha "Glad we could reach an understanding…"
    hide haya-2
    show haya-1
    r "What about your memories?"
    hide haya-1
    show haya-3
    ha "O-Oh.. I was just.. At my house and I woke up here.. "
    hide haya-3
    show haya-6
    ha "Nothing special ahaha…"
    r "Definitely suspicious."
    hide haya-6
    with dissolve


    jump repeat


label Megumi_Pressed:
    show megumi-1
    me "Maybe you should go talk to someone else first!"
    hide megumi-1
    show megumi-2
    me "You can always meet some amazing people out there."
    hide megumi-2
    with dissolve
    jump repeat

label Ranmaru_Pressed:

    show ranmaru-10
    r "What the hell am I even doing here...?"
    hide ranmaru-10
    with dissolve
    jump repeat

label BLAHBLAHBLAH:

    play sound "audio/discussion/portrait flashes.ogg"

    r ""



#    jump wow
