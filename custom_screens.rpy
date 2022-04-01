
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/move_%s.png"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.

# higher X goes to the right
# higher Y goes down
label call_mapUI:
    call screen MapUI

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
        idle "test2 selectables/test.png"
        hover "test2 selectables/test.png"
        action Jump("meal_pressed")
