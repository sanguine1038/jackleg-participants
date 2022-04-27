
#screen bleh:



screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -432
        yoffset 530
        auto "UI/move_%s.png"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -624
        yoffset 530
        auto "UI/data_%s.png"
        action ShowMenu ("save")

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.

# higher X goes to the right
# higher Y goes down
label call_mapUI:
    call screen MapUI


label characters:
    call screen characters

screen MapUI:

    add "test2.png"

    imagebutton:
        xpos 318
        ypos 100
        idle "test2 selectables/door_idle.png"
        hover "test2 selectables/door_hover.png"
        action Jump("door_pressed")

    imagebutton:
        xpos 318
        ypos 300
        idle "test2 selectables/door_idle.png"
        hover "test2 selectables/door_hover.png"
        action Jump("meal_pressed")

screen disscussion:

    imagebutton:
        xpos 0
        ypos 200
        idle "disscussion/disscussion_save.png"
        hover "disscussion/disscussion_save_hover.png"
        action ShowMenu ("save")

    #gotta make it so you NEED to press this before talking to a character
    imagebutton:
        xpos 714
        ypos 200
        idle "disscussion/disscussion_extract.png"
        hover "disscussion/disscussion_extract_hover.png"
        action Jump ("characters")

screen characters:
    imagebutton:
        #only really used for the intros. in theory when the main game starts
        #itll probably use the same variables so i'm probably going to have to make
        #a new one of these for each discussion
        xpos 0
        ypos 2
        idle "portraits/empty.png"
        hover "portraits/empty.png"
        action Jump("Anzu_Pressed")

#    imagebutton: alice
#        xpos 163 #everyone is 163 thingeys away
#        ypos 2
#        idle "portraits/empty.png"
#        hover "portraits/empty.png"
#        action Jump("another")

#if persistent.whatever:
    imagebutton:
        xpos 327
        ypos 2
        idle "portraits/haya-p.png"
        hover "portraits/haya-p.png"
        action Jump("Haya_Pressed")

#    imagebutton:hinako
#        xpos 489
#        ypos 2
#        idle "portraits/empty.png"
#        hover "portraits/empty.png"
#        action Jump("another")

    imagebutton:
        xpos 653
        ypos 2
        idle "portraits/empty.png"
        hover "portraits/empty.png"
#        action If( repflirt, Show("Kugie_Pressed") )
        action Jump("Kugie_Pressed")

#    imagebutton: kurumada
#        xpos 0
#        ypos 502
#        idle "portraits/empty.png"
#        hover "portraits/empty.png"
#        action Jump("another")

    imagebutton:
        xpos 163
        ypos 502
        idle "portraits/mai-p.png"
        hover "portraits/mai-p.png"
        action Jump("another")

    imagebutton:
        xpos 327
        ypos 502
        idle "portraits/megumi-p.png"
        hover "portraits/megumi-p.png"
        action Jump("Megumi_Pressed")

    imagebutton:
        xpos 490
        ypos 502
        idle "portraits/ranmaru-p.png"
        hover "portraits/ranmaru-p.png"
        action Jump("Ranmaru_Pressed")

#    imagebutton: shin
#        xpos 652
#        ypos 502
#        idle "portraits/empty.png"
#        hover "portraits/empty.png"
#        action Jump("another")
