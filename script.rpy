# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# yo yo yo! this is how you make a note in rpy

# define e = Character("Eileen")
# define sh = Character("Shoddy")


#tutorials and shit
# THIS IS IMPORTANT ->>>>> https://www.renpy.org/doc/html/text.html
# "An example of {b}bold test{/b}."
# "{color=#f00}Red{/color}" * #ff784c for important text, #99ccff for thinking text, #66cc40 for narrator text
# {size=-10}Smaller{/size}
# with hpunch makes the screenshake left and right, with vpunch makes the screenshake up and down

#bad guys LMAO
define b = Character("Botsun")
define who1 = Character("??? (A)")
define who2 = Character("??? (B)")
define who3 = Character("??? (C)")

#alt names
define who = Character("???")

define s = Character("Strange Woman")
define k2 = Character("Blue-haired Man")
define h2 = Character("Pink-haired Girl")
define m2 = Character("Woman with big hat")
define a2 = Character("Hooded Girl")
define ha2 = Character("Man with glasses") #bryan
define me2 = Character("Woman in uniform")
define ku2 = Character("Girl in uniform")
define sh2 = Character("Beanie Man")

#main characters
define r = Character("Ranmaru")
define k = Character("Kurumada")
define h = Character("Hinako")
define m = Character("Mai")
define a = Character("Anzu")
define ha = Character("Hayasaka")
define ku = Character("Kugie")
define sh = Character("Shin")
define me = Character("Megumi")

define config.debug_text_overflow = False

init:
#    image bg road = "test.png"

    $ flash = Fade(.15, 0, .15, color="#fff")

init:

    $ despair = Fade(.1, 0, .1, color="#ff0000")

label start:

    stop music fadeout 1.0

#    play music "audio/seme-KS-ZN.ogg"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

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
    with flash

    "…Beginning voiced guidance. "

    who1 "The First Trial will now begin."

    r "{color=#66cc40}First Trial?{/color}"
    with flash

    who1 "In front of you will is a plate of food. One course is completely normal and delicious while the other is…"

    who1 "Well it’s still quite delicious, it just has a razor blade in it."

    r "{color=#99ccff}(!?){/color}"

    with hpunch
    who2 "Bastard! Stick to the script!"

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

    with hpunch
    play sound "audio/surprise.ogg"
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

    with despair
    r "{color=#99ccff}(I have..risk my life here…){/color}"

    hide ranmaru-23 with dissolve

label test2:
    show screen gameUI
    window hide dissolve
    r "{color=#99ccff}I gotta look around!{/color}"
    jump test2

label door_pressed:
    r "{color=#99ccff}(Agh! I can't open the stupid door!){/color}"
    jump after_choice

label meal_pressed:
    r "Alright! Here goes nothing!"
    r "{color=#99ccff}(I hesitate a bit before I eat the egg itself.){/color}"
    r "{color=#99ccff}(Is it really this egg I want to eat?){/color} "

label after_choice:
    with hpunch
    r "God damnit!"
    jump test2

label after_right_choice:


    # This ends the game.

    return
