
screen _new_action_editor(opened=None, time=0, previous_time=None, in_graphic_mode=[]):
    default layer = "master"
    $int_format = "{:> }" 
    $float_format = "{:> .2f}"

    $generate_changed = _viewers.generate_changed
    $get_property = _viewers.get_property
    $get_value = _viewers.get_value
    $current_scene = _viewers.current_scene
    $scene_keyframes = _viewers.scene_keyframes
    $sound_keyframes = _viewers.sound_keyframes
    $all_keyframes = _viewers.all_keyframes
    $change_time = _viewers.change_time
    $get_sorted_keyframes = _viewers.get_sorted_keyframes
    $current_time = _viewers.current_time
    $edit_value = _viewers.edit_value
    $reset = _viewers.reset
    $force_plus = _viewers.force_plus
    $force_float = _viewers.force_float
    $force_wide_range = _viewers.force_wide_range
    $props_sets = _viewers.props_sets
    $props_groups = _viewers.props_groups
    $keyframes_exist = _viewers.keyframes_exist
    $generate_sound_menu = _viewers.generate_sound_menu
    $generate_menu = _viewers.generate_menu
    $is_wide_range = _viewers.is_wide_range
    $TimeLine = _viewers.TimeLine

    if opened is None:
        $opened = {}
    for s in range(0, len(scene_keyframes)):
        if s not in opened:
            $opened[s] = []

    $indent = "  "

    $offsetX, offsetY = get_property("offsetX"), get_property("offsetY")
    $value_range = persistent._wide_range
    $move_amount1 = 100
    $move_amount2 = 300
    key "hide_windows" action NullAction()
    if get_value("perspective", scene_keyframes[current_scene][1], True):
        if _viewers.fps_keymap:
            key "s" action Function(generate_changed("offsetY"), offsetY + move_amount1 + value_range)
            key "w" action Function(generate_changed("offsetY"), offsetY - move_amount1 + value_range)
            key "a" action Function(generate_changed("offsetX"), offsetX - move_amount1 + value_range)
            key "d" action Function(generate_changed("offsetX"), offsetX + move_amount1 + value_range)
            key "S" action Function(generate_changed("offsetY"), offsetY + move_amount2 + value_range)
            key "W" action Function(generate_changed("offsetY"), offsetY - move_amount2 + value_range)
            key "A" action Function(generate_changed("offsetX"), offsetX - move_amount2 + value_range)
            key "D" action Function(generate_changed("offsetX"), offsetX + move_amount2 + value_range)
        else:
            key "j" action Function(generate_changed("offsetY"), offsetY + move_amount1 + value_range)
            key "k" action Function(generate_changed("offsetY"), offsetY - move_amount1 + value_range)
            key "h" action Function(generate_changed("offsetX"), offsetX - move_amount1 + value_range)
            key "l" action Function(generate_changed("offsetX"), offsetX + move_amount1 + value_range)
            key "J" action Function(generate_changed("offsetY"), offsetY + move_amount2 + value_range)
            key "K" action Function(generate_changed("offsetY"), offsetY - move_amount2 + value_range)
            key "H" action Function(generate_changed("offsetX"), offsetX - move_amount2 + value_range)
            key "L" action Function(generate_changed("offsetX"), offsetX + move_amount2 + value_range)
        key "rollback"    action Function(generate_changed("offsetZ"), get_property("offsetZ")+100+persistent._wide_range)
        key "rollforward" action Function(generate_changed("offsetZ"), get_property("offsetZ")-100+persistent._wide_range)

    if time:
        timer time+_viewers.return_margin action [Show("_new_action_editor", opened=opened, in_graphic_mode=in_graphic_mode), \
                            Function(_viewers.return_start_time, previous_time)]
        key "game_menu" action [Show("_new_action_editor", opened=opened, in_graphic_mode=in_graphic_mode), \
                            Function(change_time, previous_time)]
        $play_action = [SensitiveIf(get_sorted_keyframes(current_scene) or len(scene_keyframes) > 1), SelectedIf(time > 0), \
            _viewers.pause, \
            Show("_new_action_editor", opened=opened, time=_viewers.get_animation_delay(), in_graphic_mode=in_graphic_mode)]
    else:
        key "game_menu" action Confirm("Close Editor?", Return())
        $play_action = [SensitiveIf(get_sorted_keyframes(current_scene) or len(scene_keyframes) > 1), SelectedIf(time > 0), \
            [If(get_sorted_keyframes(current_scene) or len(scene_keyframes) > 1, Function(_viewers.play, play=True))], \
            Show("_new_action_editor", opened=opened, time=_viewers.get_animation_delay(), previous_time=current_time, in_graphic_mode=in_graphic_mode)]

        if persistent._show_camera_icon:
            if _viewers.aspect_16_9():
                $xpos = int(config.screen_width * (1 - _viewers.preview_size) / 2)
                $ypos = 0
            else:
                $xpos = 0
                $ypos = 0
            add _viewers.ImagePins() xpos xpos ypos ypos
    key "K_SPACE" action play_action
    key "action_editor" action NullAction()

    $state=_viewers.get_image_state(layer)
    $tag_list =  []
    for tag, z in _viewers.zorder_list[current_scene][layer]:
        if tag in state:
            $tag_list.append(tag)

    add _viewers.screen_background

    frame:
        style_group "new_action_editor"
        align (1., 0.)
        vbox:
            xfill False
            text "absolute" xalign 1.
            add DynamicDisplayable(_viewers.absolute_pos) xalign 1.
            text "fraction" xalign 1.
            add DynamicDisplayable(_viewers.rel_pos) xalign 1.

    frame:
        pos (1., _viewers.preview_size)
        align (1., 1.)
        style_group "new_action_editor"
        vbox:
            style_group "new_action_editor_a"
            textbutton _("option") action Show("_action_editor_option")
            textbutton _("show image pins") action ToggleField(persistent, "_show_camera_icon")
            textbutton _("scene editor") action [SensitiveIf(len(scene_keyframes) > 1), Show("_scene_editor")]
            hbox:
                xalign 1.
                textbutton _("remove keys") action [
                    SensitiveIf(current_time in get_sorted_keyframes(current_scene)), 
                    Function(_viewers.remove_all_keyframe, current_time), renpy.restart_interaction]
                textbutton _("move keys") action [
                    SensitiveIf(current_time in get_sorted_keyframes(current_scene)),
                    SelectedIf(False), SetField(_viewers, "moved_time", current_time), Show("_move_keyframes")]
            hbox:
                xalign 1.
                textbutton _("<") action Function(_viewers.prev_time)
                textbutton _(">") action Function(_viewers.next_time)
                textbutton _("play") action play_action
                textbutton _("clipboard") action Function(_viewers.put_clipboard)
                textbutton _("close") action Return()
    frame:
        style_group "new_action_editor"
        ymaximum 1 - _viewers.preview_size
        yalign 1.0
        padding (0, 0, 0, 0)
        vbox:
            hbox:
                ymaximum _viewers.time_column_height
                hbox:
                    style_group "new_action_editor_c"
                    imagebutton:
                        idle DynamicDisplayable(_viewers.show_current_time)
                        hover DynamicDisplayable(_viewers.show_current_time)
                        action Function(_viewers.edit_time)
                        xalign 1.
                        size_group None
                bar value _viewers.CurrentTime(persistent._time_range):
                    xalign 1. yalign .5 style "new_action_editor_bar"
            if in_graphic_mode:
                $key = in_graphic_mode[0]
                if isinstance(key, tuple):
                    $p = key[2]
                    $d = _viewers.get_default(p)
                    $tag=(key[0], key[1])
                else:
                    $p = key
                    $d = _viewers.get_default(p, True)
                    $tag = "camera"
                $value = get_property(key)
                $f = generate_changed(key)
                $use_wide_range = is_wide_range(key)
                if not use_wide_range or isinstance(value, float):
                    $value_format = float_format
                else:
                    $value_format = int_format
                hbox:
                    #他と同時にグラフィックモードで表示するとタイムバーが反応しないことがある
                    hbox:
                        style_group "new_action_editor_c"
                        textbutton "  [key]" action None text_color "#CCC"
                        add _viewers.DraggableValue(value_format, key, f, use_wide_range, p in force_plus,
                            text_size=16, text_color="#CCC", text_hover_underline=True)
                    fixed:
                        # ysize int(config.screen_height*(1-_viewers.preview_size)-_viewers.time_column_height)
                        ysize None
                        add TimeLine(current_scene, tag, key=key, changed=f, use_wide_range=use_wide_range, opened=opened, in_graphic_mode=in_graphic_mode)
            else:
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    has vbox
                    for s, ks in enumerate(all_keyframes):
                        if s != current_scene:
                            hbox:
                                hbox:
                                    style_group "new_action_editor_c"
                                    textbutton "+ "+"scene[s]":
                                        action [SelectedIf(current_scene == s), Function(_viewers.change_scene, s)]
                                fixed:
                                    add TimeLine(s, None)
                        else:
                            hbox:
                                hbox:
                                    style_group "new_action_editor_c"
                                    textbutton "- "+"scene[s]" action SelectedIf(current_scene == s)
                                fixed:
                                    add TimeLine(s, None)
                            if "camera" not in opened[s]:
                                hbox:
                                    hbox:
                                        style_group "new_action_editor_c"
                                        if persistent._open_only_one_page:
                                            $new_opened = {s:["camera"]}
                                        else:
                                            $new_opened = opened.copy()
                                            $new_opened[s] = new_opened[s] + ["camera"]
                                        textbutton _(indent+"+ "+"camera"):
                                            action [SensitiveIf(get_value("perspective", scene_keyframes[s][1], True) != False),
                                            Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)]
                                    fixed:
                                        add TimeLine(s, "camera")
                            else:
                                hbox:
                                    hbox:
                                        style_group "new_action_editor_c"
                                        $new_opened = opened.copy()
                                        $new_opened[s] = opened[s].copy()
                                        $new_opened[s].remove("camera")
                                        textbutton _(indent+"- "+"camera"):
                                            action Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)
                                        textbutton _("clipboard"):
                                            action Function(_viewers.put_camera_clipboard)
                                            size_group None
                                            style_group "new_action_editor_b"
                                    fixed:
                                        add TimeLine(s, "camera")
                                for props_set_name, props_set in props_sets:
                                    if props_set_name in opened[s]:
                                        hbox:
                                            hbox:
                                                style_group "new_action_editor_c"
                                                $new_opened = opened.copy()
                                                $new_opened[s] = opened[s].copy()
                                                $new_opened[s].remove(props_set_name)
                                                textbutton indent*2+"- " + props_set_name action Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)
                                            fixed:
                                                add TimeLine(s, "camera", props_set=props_set)
                                        for p in props_set:
                                            if (p, _viewers.get_default(p, True)) in _viewers.camera_props and p != "child" and (p not in props_groups["focusing"] or \
                                                (persistent._viewer_focusing and get_value("perspective", scene_keyframes[s][1], True))):
                                                $key = p
                                                $value = get_property(p)
                                                $d = _viewers.get_default(p, True)
                                                $f = generate_changed(p)
                                                $use_wide_range = is_wide_range(key)
                                                if not use_wide_range or isinstance(value, float):
                                                    $value_format = float_format
                                                else:
                                                    $value_format = int_format
                                                hbox:
                                                    if p == "perspective":
                                                        hbox:
                                                            style_group "new_action_editor_c"
                                                            textbutton indent*3+"  [p]":
                                                                action None text_color "#CCC"
                                                            textbutton "[value]":
                                                                action [SelectedIf(get_value(key, scene_keyframes[s][1], True)),
                                                                Function(_viewers.toggle_perspective)]
                                                                size_group None
                                                    elif p in _viewers.any_props:
                                                        hbox:
                                                            style_group "new_action_editor_c"
                                                            textbutton indent*3+"  [p]":
                                                                action None text_color "#CCC"
                                                            if isinstance(value, str):
                                                                textbutton "'[value]'":
                                                                    action [SelectedIf(get_value(key, scene_keyframes[s][1], True)),
                                                                    Function(_viewers.edit_any, key)]
                                                                    size_group None
                                                            else:
                                                                textbutton "[value]":
                                                                    action [SelectedIf(get_value(key, scene_keyframes[s][1], True)),
                                                                    Function(_viewers.edit_any, key)]
                                                                    size_group None
                                                    elif p in _viewers.boolean_props:
                                                        hbox:
                                                            style_group "new_action_editor_c"
                                                            textbutton indent*3+"  [p]":
                                                                action None text_color "#CCC"
                                                            textbutton "[value]":
                                                                action [SelectedIf(get_value(key, scene_keyframes[s][1], True)),
                                                                Function(_viewers.toggle_boolean_property, key)]
                                                                size_group None
                                                    else:
                                                        hbox:
                                                            style_group "new_action_editor_c"
                                                            textbutton indent*3+"  [p]" action None text_color "#CCC"
                                                            add _viewers.DraggableValue(value_format, key, f, use_wide_range, p in force_plus,
                                                                text_size=16, text_color="#CCC", text_hover_underline=True)
                                                    # if key not in in_graphic_mode:
                                                    fixed:
                                                        add TimeLine(s, "camera", key=key, changed=f, use_wide_range=use_wide_range, opened=opened)
                                                    # else:
                                                    #     fixed:
                                                    #         ysize int(config.screen_height*(1-_viewers.preview_size)-_viewers.time_column_height)
                                                    #         add TimeLine(s, "camera", key=key, changed=f, use_wide_range=use_wide_range, opened=opened, in_graphic_mode=in_graphic_mode)
                                    else:
                                        hbox:
                                            hbox:
                                                style_group "new_action_editor_c"
                                                if persistent._open_only_one_page:
                                                    $new_opened = {s:["camera", props_set_name]}
                                                else:
                                                    $new_opened = opened.copy()
                                                    $new_opened[s] = new_opened[s] + [props_set_name]
                                                textbutton indent*2+"+ "+props_set_name action Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)
                                            fixed:
                                                add TimeLine(s, "camera", props_set=props_set)
                            for tag in tag_list:
                                if tag not in opened[s]:
                                    hbox:
                                        hbox:
                                            style_group "new_action_editor_c"
                                            if persistent._open_only_one_page:
                                                $new_opened = {s:[tag]}
                                            else:
                                                $new_opened = opened.copy()
                                                $new_opened[s] = new_opened[s] + [tag]
                                            textbutton indent+"+ "+"{}".format(tag):
                                                action Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)
                                        fixed:
                                            add TimeLine(s, (tag, layer))
                                else:
                                    hbox:
                                        hbox:
                                            style_group "new_action_editor_c"
                                            $new_opened = opened.copy()
                                            $new_opened[s] = opened[s].copy()
                                            $new_opened[s].remove(tag)
                                            textbutton indent+"- "+"{}".format(tag):
                                                action Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)
                                            textbutton _("clipboard"):
                                                action Function(_viewers.put_image_clipboard, tag, layer)
                                                style_group "new_action_editor_b"
                                                size_group None
                                        fixed:
                                            add TimeLine(s, (tag, layer))
                                    for props_set_name, props_set in props_sets:
                                        if (tag, layer, props_set_name) not in opened[s]:
                                            hbox:
                                                hbox:
                                                    style_group "new_action_editor_c"
                                                    if persistent._open_only_one_page:
                                                        $new_opened = {s:[tag, (tag, layer, props_set_name)]}
                                                    else:
                                                        $new_opened = opened.copy()
                                                        $new_opened[s] = new_opened[s] + [(tag, layer, props_set_name)]
                                                    textbutton indent*2+"+ "+props_set_name:
                                                        action Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)
                                                fixed:
                                                    add TimeLine(s, (tag, layer), props_set=props_set)
                                        else:
                                            hbox:
                                                hbox:
                                                    style_group "new_action_editor_c"
                                                    $new_opened = opened.copy()
                                                    $new_opened[s] = opened[s].copy()
                                                    $new_opened[s].remove((tag, layer, props_set_name))
                                                    textbutton indent*2+"- " + props_set_name:
                                                        action Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)
                                                fixed:
                                                    add TimeLine(s, (tag, layer), props_set=props_set)
                                            for p in props_set:
                                                if (p, _viewers.get_default(p)) in _viewers.transform_props and (p not in props_groups["focusing"] and (((persistent._viewer_focusing
                                                    and get_value("perspective", scene_keyframes[s][1], True)) and p != "blur")
                                                    or (not persistent._viewer_focusing or not get_value("perspective", scene_keyframes[s][1], True)))):
                                                    $key = (tag, layer, p)
                                                    $d = _viewers.get_default(p)
                                                    $value = get_property(key)
                                                    $f = generate_changed(key)
                                                    $use_wide_range = p not in force_float and (p in force_wide_range or ((value is None and isinstance(d, int)) or isinstance(value, int)))
                                                    if not use_wide_range or isinstance(value, float):
                                                        $value_format = float_format
                                                    else:
                                                        $value_format = int_format
                                                    hbox:
                                                        if p == "child":
                                                            vbox:
                                                                xfill False
                                                                hbox:
                                                                    style_group "new_action_editor_c"
                                                                    textbutton indent*3+"  [value[0]]":
                                                                        action [SelectedIf(keyframes_exist((tag, layer, "child"))),
                                                                        Function(_viewers.change_child, tag, layer, default=value[0])]
                                                                        size_group None
                                                                hbox:
                                                                    style_group "new_action_editor_c"
                                                                    textbutton indent*3+"  with [value[1]]":
                                                                        action [
                                                                        SelectedIf(keyframes_exist((tag, layer, "child"))),
                                                                        Function(_viewers.edit_transition, tag, layer)]
                                                                        size_group None
                                                        elif p in _viewers.any_props:
                                                            hbox:
                                                                style_group "new_action_editor_c"
                                                                textbutton indent*3+"  [p]":
                                                                    action None text_color "#CCC"
                                                                if isinstance(value, str):
                                                                    textbutton "'[value]'":
                                                                        action [SelectedIf(get_value(key, scene_keyframes[s][1], True)),
                                                                        Function(_viewers.edit_any, key)]
                                                                        size_group None
                                                                else:
                                                                    textbutton "[value]":
                                                                        action [SelectedIf(get_value(key, scene_keyframes[s][1], True)),
                                                                        Function(_viewers.edit_any, key)]
                                                                        size_group None
                                                        elif p in _viewers.boolean_props:
                                                            hbox:
                                                                style_group "new_action_editor_c"
                                                                textbutton indent*3+"  [p]":
                                                                    action None text_color "#CCC"
                                                                textbutton "[value]":
                                                                    action [SelectedIf(get_value(key, scene_keyframes[s][1], True)),
                                                                    Function(_viewers.toggle_boolean_property, key)]
                                                                    size_group None
                                                        else:
                                                            hbox:
                                                                style_group "new_action_editor_c"
                                                                textbutton indent*3+"  [p]":
                                                                    action None text_color "#CCC"
                                                                add _viewers.DraggableValue(value_format, key, f, use_wide_range, p in force_plus,
                                                                    text_size=16, text_color="#CCC", text_hover_underline=True)
                                                        fixed:
                                                            # if key not in in_graphic_mode:
                                                            add TimeLine(s, (tag, layer), key=key, changed=f, use_wide_range=use_wide_range, opened=opened)
                                                            # else:
                                                                # ysize int(config.screen_height*(1-_viewers.preview_size)-_viewers.time_column_height)
                                                                # add TimeLine(s, (tag, layer), key=key, changed=f, use_wide_range=use_wide_range, opened=opened, in_graphic_mode=in_graphic_mode)
                                    $new_opened = opened.copy()
                                    $new_opened[s] = opened[s].copy()
                                    $new_opened[s] = [o for o in opened if (not isinstance(o, tuple) or o[0] != tag) and o !=tag]
                                    textbutton _(indent*3+"  remove"):
                                        action [SensitiveIf(tag in _viewers.image_state[s][layer]),
                                            Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode),
                                            Function(_viewers.remove_image, layer, tag)]
                                        size_group None
                            textbutton _(indent+"+(add image)"):
                                action Function(_viewers.add_image, layer)
                                style_group "new_action_editor_c"
                    textbutton _("+(add scene)"):
                        action _viewers.add_scene
                        style_group "new_action_editor_c"
                    if "sounds" not in opened:
                        hbox:
                            hbox:
                                style_group "new_action_editor_c"
                                if persistent._open_only_one_page:
                                    $new_opened = {"sounds":True}
                                else:
                                    $new_opened = opened.copy()
                                    $new_opened["sounds"] = True
                                textbutton _("+ "+"sounds"):
                                    action [SensitiveIf(persistent._viewer_channel_list),
                                    Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)]
                            fixed:
                                add TimeLine(s, "sounds")
                    else:
                        hbox:
                            style_group "new_action_editor_c"
                            $new_opened = opened.copy()
                            $del new_opened["sounds"]
                            textbutton _(indent+"- "+"sounds"):
                                action Show("_new_action_editor", opened=new_opened, in_graphic_mode=in_graphic_mode)
                            textbutton _("clipboard"):
                                action Function(_viewers.put_sound_clipboard)
                                size_group None
                                style_group "new_action_editor_b"
                        for channel in sound_keyframes:
                            hbox:
                                hbox:
                                    style_group "new_action_editor_c"
                                    textbutton indent*1+"  [channel]":
                                        action None text_color "#CCC"
                                        size_group None
                                fixed:
                                    add TimeLine(s, "sounds", key=channel)
                            hbox:
                                $value = "None"
                                $sorted_play_times = sorted(sound_keyframes[channel].keys())
                                for t in sorted_play_times:
                                    if current_time >= t:
                                        $value = sound_keyframes[channel][t]
                                textbutton indent*2+"  [value]":
                                    action [SelectedIf(keyframes_exist(channel, is_sound=True)),
                                        Function(_viewers.edit_playing_file, channel, current_time)]
                                    size_group None


init -1599 python in _viewers:
    return_margin = 0.5
    time_column_height = 30
    key_xsize = 22
    key_ysize = 22
    key_half_xsize = 22 // 2
    key_half_ysize = 22 // 2
    time_line_background_color = "#222"

    key_child = Transform(rotate=45)(Solid("#77A", xsize=16, ysize=16))
    key_hovere_child = Transform(rotate=45)(Solid("#AAD", xsize=16, ysize=16))
    warperkey_child = Transform(rotate=45)(Solid("#07A", xsize=16, ysize=16))
    warperkey_hovere_child = Transform(rotate=45)(Solid("#4AD", xsize=16, ysize=16))
    knot_child = Transform(rotate=45)(Solid("#04A", xsize=16, ysize=16))
    knot_hovere_child = Transform(rotate=45)(Solid("#48D", xsize=16, ysize=16))
    insensitive_key_child = Transform(rotate=45)(Solid("#447", xsize=16, ysize=16))
    insensitive_key_hovere_child = Transform(rotate=45)(Solid("#669", xsize=16, ysize=16))
    interpolate_key_child = Solid("#BBB", xsize=4, ysize=4) #, xoffset=key_half_xsize-2, yoffset=key_half_ysize-2)

    c_box_size = 320
    timeline_ysize = 27

init python in _viewers:
    box = Fixed()
    if aspect_16_9():
        box.add(Solid(preview_background_color, xsize=config.screen_width, ysize=(1-preview_size), ypos=preview_size))
        box.add(Solid(preview_background_color, xsize=(1-preview_size)/2, ysize=preview_size, xpos=0.))
        box.add(Solid(preview_background_color, xsize=(1-preview_size)/2, ysize=preview_size, xalign=1.))
    else:
        box.add(Solid(preview_background_color, xsize=config.screen_width, ysize=(1-preview_size), ypos=preview_size))
        box.add(Solid(preview_background_color, xsize=(1-preview_size), ysize=preview_size, xalign=1.))
    screen_background = box


init -1597:
    style new_action_editor_frame:
        background None
    style new_action_editor_button:
        size_group "action_editor"
        background None
        idle_background None
        insensitive_background None
        ysize None
        padding (1, 1, 1, 1)
        margin (1, 1)
    style new_action_editor_text:
        color "#CCC"
        outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
        size 16
    style new_action_editor_button_text is new_action_editor_text:
        hover_underline True
        selected_color "#FFF"
        insensitive_color "#888"
    style new_action_editor_label:
        xminimum 110
    style new_action_editor_vbox xfill True
    style new_action_editor_bar is slider:
        # ysize _viewers.timeline_ysize
        xoffset _viewers.key_half_xsize
        xsize config.screen_width-_viewers.c_box_size-50-_viewers.key_half_xsize

    style new_action_editor_a_button:
        take new_action_editor_button
        size_group None
        xalign 1.
    style new_action_editor_a_button_text is new_action_editor_button_text
    style new_action_editor_a_bar is new_action_editor_bar

    style new_action_editor_fixed:
        xsize config.screen_width-_viewers.c_box_size-50+_viewers.key_half_xsize
        ysize _viewers.key_ysize
        yalign .5
    # style new_action_editor_drag:
    #     xanchor .5

    style new_action_editor_b_button:
        take new_action_editor_button
        size_group "new_action_editor_b"
        xminimum 90
    style new_action_editor_b_button_text is new_action_editor_button_text:
        xalign 1.0

    style new_action_editor_c_text is new_action_editor_text
    style new_action_editor_c_button is new_action_editor_button:
        size_group "new_action_editor_c"
    style new_action_editor_c_button_text is new_action_editor_button_text
    style new_action_editor_c_bar is new_action_editor_bar
    style new_action_editor_c_hbox:
        size_group "new_action_editor_c"
        xsize _viewers.c_box_size
        ysize _viewers.key_ysize


    style _viewers_alternate_menu_frame:
        background "#222"
    style _viewers_alternate_menu_button is new_action_editor_button
    style _viewers_alternate_menu_button_text is new_action_editor_button_text

# tab="images"/"camera", layer="master",  
screen _action_editor(tab="camera", layer="master", opened=0, time=0, page=0):
    $int_format = "{:> }" 
    $float_format = "{:> .2f}"
    $generate_changed = _viewers.generate_changed
    $get_property = _viewers.get_property
    $get_value = _viewers.get_value
    $current_scene = _viewers.current_scene
    $scene_keyframes = _viewers.scene_keyframes
    $all_keyframes = _viewers.all_keyframes
    $change_time = _viewers.change_time
    $get_sorted_keyframes = _viewers.get_sorted_keyframes
    $current_time = _viewers.current_time
    $edit_value = _viewers.edit_value
    $reset = _viewers.reset
    $force_plus = _viewers.force_plus
    $force_float = _viewers.force_float
    $force_wide_range = _viewers.force_wide_range
    $props_sets = _viewers.props_sets
    $props_groups = _viewers.props_groups
    $keyframes_exist = _viewers.keyframes_exist

    $play_action = [SensitiveIf(get_sorted_keyframes(current_scene) or len(scene_keyframes) > 1), \
        SelectedIf(False), Function(_viewers.play, play=True), \
        Show("_action_editor", tab=tab, layer=layer, opened=opened, page=page, time=_viewers.get_animation_delay())]
    if get_value("perspective", scene_keyframes[current_scene][1], True):
        key "rollback"    action Function(generate_changed("offsetZ"), get_property("offsetZ")+100+persistent._wide_range)
        key "rollforward" action Function(generate_changed("offsetZ"), get_property("offsetZ")-100+persistent._wide_range)
    key "K_SPACE" action play_action
    key "action_editor" action NullAction()

    $offsetX, offsetY = get_property("offsetX"), get_property("offsetY")
    $value_range = persistent._wide_range
    $move_amount1 = 100
    $move_amount2 = 300
    if get_value("perspective", scene_keyframes[current_scene][1], True):
        if _viewers.fps_keymap:
            key "s" action Function(generate_changed("offsetY"), offsetY + move_amount1 + value_range)
            key "w" action Function(generate_changed("offsetY"), offsetY - move_amount1 + value_range)
            key "a" action Function(generate_changed("offsetX"), offsetX - move_amount1 + value_range)
            key "d" action Function(generate_changed("offsetX"), offsetX + move_amount1 + value_range)
            key "S" action Function(generate_changed("offsetY"), offsetY + move_amount2 + value_range)
            key "W" action Function(generate_changed("offsetY"), offsetY - move_amount2 + value_range)
            key "A" action Function(generate_changed("offsetX"), offsetX - move_amount2 + value_range)
            key "D" action Function(generate_changed("offsetX"), offsetX + move_amount2 + value_range)
        else:
            key "j" action Function(generate_changed("offsetY"), offsetY + move_amount1 + value_range)
            key "k" action Function(generate_changed("offsetY"), offsetY - move_amount1 + value_range)
            key "h" action Function(generate_changed("offsetX"), offsetX - move_amount1 + value_range)
            key "l" action Function(generate_changed("offsetX"), offsetX + move_amount1 + value_range)
            key "J" action Function(generate_changed("offsetY"), offsetY + move_amount2 + value_range)
            key "K" action Function(generate_changed("offsetY"), offsetY - move_amount2 + value_range)
            key "H" action Function(generate_changed("offsetX"), offsetX - move_amount2 + value_range)
            key "L" action Function(generate_changed("offsetX"), offsetX + move_amount2 + value_range)

    if time:
        timer time+1 action [Show("_action_editor", tab=tab, layer=layer, opened=opened, page=page), \
                            Function(change_time, current_time), renpy.restart_interaction]
        key "game_menu" action [Show("_action_editor", tab=tab, layer=layer, opened=opened, page=page), \
                            Function(change_time, current_time)]
        key "hide_windows" action NullAction()
    else:
        key "game_menu" action Return()

    $state_list = [tag for tag, z in _viewers.zorder_list[current_scene][layer]]
    $page_list = []
    if len(state_list) > _viewers.tab_amount_in_page:
        for i in range(0, len(state_list)//_viewers.tab_amount_in_page):
            $page_list.append(state_list[i*_viewers.tab_amount_in_page:(i+1)*_viewers.tab_amount_in_page])
        if len(state_list)%_viewers.tab_amount_in_page != 0:
            $page_list.append(state_list[len(state_list)//_viewers.tab_amount_in_page*_viewers.tab_amount_in_page:])
    else:
        $page_list.append(state_list)
    $state=_viewers.get_image_state(layer)
    if get_value("perspective", scene_keyframes[current_scene][1], True) == False and tab == "camera":
        $tab = state_list[0]

    frame:
        style_group "action_editor"
        if time:
            at _no_show()
        has vbox

        hbox:
            style_group "action_editor_a"
            textbutton _("time: [current_time:>05.2f] s") action Function(_viewers.edit_time)
            textbutton _("<") action Function(_viewers.prev_time)
            textbutton _(">") action Function(_viewers.next_time)
            textbutton _("play") action play_action
            bar adjustment ui.adjustment(range=persistent._time_range, value=current_time, changed=change_time):
                xalign 1. yalign .5 style "action_editor_bar"
        hbox:
            style_group "action_editor_a"
            textbutton _("option") action Show("_action_editor_option")
            textbutton _("remove keyframes"):
                action [SensitiveIf(current_time in get_sorted_keyframes(current_scene)), \
                Function(_viewers.remove_all_keyframe, current_time), renpy.restart_interaction]
            textbutton _("move keyframes"):
                action [SensitiveIf(current_time in get_sorted_keyframes(current_scene)), \
                SelectedIf(False), SetField(_viewers, "moved_time", current_time), Show("_move_keyframes")]
            textbutton _("hide") action HideInterface()
            textbutton _("clipboard") action Function(_viewers.put_clipboard)
            textbutton _("x") action Return()
        hbox:
            style_group "action_editor_a"
            textbutton _("scene") action [SensitiveIf(len(scene_keyframes) > 1), Show("_scene_editor")]
            for i, ks in enumerate(all_keyframes):
                textbutton "[i]" action [SelectedIf(current_scene == i), Function(_viewers.change_scene, i), Show("_action_editor")]
            textbutton _("+") action _viewers.add_scene
        hbox:
            style_group "action_editor_a"
            xfill False
            textbutton _("<"):
                action [SensitiveIf(page != 0), Show("_action_editor", tab=tab, layer=layer, page=page-1), renpy.restart_interaction]
            textbutton _("camera"):
                action [SensitiveIf(get_value("perspective", scene_keyframes[current_scene][1], True) != False),
                SelectedIf(tab == "camera"), Show("_action_editor", tab="camera")]
            for n in page_list[page]:
                textbutton "{}".format(n):
                    action [SelectedIf(n == tab), Show("_action_editor", tab=n, layer=layer, page=page)]
            textbutton _("+"):
                action Function(_viewers.add_image, layer)
            textbutton _(">"):
                action [SensitiveIf(len(page_list) != page+1), Show("_action_editor", tab=tab, layer=layer, page=page+1), renpy.restart_interaction]

        if tab == "camera":
            for i, (props_set_name, props_set) in enumerate(props_sets):
                if i == opened:
                    textbutton "- " + props_set_name action [SelectedIf(True), NullAction()]
                    for p, d in _viewers.camera_props:
                        if p in props_set and (p not in props_groups["focusing"] or 
                            (persistent._viewer_focusing and get_value("perspective", scene_keyframes[current_scene][1], True))):
                            $value = get_property(p)
                            $f = generate_changed(p)
                            $use_wide_range = p not in force_float and (p in force_wide_range or ((value is None and isinstance(d, int)) or isinstance(value, int)))
                            if use_wide_range:
                                $value_range = persistent._wide_range
                                $bar_page = 1
                            else:
                                $value_range = persistent._narrow_range
                                $bar_page = .05
                            if not use_wide_range or isinstance(value, float):
                                $value_format = float_format
                            else:
                                $value_format = int_format
                            hbox:
                                textbutton "  [p]":
                                    action [SensitiveIf(p in all_keyframes[current_scene]),
                                    SelectedIf(keyframes_exist(p)), Show("_edit_keyframe", key=p, use_wide_range=use_wide_range, change_func=f)]
                                if p == "perspective":
                                    textbutton "[value]":
                                        action [SelectedIf(get_value(p, scene_keyframes[current_scene][1], True)),
                                        Function(_viewers.toggle_perspective)]
                                elif p in _viewers.any_props:
                                    if isinstance(value, str):
                                        textbutton "'[value]'":
                                            action [SelectedIf(get_value(p, scene_keyframes[current_scene][1], True)), 
                                            Function(_viewers.edit_any, p)]
                                    else:
                                        textbutton "[value]":
                                            action [SelectedIf(get_value(p, scene_keyframes[current_scene][1], True)), 
                                            Function(_viewers.edit_any, p)]
                                elif p in _viewers.boolean_props:
                                    textbutton "[value]":
                                        action [SelectedIf(get_value(p, scene_keyframes[current_scene][1], True)), 
                                        Function(_viewers.toggle_boolean_property, p)]
                                else:
                                    if p in force_plus:
                                        $bar_value = value
                                    else:
                                        $bar_value = value + value_range
                                        $value_range = value_range*2
                                    textbutton value_format.format(value):
                                        action Function(edit_value, f, use_wide_range=use_wide_range, default=value, force_plus=p in force_plus)
                                        alternate Function(reset, p) style_group "action_editor_b"
                                    bar adjustment ui.adjustment(range=value_range, value=bar_value, page=bar_page, changed=f):
                                        xalign 1. yalign .5 style "action_editor_bar"
                else:
                    hbox:
                        textbutton "+ "+props_set_name:
                            action Show("_action_editor", tab=tab, layer=layer, opened=i, page=page)
        else:
            for i, (props_set_name, props_set) in enumerate(props_sets):
                if i == opened:
                    textbutton "- " + props_set_name action [SelectedIf(True), NullAction()]
                    for p, d in _viewers.transform_props:
                        if p in props_set and (p not in props_groups["focusing"] and (((persistent._viewer_focusing 
                            and get_value("perspective", scene_keyframes[current_scene][1], True)) and p != "blur") 
                            or (not persistent._viewer_focusing or not get_value("perspective", scene_keyframes[current_scene][1], True)))):
                            $key = (tab, layer, p)
                            $value = get_property(key)
                            $f = generate_changed(key)
                            $use_wide_range = p not in force_float and (p in force_wide_range or ((value is None and isinstance(d, int)) or isinstance(value, int)))
                            if use_wide_range:
                                $value_range = persistent._wide_range
                                $bar_page = 1
                            else:
                                $value_range = persistent._narrow_range
                                $bar_page = .05
                            if not use_wide_range or isinstance(value, float):
                                $value_format = float_format
                            else:
                                $value_format = int_format
                            hbox:
                                textbutton "  [p]":
                                    action [SensitiveIf(key in all_keyframes[current_scene]), 
                                    SelectedIf(keyframes_exist(key)), 
                                    Show("_edit_keyframe", key=key, use_wide_range=use_wide_range, change_func=f)]
                                if p == "child":
                                    textbutton "[value[0]]":
                                        action [SelectedIf(keyframes_exist((tab, layer, "child"))), 
                                        Function(_viewers.change_child, tab, layer, default=value[0])]
                                        size_group None
                                    textbutton "with" action None size_group None
                                    textbutton "[value[1]]":
                                        action [SensitiveIf(key in all_keyframes[current_scene]), 
                                        SelectedIf(keyframes_exist((tab, layer, "child"))), 
                                        Function(_viewers.edit_transition, tab, layer)]
                                        size_group None
                                elif p in _viewers.any_props:
                                    if isinstance(value, str):
                                        textbutton "'[value]'":
                                            action [SelectedIf(get_value(p, scene_keyframes[current_scene][1], True)), 
                                            Function(_viewers.edit_any, p)]
                                    else:
                                        textbutton "[value]":
                                            action [SelectedIf(get_value(p, scene_keyframes[current_scene][1], True)), 
                                            Function(_viewers.edit_any, p)]
                                elif p in _viewers.boolean_props:
                                    textbutton "[value]":
                                        action [SelectedIf(get_value(key, scene_keyframes[current_scene][1], True)), 
                                        Function(_viewers.toggle_boolean_property, key)]
                                else:
                                    if p in force_plus:
                                        $bar_value = value
                                    else:
                                        $bar_value = value + value_range
                                        $value_range = value_range*2
                                    textbutton value_format.format(value):
                                        action Function(edit_value, f, use_wide_range=use_wide_range, default=value, force_plus=p in force_plus)
                                        alternate Function(reset, key) style_group "action_editor_b"
                                    bar adjustment ui.adjustment(range=value_range, value=bar_value, page=bar_page, changed=f):
                                        xalign 1. yalign .5 style "action_editor_bar"
                else:
                    hbox:
                        textbutton "+ "+props_set_name:
                            action Show("_action_editor", tab=tab, layer=layer, opened=i, page=page)
        hbox:
            xfill False
            xalign 1.
            if tab == "camera":
                textbutton _("clipboard") action Function(_viewers.put_camera_clipboard) size_group None
                # textbutton _("reset") action [_viewers.camera_reset, renpy.restart_interaction] size_group None
            else:
                textbutton _("remove") action [
                    SensitiveIf(tab in _viewers.image_state[current_scene][layer]), 
                    Show("_action_editor", tab="camera", layer=layer, opened=opened, page=page), 
                    Function(_viewers.remove_image, layer, tab)] size_group None
                textbutton _("clipboard"):
                    action Function(_viewers.put_image_clipboard, tab, layer)
                    size_group None
                # textbutton _("reset") action [_viewers.image_reset, renpy.restart_interaction] size_group None

    if not time and persistent._show_camera_icon:
        add _viewers.camera_icon

transform _no_show():
    alpha 0

init -1598:
    style action_editor_frame:
        background "#0003"
    style action_editor_button:
        size_group "action_editor"
        background None
        idle_background None
        insensitive_background None
        ysize None
    style action_editor_text:
        color "#CCC"
        outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
        size 18
    style action_editor_button_text is action_editor_text:
        hover_underline True
        selected_color "#FFF"
        insensitive_color "#888"
    style action_editor_label:
        xminimum 110
    style action_editor_vbox xfill True
    style action_editor_bar is slider:
        ysize 20

    style action_editor_a_button:
        take action_editor_button
        size_group None
    style action_editor_a_button_text is action_editor_button_text
    style action_editor_a_bar is action_editor_bar

    style action_editor_b_button:
        take action_editor_button
        size_group "action_editor_b"
        xminimum 140
    style action_editor_b_button_text is action_editor_button_text:
        xalign 1.0

screen _input_screen(message="type value", default=""):
    modal True
    key "game_menu" action Return("")

    frame:
        style_group "action_editor_input"

        has vbox

        label message

        hbox:
            input default default copypaste True

screen _action_editor_option():
    modal True
    key "game_menu" action Hide("_action_editor_option")
    frame:
        style_group "action_editor_modal"
        has vbox
        viewport:
            ymaximum 0.7
            mousewheel True
            scrollbars "vertical"

            has vbox
            text _("Use Legacy ActionEditor Screen(recommend legacy gui for the 4:3 or small window)")
            textbutton _("legacy gui") action [SelectedIf(persistent._viewer_legacy_gui), ToggleField(persistent, "_viewer_legacy_gui"), If(persistent._viewer_legacy_gui, true=[Hide("_action_editor"), Show("_new_action_editor")], false=[Hide("_new_action_editor"), Show("_action_editor")]), Hide("_action_editor_option")]
            text _("Show/Hide rule of thirds lines")
            textbutton _("show rot") action [SelectedIf(persistent._viewer_rot), ToggleField(persistent, "_viewer_rot")]
            text _("Show/Hide window during animation in clipboard(window is forced to be hide when the action has multi scene)")
            textbutton _("hide window") action [SelectedIf(persistent._viewer_hide_window), ToggleField(persistent, "_viewer_hide_window")]
            text _("Allow/Disallow skipping animation in clipboard(be forced to allow when the action has multi scene)")
            text _("(*This doesn't work correctly when the animation include loops and that tag is already shown)")
            textbutton _("skippable") action [SelectedIf(persistent._viewer_allow_skip), ToggleField(persistent, "_viewer_allow_skip")]
            text _("Enable/Disable simulating camera blur(This is available when perspective is True)")
            textbutton _("focusing") action [SensitiveIf(_viewers.get_value("perspective", _viewers.scene_keyframes[_viewers.current_scene][1], True)), SelectedIf(persistent._viewer_focusing), ToggleField(persistent, "_viewer_focusing"), Function(_viewers.change_time, _viewers.current_time)]
            text _("One line includes only one property in clipboard data")
            textbutton _("one_line_one_property") action [ToggleField(persistent, "_one_line_one_prop")]
            text _("Assign default warper")
            textbutton "[persistent._viewer_warper]" action _viewers.select_default_warper
            text _("Assign default transition(example: dissolve, Dissolve(5), None)")
            textbutton "[persistent._viewer_transition]" action _viewers.edit_default_transition
            text _("the time range of property bar(type float)")
            textbutton "[persistent._time_range]" action Function(_viewers.edit_range_value, persistent, "_time_range", False)
            text _("Show/Hide camera and image icon")
            textbutton _("show icon") action [SelectedIf(persistent._show_camera_icon), ToggleField(persistent, "_show_camera_icon")]
            text _("")
            text _("following options have effect for only New GUI")
            text _("Open only one page at once")
            textbutton _("open only one page") action [SelectedIf(persistent._open_only_one_page), ToggleField(persistent, "_open_only_one_page"), If(not persistent._viewer_legacy_gui, true=Show("_new_action_editor"))]
            text _("Set the amount of change per pixel when dragging the value of the integer property")
            textbutton "[persistent._viewers_wide_dragg_speed]" action Function(_viewers.edit_range_value, persistent, "_viewers_wide_dragg_speed", True)
            text _("Set the amount of change per pixel when dragging the value of the float property")
            textbutton "[persistent._viewers_narow_dragg_speed]" action Function(_viewers.edit_range_value, persistent, "_viewers_narow_dragg_speed", False)
            text _("Set the list of channels for playing in ActionEditor")
            textbutton "[persistent._viewer_channel_list]" action _viewers.edit_channel_list
            text _("the wide range of property in Graphic Editor(type int)")
            textbutton "[persistent._graphic_editor_wide_range]" action Function(_viewers.edit_range_value, persistent, "_graphic_editor_wide_range", True)
            text _("the narrow range of property in Graphic Editor(type float)")
            textbutton "[persistent._graphic_editor_narrow_range]" action Function(_viewers.edit_range_value, persistent, "_graphic_editor_narrow_range", False)
            text _("")
            text _("following options have effect for only Legacy GUI")
            text _("the wide range of property bar which is mainly used for int values(type int)")
            textbutton "[persistent._wide_range]" action Function(_viewers.edit_range_value, persistent, "_wide_range", True)
            text _("the narrow range of property bar which is used for float values(type float)")
            textbutton "[persistent._narrow_range]" action Function(_viewers.edit_range_value, persistent, "_narrow_range", False)

        textbutton _("Return") action Hide("_action_editor_option") xalign .9

screen _warper_selecter(current_warper=""):
    modal True
    key "game_menu" action Return("")

    frame:
        background "#AAAA"
        style_group "action_editor_subscreen"

        has vbox

        label _("Select a warper function")
        viewport:
            mousewheel True
            edgescroll (100, 100)
            scrollbars "vertical"
            vbox:
                for warper in sorted(renpy.atl.warpers.keys()):
                    textbutton warper:
                        action [SelectedIf((persistent._viewer_warper == warper and not current_warper) or warper == current_warper), Return(warper)]
                        hovered Show("_warper_graph", warper=warper) unhovered Hide("_warper")
        hbox:
            textbutton _("add") action OpenURL("http://renpy.org/wiki/renpy/doc/cookbook/Additional_basic_move_profiles")
            textbutton _("close") action Return("")

screen _warper_graph(warper):
    $ t=120
    $ length=300
    $ xpos=config.screen_width-400
    $ ypos=200
    # add Solid("#000", xsize=3, ysize=1.236*length, xpos=xpos+length/2, ypos=length/2+xpos, rotate=45, anchor=(.5, .5)) 
    add Solid("#CCC", xsize=length, ysize=length, xpos=xpos, ypos=ypos ) 
    add Solid("#000", xsize=length, ysize=3, xpos=xpos, ypos=length+ypos ) 
    add Solid("#000", xsize=length, ysize=3, xpos=xpos, ypos=ypos ) 
    add Solid("#000", xsize=3, ysize=length, xpos=xpos+length, ypos=ypos)
    add Solid("#000", xsize=3, ysize=length, xpos=xpos, ypos=ypos)
    for i in range(1, t):
        $ysize=int(length*renpy.atl.warpers[warper](i/float(t)))
        if ysize >= 0:
            add Solid("#000", xsize=length//t, ysize=ysize, xpos=xpos+i*length//t, ypos=length+ypos, yanchor=1.) 
        else:
            add Solid("#000", xsize=length//t, ysize=-ysize, xpos=xpos+i*length//t, ypos=length+ypos-ysize, yanchor=1.) 

screen _move_keyframes:
    modal True
    key "game_menu" action Hide("_move_keyframes")
    frame:
        yalign .5
        style_group "action_editor_subscreen"
        has vbox
        textbutton _("time: [_viewers.moved_time:>.2f] s") action Function(_viewers.edit_move_all_keyframe)
        bar adjustment ui.adjustment(range=persistent._time_range, value=_viewers.moved_time, changed=renpy.curry(_viewers.move_all_keyframe)(old=_viewers.moved_time)):
            xalign 1. yalign .5 style "action_editor_bar"
        textbutton _("close") action Hide("_move_keyframes") xalign .98

screen _edit_keyframe(key, change_func=None, use_wide_range=False):
    $check_points = _viewers.all_keyframes[_viewers.current_scene][key]
    if isinstance(key, tuple):
        $n, l, p = key
        $k_list = [key]
        $check_points_list = [check_points]
        $loop_button_action = [ToggleDict(_viewers.loops[_viewers.current_scene], key)]
        for gn, ps in _viewers.props_groups.items():
            if p in ps:
                $k_list = [(n, l, p) for p in _viewers.props_groups[gn]]
                $check_points_list = [_viewers.all_keyframes[_viewers.current_scene][k2] for k2 in k_list]
                $loop_button_action = [ToggleDict(_viewers.loops[_viewers.current_scene], k2) for k2 in k_list+[(n, l, gn)]]
    else:
        $k_list = [key]
        $p = key
        $check_points_list = [check_points]
        $loop_button_action = [ToggleDict(_viewers.loops[_viewers.current_scene], key)]
        for gn, ps in _viewers.props_groups.items():
            if key in ps:
                if gn != "focusing":
                    $k_list = _viewers.props_groups[gn]
                    $check_points_list = [_viewers.all_keyframes[_viewers.current_scene][k2] for k2 in k_list]
                    $loop_button_action = [ToggleDict(_viewers.loops[_viewers.current_scene], k2) for k2 in k_list+[gn]]

    modal True
    key "game_menu" action Hide("_edit_keyframe")
    frame:
        style_group "action_editor_subscreen"
        xfill True
        has vbox
        label _("KeyFrames") xalign .5
        for i, (v, t, w) in enumerate(check_points):
            if t == _viewers.scene_keyframes[_viewers.current_scene][1]:
                hbox:
                    textbutton _("x") action [SensitiveIf(len(check_points) == 1), Function(_viewers.remove_keyframe, remove_time=t, key=k_list), Hide("_edit_keyframe")] size_group None
                    if p == "child":
                        textbutton "[v[0]]" action Function(_viewers.change_child, n, l, time=t, default=v[0]) size_group None
                        textbutton "with" action None size_group None
                        textbutton "[v[1]]" action Function(_viewers.edit_transition, n, l, time=t) size_group None
                    else:
                        textbutton _("{}".format(w)) action None
                        if p not in [prop for ps in _viewers.props_groups.values() for prop in ps]:
                            textbutton _("spline") action None
                        textbutton _("{}".format(v)) action [\
                            Function(_viewers.edit_value, change_func, default=v, use_wide_range=use_wide_range, force_plus=p in _viewers.force_plus, time=t), \
                            Function(_viewers.change_time, t)]
                    textbutton _("[t:>05.2f] s") action None
            else:
                hbox:
                    textbutton _("x") action [Function(_viewers.remove_keyframe, remove_time=t, key=k_list), renpy.restart_interaction] size_group None
                    if p == "child":
                        textbutton "[v[0]]" action Function(_viewers.change_child, n, l, time=t, default=v[0]) size_group None
                        textbutton "with" action None size_group None
                        textbutton "[v[1]]" action Function(_viewers.edit_transition, n, l, time=t) size_group None
                    else:
                        textbutton _("{}".format(w)) action Function(_viewers.edit_warper, check_points=check_points_list, old=t, value_org=w)
                        if p not in [prop for ps in _viewers.props_groups.values() for prop in ps]:
                            textbutton _("spline") action [\
                                SelectedIf(t in _viewers.splines[_viewers.current_scene][key]), \
                                Show("_spline_editor", change_func=change_func, \
                                    key=key, prop=p, pre=check_points[i-1], post=check_points[i], default=v, \
                                    use_wide_range=use_wide_range, force_plus=p in _viewers.force_plus, time=t)]
                        textbutton _("{}".format(v)) action [\
                            Function(_viewers.edit_value, change_func, default=v, use_wide_range=use_wide_range, force_plus=p in _viewers.force_plus, time=t), \
                            Function(_viewers.change_time, t)]
                    textbutton _("[t:>05.2f] s") action Function(_viewers.edit_move_keyframe, keys=k_list, old=t)
                    bar adjustment ui.adjustment(range=persistent._time_range, value=t, changed=renpy.curry(_viewers.move_keyframe)(old=t, keys=k_list)):
                        xalign 1. yalign .5 style "action_editor_bar"
        hbox:
            textbutton _("loop") action loop_button_action size_group None
            textbutton _("close") action Hide("_edit_keyframe") xalign .98 size_group None

screen _spline_editor(change_func, key, prop, pre, post, default, use_wide_range, force_plus, time):

    modal True
    key "game_menu" action Hide("_spline_editor")
    $cs = _viewers.all_keyframes[_viewers.current_scene][key]
    if use_wide_range:
        $value_range = persistent._wide_range
        $_page = 1
    else:
        $value_range = persistent._narrow_range
        $_page = 0.05
    if not force_plus:
        default old_v = post[0] + value_range
    else:
        default old_v = post[0]
    on "show" action [Function(_viewers.change_time, time)]
    on "hide" action [Function(change_func, old_v), Function(_viewers.change_time, time)]

    frame:
        style_group "spline_editor"
        xfill True
        has vbox
        label _("spline_editor") xalign .5
        hbox:
            null width 50
            text " "
            text "Start"
            text "[pre[0]]"
        if time in _viewers.splines[_viewers.current_scene][key]:
            for i, v in enumerate(_viewers.splines[_viewers.current_scene][key][time]):
                textbutton _("+") action [Function(_viewers.add_knot, key, time, pre[0], knot_number=i), renpy.restart_interaction]
                hbox:
                    null width 50
                    textbutton _("x") action [Function(_viewers.remove_knot, key, time, i), renpy.restart_interaction] size_group None
                    textbutton "Knot{}".format(i+1) action None
                    textbutton "{}".format(v) action [Function(_viewers.edit_value, renpy.curry(change_func)(time=time, knot_number=i), default=v, use_wide_range=use_wide_range, force_plus=force_plus, time=time)]
                    if force_plus:
                        $_v = v
                    else:
                        $_v = v + value_range
                        $_value_range = value_range*2
                    bar adjustment ui.adjustment(range=_value_range, value=_v, page=_page, changed=renpy.curry(change_func)(time=time, knot_number=i)):
                        xalign 1. yalign .5 style "action_editor_bar"
        textbutton _("+") action [Function(_viewers.add_knot, key, time, pre[0]), renpy.restart_interaction]
        hbox:
            null width 50
            text " "
            text "End"
            text "[post[0]]"
        hbox:
            xfill True
            textbutton _("close") action Hide("_spline_editor") xalign .9

screen _scene_editor():

    modal True
    key "game_menu" action Hide("_scene_editor")
    # on "hide" action Show("_action_editor")

    frame:
        style_group "scene_editor"
        xfill True
        has vbox
        label _("scene_editor") xalign .5
        text "    Scene0"
        for i, (tran, t, w) in enumerate(_viewers.scene_keyframes):
            if i > 0:
                hbox:
                    textbutton _("x") action Function(_viewers.remove_scene, i)
                    textbutton "Scene[i]" action None
                    textbutton "with" action None
                    textbutton "[tran]" action Function(_viewers.edit_scene_transition, i)
                    textbutton "[t:>.2f] s" action Function(_viewers.edit_move_scene, i)
                    bar adjustment ui.adjustment(range=persistent._time_range, value=t, changed=renpy.curry(_viewers.move_scene)(scene_num=i)) xalign 1. yalign .5 style "action_editor_bar"
        hbox:
            xfill True
            textbutton _("close") action Hide("_scene_editor") xalign .9

init -1598:
    style action_editor_modal_frame background "#000D"
    style action_editor_modal_text is action_editor_text color "#AAA"
    style action_editor_modal_button is action_editor_button
    style action_editor_modal_button_text is action_editor_button_text

    style action_editor_input_frame xfill True ypos .1 xmargin .05 ymargin .05 background "#000B"
    style action_editor_input_vbox xfill True spacing 30
    style action_editor_input_label xalign .5
    style action_editor_input_hbox  xalign .5

    style action_editor_subscreen_frame is action_editor_modal_frame
    style action_editor_subscreen_text is action_editor_modal_text
    style action_editor_subscreen_button_text is action_editor_modal_button_text
    style action_editor_subscreen_button is action_editor_modal_button:
        size_group "action_editor_subscreen"

    style spline_editor_frame is action_editor_modal_frame
    style spline_editor_text is action_editor_text size_group "spline_editor"
    style spline_editor_button is action_editor_modal_button size_group "spline_editor"
    style spline_editor_button_text is action_editor_modal_button_text

    style scene_editor_frame is action_editor_modal_frame
    style scene_editor_text is action_editor_text size_group None
    style scene_editor_button is action_editor_modal_button size_group None
    style scene_editor_button_text is action_editor_modal_button_text



init 1 python in _viewers:
    from renpy.store import Function, QueueEvent, Text, BarValue, DictEquality, ShowAlternateMenu


    def return_start_time(start_time):
        if playing:
            change_time(start_time)


    def pause():
        global playing
        if playing:
            change_time(current_time)


    def pos_to_time(x):
        barwidth = config.screen_width - c_box_size - 50 - key_half_xsize
        frac = float(x - key_half_xsize)/barwidth
        goal = round(frac*persistent._time_range, 2)
        if goal < 0:
            goal = 0.
        elif goal > persistent._time_range:
            goal = persistent._time_range
        return goal


    def time_to_pos(time):
        frac = time/persistent._time_range
        barwidth = config.screen_width - c_box_size - 50 - key_half_xsize
        pos = frac*barwidth + key_half_xsize
        if pos > barwidth + key_half_xsize:
            pos = barwidth + key_half_xsize
        if pos < key_half_xsize:
            pos = key_half_xsize
        return pos


    def pos_to_value(y, use_wide_range, force_plus):
        if use_wide_range:
            range = persistent._graphic_editor_wide_range
        else:
            range = persistent._graphic_editor_narrow_range

        barheight = config.screen_height*(1-preview_size)-time_column_height
        if force_plus:
            frac = 1 - (float(y)-key_half_ysize)/(barheight-key_ysize)
            value = frac*range
            if value < 0:
                value = 0.
        else:
            frac = (0.5 - (float(y)-key_half_ysize)/(barheight-key_ysize))*2
            value = frac*range
            if value < -range:
                value = -range
        if value > range:
            value = range
        if use_wide_range:
            value = int(value)
        return value


    def value_to_pos(value, range, force_plus):
        barheight = config.screen_height*(1-preview_size)-time_column_height
        if force_plus:
            frac = value/float(range)
        else:
            frac = value/float(range)*0.5 + 0.5
        pos = barheight - key_ysize - frac*(barheight - 3*key_half_ysize)
        if pos > barheight - key_ysize:
            pos = barheight - key_ysize
        if pos  < key_half_ysize:
            pos = key_half_ysize
        return pos


    def time_and_key_to_pos(time, key, force_plus):
        value = get_value(key, time)
        if is_wide_range(key):
            range = persistent._graphic_editor_wide_range
        else:
            range = persistent._graphic_editor_narrow_range
        return value_to_pos(value, range, force_plus)


    def key_drag_changed(pos, key, time, is_sound=False, in_graphic_mode=None):
        if in_graphic_mode:
            x, y = pos
        else:
            x = pos
        key_list = [key]
        if not is_sound:
            if isinstance(key, tuple):
                n, l, p = key
                for gn, ps in props_groups.items():
                    if p in ps:
                        key_list = [(n, l, p) for p in props_groups[gn]]
            else:
                p = key
                for gn, ps in props_groups.items():
                    if key in ps:
                        if gn != "focusing":
                            key_list = props_groups[gn]

        goal = pos_to_time(x)
        if move_keyframe(new=goal, old=time, keys=key_list, is_sound=is_sound):
            time = goal
        if in_graphic_mode:
            use_wide_range = is_wide_range(key)
            value = pos_to_value(y, use_wide_range, p in force_plus)
            vchanged = generate_changed(key)
            vchanged(to_changed_value(value, p in force_plus, use_wide_range), time)
        return time


    def absolute_pos(st, at):
        (x, y) = renpy.get_mouse_pos()
        if aspect_16_9():
            x = int((x-config.screen_width*(1.-preview_size)/2)/preview_size)
            y = int(y/preview_size)
        else:
            (x, y) = (x/preview_size, y/preview_size)
        return Text("({:>4}, {:>4})".format(x, y), style="new_action_editor_text"), 0.1


    def rel_pos(st, at):
        (x, y) = renpy.get_mouse_pos()
        if aspect_16_9():
            x = int((x-config.screen_width*(1.-preview_size)/2)/preview_size)
            y = int(y/preview_size)
        else:
            (x, y) = (x/preview_size, y/preview_size)
        rx = x/float(config.screen_width)
        ry = y/float(config.screen_height)
        return Text("({:>.3}, {:>.3})".format(rx, ry), style="new_action_editor_text"), 0.1


    def show_current_time(st, at):
        return Text(_("time: {:>05.2f} s").format(current_time), style="new_action_editor_text"), 0.01


    def is_wide_range(key):
        if isinstance(key, tuple):
            _, _, prop = key
            d = get_default(prop)
        else:
            prop = key
            d = get_default(prop, True)
        value = get_property(key)
        return prop not in force_float and (prop in force_wide_range or ((value is None and isinstance(d, int)) or isinstance(value, int)))


    def out_of_viewport():
        #check if there is out of showing range of viewport
        x, y = renpy.get_mouse_pos()
        if y < config.screen_height * preview_size + time_column_height or y > config.screen_height:
            return True
        else:
            return False


    class DraggableValue(renpy.Displayable):


        def __init__(self, format, key, changed, use_wide_range, force_plus, clicked=None, alternate=None, **properties):
            super(DraggableValue, self).__init__(**properties)
            from pygame import MOUSEMOTION, KMOD_CTRL, KMOD_SHIFT
            from pygame.key import get_mods
            from pygame.mouse import get_pressed
            # The child.
            self.format = format
            self.key = key
            self.changed = changed
            self.use_wide_range = use_wide_range
            self.force_plus = force_plus
            self.dragging = False
            self.kwargs = {}
            for k, v in properties.items():
                if k.startswith("text_") and not k.startswith("text_hover_"):
                    self.kwargs[k[5:]] = v
            self.hover_kwargs = dict(self.kwargs)
            for k, v in properties.items():
                if k.startswith("text_hover_"):
                    self.hover_kwargs[k[11:]] = v

            if self.use_wide_range:
                self.change_per_pix = int(persistent._viewers_wide_dragg_speed)
            else:
                self.change_per_pix = float(persistent._viewers_narow_dragg_speed)
            self.clicking = False
            self.hovered = False

            self.MOUSEMOTION = MOUSEMOTION
            self.SLOW = 0.33
            self.NORMAL = 1.0
            self.FAST = 3.0
            self.KMOD_SHIFT = KMOD_SHIFT
            self.KMOD_CTRL = KMOD_CTRL
            self.get_mods = get_mods
            self.get_pressed = get_pressed


            self.speed = 1.0


        def __eq__(self, other):
            if not isinstance(other, DraggableValue):
                return False
            return True


        def render(self, width, height, st, at):
            value = get_property(self.key)
            if self.hovered:
                kwargs = self.hover_kwargs
            else:
                kwargs = self.kwargs
            d = Text(self.format.format(value), align=(.5, .5), **kwargs)
            box = Fixed()
            box.add(d)
            render = box.render(width, height, st, at)
            self.width, self.height = render.get_size()
            return render


        def event(self, ev, x, y, st):
            clicking, _, _ = self.get_pressed()
            if not clicking and self.dragging:
                self.dragging = False
                self.clicking = False
                self.last_x = None

            if ev.type == self.MOUSEMOTION and self.clicking:
                self.dragging = True
                v = ((x - self.last_x)*self.change_per_pix)*self.speed+self.value
                if self.use_wide_range:
                    v = int(v)
                self.changed(to_changed_value(v, self.force_plus, self.use_wide_range))

            self.hovered = False
            if not self.dragging and x >= 0 and x <= self.width and y >= 0 and y <= self.height:
                self.hovered = True
                if renpy.map_event(ev, "mousedown_1") and not out_of_viewport():
                    if self.get_mods() & self.KMOD_CTRL:
                        self.speed = self.SLOW
                    elif self.get_mods() & self.KMOD_SHIFT:
                        self.speed = self.FAST
                    else:
                        self.speed = self.NORMAL
                    self.clicking = True
                    self.last_x = x
                    self.value = get_property(self.key)
                    raise renpy.display.core.IgnoreEvent()
                elif not self.dragging and renpy.map_event(ev, "mouseup_1"):
                    if self.clicking == True:
                        self.clicking = False
                        action=Function(edit_value, self.changed, self.use_wide_range, self.value, self.force_plus),
                        rv = renpy.run(action)
                        if rv is not None:
                            return rv
                        raise renpy.display.core.IgnoreEvent()
                elif renpy.map_event(ev, "button_alternate"):
                    alternate=Function(reset, self.key),
                    rv = renpy.run(alternate)
                    if rv is not None:
                        return rv
                    raise renpy.display.core.IgnoreEvent()
            elif self.clicking and renpy.map_event(ev, "mouseup_1"):
                self.dragging = False
                self.clicking = False
                self.last_x = None
                raise renpy.display.core.IgnoreEvent()
            if not playing:
                renpy.redraw(self, 0)


        def per_interact(self):
            if not playing:
                renpy.redraw(self, 0)


    class TimeLine(renpy.Displayable):


        def __init__(self, scene, tag, props_set=None, key=None, changed=None, use_wide_range=None, opened=None, in_graphic_mode=[]):
            super(TimeLine, self).__init__()
            from pygame import MOUSEMOTION
            from renpy.store import Function, Solid, Fixed
            self.scene = scene
            self.tag = tag
            self.props_set = props_set
            self.key = key
            self.changed=changed
            self.use_wide_range=use_wide_range
            self.opened=opened
            self.in_graphic_mode = in_graphic_mode

            self.children = []
            self.warpkey_children = []
            self.knot_children = []
            self.graphic_mode = self.key in self.in_graphic_mode
            self.background = TimeLineBackground(self.key, self.graphic_mode)
            self.mark_num = 100


        def __eq__(self, other):
            if not isinstance(other, TimeLine):
                return False
            if self.scene != other.scene:
                return False
            if self.tag != other.tag:
                return False
            if self.props_set != other.props_set:
                return False
            if self.key != other.key:
                return False
            if self.in_graphic_mode != other.in_graphic_mode:
                return False
            return True


        def render(self, width, height, st, at):
            new_children = []
            new_warpkey_children = []
            new_knot_children = []
            box = Fixed()
            box.add(self.background.get_child())

            if self.tag is None:
                _, t, _ = scene_keyframes[self.scene]
                scene_start = scene_keyframes[self.scene][1]
                child = KeyFrame(insensitive_key_child, t, insensitive_key_hovere_child, False, key=None, clicked=Function(change_time, t))
                new_children.append(child)
                for key, cs in all_keyframes[self.scene].items():
                    if isinstance(key, tuple):
                        p = key[2]
                    else:
                        p = key
                    if p not in props_groups["focusing"] or \
                        (persistent._viewer_focusing and get_value("perspective", scene_start, True)):
                        for c in cs:
                            _, t, _ = c
                            child = KeyFrame(insensitive_key_child, t, insensitive_key_hovere_child, False, key=None, clicked=Function(change_time, t))
                            new_children.append(child)
            elif self.tag == "camera" and self.props_set is None and self.key is None:
                scene_start = scene_keyframes[self.scene][1]
                for p, d in camera_props:
                    _all_keyframes = all_keyframes[self.scene]
                    if (p not in props_groups["focusing"] or
                        (persistent._viewer_focusing and get_value("perspective", scene_start, True))):
                        for _, t, _ in _all_keyframes.get(p, []):
                            child = KeyFrame(insensitive_key_child, t, insensitive_key_hovere_child, False, key=None, clicked=Function(change_time, t))
                            new_children.append(child)
            elif self.tag == "camera" and self.props_set is not None:
                _all_keyframes = all_keyframes[self.scene]
                scene_start = scene_keyframes[self.scene][1]
                for p in self.props_set:
                    if (p not in props_groups["focusing"] or \
                        (persistent._viewer_focusing and get_value("perspective", scene_start, True))):
                        for _, t, _ in _all_keyframes.get(p, []):
                            child = KeyFrame(insensitive_key_child, t, insensitive_key_hovere_child, False, key=None, clicked=Function(change_time, t))
                            new_children.append(child)
            elif self.tag == "camera" and self.key is not None and not self.graphic_mode:
                for c in all_keyframes[self.scene].get(self.key, []):
                    _, t, _ = c
                    child = KeyFrame(key_child, t, key_hovere_child, key=self.key,
                        clicked=Function(change_time, t),
                        alternate=ShowAlternateMenu(
                            generate_menu(key=self.key, check_point=c, use_wide_range=self.use_wide_range,
                                change_func=self.changed, opened=self.opened, in_graphic_mode=self.in_graphic_mode),
                            style_prefix="_viewers_alternate_menu"))
                    new_children.append(child)
            elif self.tag == "camera" and self.key is not None and self.graphic_mode:
                last_v, last_t = None, None
                is_force_plus = self.key in force_plus
                for c in all_keyframes[self.scene].get(self.key, []):
                    v, t, w = c
                    child = KeyFrame(key_child, t, key_hovere_child, key=self.key, in_graphic_mode=True,
                        clicked=Function(change_time, t),
                        alternate=ShowAlternateMenu(
                            generate_menu(key=self.key, check_point=c, use_wide_range=self.use_wide_range,
                                change_func=self.changed, opened=self.opened, in_graphic_mode=self.in_graphic_mode),
                            style_prefix="_viewers_alternate_menu"))
                    new_children.append(child)

                    if last_v is not None:
                        v_diff = (v - last_v)
                        t_diff = (t - last_t)
                        for t2 in range(1, self.mark_num):
                            xpos = time_to_pos(last_t + t_diff*t2/self.mark_num)
                            ypos = time_and_key_to_pos(last_t + t_diff*t2/self.mark_num, self.key, is_force_plus)
                            box.add(Transform(interpolate_key_child, xoffset=xpos, yoffset=ypos))
                        if w.startswith("warper_generator"):
                            warperkey_child = WarperKey(t_diff/2 + last_t, self.key, last_v, v, self.scene, t)
                            new_warpkey_children.append(warperkey_child)
                        if t in splines[self.scene][self.key]:
                            knots = splines[self.scene][self.key][t]
                            for i in range(1, len(knots)+1):
                                knot_child = KnotKey(i*t_diff/(len(knots)+1) + last_t, self.key, i-1, self.scene, t)
                                new_knot_children.append(knot_child)
                    last_v, last_t = v, t

            elif isinstance(self.tag, tuple) and self.props_set is None and self.key is None:
                tag, layer = self.tag
                _all_keyframes = all_keyframes[self.scene]
                for p, d in transform_props:
                    for _, t, _ in _all_keyframes.get((tag, layer, p), []):
                        child = KeyFrame(insensitive_key_child, t, insensitive_key_hovere_child, False, key=None,
                            clicked=Function(change_time, t))
                        new_children.append(child)
            elif isinstance(self.tag, tuple) and self.props_set is not None:
                tag, layer = self.tag
                _all_keyframes = all_keyframes[self.scene]
                for p in self.props_set:
                    for _, t, _ in _all_keyframes.get((tag, layer, p), []):
                        child = KeyFrame(insensitive_key_child, t, insensitive_key_hovere_child, False, key=None,
                            clicked=Function(change_time, t))
                        new_children.append(child)
            elif isinstance(self.tag, tuple) and self.key is not None and not self.graphic_mode:
                for c in all_keyframes[self.scene].get(self.key, []):
                    _, t, _ = c
                    child = KeyFrame(key_child, t, key_hovere_child, key=self.key,
                        clicked=Function(change_time, t),
                        alternate=ShowAlternateMenu(
                            generate_menu(key=self.key, check_point=c, use_wide_range=self.use_wide_range,
                                change_func=self.changed, opened=self.opened, in_graphic_mode=self.in_graphic_mode),
                            style_prefix="_viewers_alternate_menu"))
                    new_children.append(child)
            elif isinstance(self.tag, tuple) and self.key is not None and self.graphic_mode:
                last_v, last_t = None, None
                is_force_plus = self.key[2] in force_plus
                for c in all_keyframes[self.scene].get(self.key, []):
                    v, t, w = c
                    child = KeyFrame(key_child, t, key_hovere_child, key=self.key, in_graphic_mode=True,
                        clicked=Function(change_time, t),
                        alternate=ShowAlternateMenu(
                            generate_menu(key=self.key, check_point=c, use_wide_range=self.use_wide_range,
                                change_func=self.changed, opened=self.opened, in_graphic_mode=self.in_graphic_mode),
                            style_prefix="_viewers_alternate_menu"))
                    new_children.append(child)

                    if last_v is not None:
                        v_diff = (v - last_v)
                        t_diff = (t - last_t)
                        for t2 in range(1, self.mark_num):
                            xpos = time_to_pos(last_t + t_diff*t2/self.mark_num)
                            ypos = time_and_key_to_pos(last_t + t_diff*t2/self.mark_num, self.key, is_force_plus)
                            box.add(Transform(interpolate_key_child, xoffset=xpos, yoffset=ypos))
                        if w.startswith("warper_generator"):
                            warperkey_child = WarperKey(t_diff/2 + last_t, self.key, last_v, v, self.scene, t)
                            new_warpkey_children.append(warperkey_child)
                        if t in splines[self.scene][self.key]:
                            knots = splines[self.scene][self.key][t]
                            for i in range(1, len(knots)+1):
                                knot_child = KnotKey(i*t_diff/(len(knots)+1) + last_t, self.key, i-1, self.scene, t)
                                new_knot_children.append(knot_child)
                    last_v, last_t = v, t

            elif self.tag == "sounds" and self.key is None:
                for channel, play_times in sound_keyframes.items():
                    for t in play_times:
                        child = KeyFrame(insensitive_key_child, t, insensitive_key_hovere_child, False, key=channel,
                            clicked=Function(change_time, t))
                        new_children.append(child)
            elif self.tag == "sounds" and self.key is not None:
                for t in sound_keyframes[self.key]:
                    child = KeyFrame(key_child, t, key_hovere_child, key=self.key, is_sound=True, 
                        clicked=Function(change_time, t),
                        alternate=ShowAlternateMenu(
                            generate_sound_menu(channel=self.key, time=t),
                            style_prefix="_viewers_alternate_menu"))
                    new_children.append(child)

            warpkey_children = []
            for new_c in new_warpkey_children:
                for old_c in self.warpkey_children:
                    if new_c == old_c:
                        warpkey_children.append(old_c)
                        box.add(old_c.get_child())
                        break
                else:
                    warpkey_children.append(new_c)
                    box.add(new_c.get_child())
            self.warpkey_children = warpkey_children

            knot_children = []
            for new_c in new_knot_children:
                for old_c in self.knot_children:
                    if new_c == old_c:
                        knot_children.append(old_c)
                        box.add(old_c.get_child())
                        break
                else:
                    knot_children.append(new_c)
                    box.add(new_c.get_child())
            self.knot_children = knot_children

            children = []
            for new_c in new_children:
                for old_c in self.children:
                    if new_c == old_c:
                        old_c.update(new_c)
                        children.append(old_c)
                        box.add(old_c.get_child())
                        break
                else:
                    children.append(new_c)
                    box.add(new_c.get_child())
            self.children = children

            render = box.render(width, height, st, at)
            return render


        def event(self, ev, x, y, st):
#すべてのイベントをオフにするとバーの問題は確認できない
            redraw = False
            for c in self.warpkey_children:
                rv = c.event(ev, x, y, st)
                if rv:
                    redraw = True
            for c in self.knot_children:
                rv = c.event(ev, x, y, st)
                if rv:
                    redraw = True
            for c in self.children:
                rv = c.event(ev, x, y, st)
                if rv:
                    redraw = True
#以降を飛すとバーの問題は確認できない
#背景をクリックしなくても問題は発生する
#グラフィックモードでのみ背景のイベントを飛しても問題は発生する
#背景のイベントをなくしても再描画が有効では問題発生
            self.background.event(ev, x, y, st)
#以降を飛ばしても問題は発生した
            if redraw:
                renpy.redraw(self, 0)


        def per_interact(self):
            if not playing:
                renpy.redraw(self, 0)


    class KeyFrame():


        def __init__(self, child, time, hover_child=None, draggable=True, key=None, clicked=None, alternate=None, in_graphic_mode=False, is_sound=False):
            from pygame import MOUSEMOTION, KMOD_CTRL, KMOD_SHIFT
            from pygame.key import get_mods
            from pygame.mouse import get_pressed
            self.child = child
            self.hover_child = hover_child
            self.time = time
            self.draggable = draggable
            self.key = key
            if not isinstance(clicked, list):
                clicked = [clicked]
            self.clicked = clicked + [QueueEvent("mouseup_1")]
            self.alternate = alternate
            self.in_graphic_mode = in_graphic_mode
            self.is_sound = is_sound

            self.dragging = False
            self.clicking = False
            self.last_hovered = self.hovered = False

            self.MOUSEMOTION = MOUSEMOTION
            self.speed = 1.0
            self.SLOW = 0.33
            self.NORMAL = 1.0
            self.FAST = 3.0
            self.KMOD_SHIFT = KMOD_SHIFT
            self.KMOD_CTRL = KMOD_CTRL
            self.get_mods = get_mods
            self.get_pressed = get_pressed

            self.barwidth = config.screen_width - c_box_size-50 - key_half_xsize
            if in_graphic_mode:
                self.barheight = config.screen_height*(1-preview_size)-time_column_height
            else:
                self.barheight = key_ysize
            self.width = key_xsize
            self.height = key_ysize
            if in_graphic_mode:
                self.yoffset = self.height/2.
            else:
                self.yoffset = 0
            if self.key is not None:
                if isinstance(self.key, tuple):
                    p = self.key[2]
                else:
                    p = self.key
                self.force_plus = p in force_plus


        def __eq__(self, other):
            # if not isinstance(other, KeyFrame):
            #     return False
            if self.child != other.child:
                return False
            if self.hover_child != other.hover_child:
                return False
            if self.draggable != other.draggable:
                return False
            if self.key != other.key:
                return False
            if self.in_graphic_mode != other.in_graphic_mode:
                return False
            if self.is_sound != other.is_sound:
                return False
            if self.time != other.time:
                return False
            return True


        def update(self, other):
            self.clicked = other.clicked
            self.alternate = other.alternate


        def get_child(self):
            if self.in_graphic_mode:
                self.xpos = time_to_pos(self.time)
                self.ypos = time_and_key_to_pos(self.time, self.key, self.force_plus)
                anchor = (0.5, 0.5)
            else:
                self.xpos = time_to_pos(self.time)
                self.ypos = 0.
                anchor = (0.5, 0.0)
            if self.hovered:
                child = self.hover_child
            else:
                child = self.child
            return Transform(child, xoffset=self.xpos, yoffset=self.ypos, anchor=anchor)


        def event(self, ev, x, y, st):
            clicking, _, _ = self.get_pressed()
            if not clicking and self.dragging:
                self.dragging = False
                self.clicking = False
                self.last_xpos = self.xpos
                self.last_ypos = self.ypos
                self.last_x = None
                self.last_y = None

            if self.draggable and ev.type == self.MOUSEMOTION and self.clicking:
                self.dragging = True
                to_x = (x - self.last_x)*self.speed + self.last_xpos
                pos = to_x
                if self.in_graphic_mode:
                    to_y = (y - self.last_y)*self.speed + self.last_ypos
                    pos = (to_x, to_y)
                last_time = self.time
                self.time = key_drag_changed(pos, self.key, self.time, \
                    is_sound=self.is_sound, in_graphic_mode=self.in_graphic_mode)

            self.hovered = False
            if not self.dragging and \
                x >= self.xpos - self.width/2. and x <= self.width/2.+self.xpos and \
                y >= self.ypos - self.yoffset and y <= self.height - self.yoffset +self.ypos:
                self.hovered = True
                if renpy.map_event(ev, "mousedown_1") and not out_of_viewport():
                    if self.get_mods() & self.KMOD_CTRL:
                        self.speed = self.SLOW
                    elif self.get_mods() & self.KMOD_SHIFT:
                        self.speed = self.FAST
                    else:
                        self.speed = self.NORMAL
                    self.clicking = True
                    self.last_xpos = self.xpos
                    self.last_ypos = self.ypos
                    self.last_x = x
                    self.last_y = y
                    raise renpy.display.core.IgnoreEvent()
                elif not self.dragging and renpy.map_event(ev, "mouseup_1"):
                    if self.clicking == True:
                        self.clicking = False
                        rv = renpy.run(self.clicked)
                        if rv is not None:
                            return rv
                        raise renpy.display.core.IgnoreEvent()
                elif renpy.map_event(ev, "button_alternate"):
                    rv = renpy.run(self.alternate)
                    if rv is not None:
                        return rv
                    raise renpy.display.core.IgnoreEvent()
            elif self.clicking and renpy.map_event(ev, "mouseup_1"):
                self.dragging = False
                self.clicking = False
                self.last_xpos = self.xpos
                self.last_ypos = self.ypos
                self.last_x = None
                self.last_y = None
                raise renpy.display.core.IgnoreEvent()
            if self.last_hovered != self.hovered:
                self.last_hovered = self.hovered
                return True
            self.last_hovered = self.hovered



    class WarperKey():


        def __init__(self, time, key, last_v, v, scene, key_time):
            from pygame import MOUSEMOTION, KMOD_CTRL, KMOD_SHIFT
            from pygame.key import get_mods
            from pygame.mouse import get_pressed
            self.child = warperkey_child
            self.hover_child = warperkey_hovere_child
            self.time = time
            self.key = key
            self.last_v = last_v
            self.v = v
            self.scene = scene
            self.key_time = key_time

            self.dragging = False
            self.clicking = False
            self.last_hovered = self.hovered = False

            self.MOUSEMOTION = MOUSEMOTION
            self.get_pressed = get_pressed

            self.barwidth = config.screen_width - c_box_size-50 - key_half_xsize
            self.barheight = config.screen_height*(1-preview_size)-time_column_height
            self.width = key_xsize
            self.height = key_ysize
            self.yoffset = self.height/2.

            self.key_list = [key]
            if isinstance(key, tuple):
                n, l, p = key
                for gn, ps in props_groups.items():
                    if p in ps:
                        self.key_list = [(n, l, p) for p in props_groups[gn]]
                self.force_plus = p in force_plus
            else:
                for gn, ps in props_groups.items():
                    if key in ps:
                        if gn != "focusing":
                            self.key_list = props_groups[gn]
                self.force_plus = key in force_plus

            if is_wide_range(key):
                self.range = persistent._graphic_editor_wide_range
            else:
                self.range = persistent._graphic_editor_narrow_range


        def __eq__(self, other):
            # if not isinstance(other, WarperKey):
            #     return False
            if self.key != other.key:
                return False
            if self.time != other.time:
                return False
            return True


        def get_child(self):
            self.xpos = time_to_pos(self.time)
            self.ypos = time_and_key_to_pos(self.time, self.key, self.force_plus)
            anchor = (0.5, 0.5)
            if self.hovered:
                child = self.hover_child
            else:
                child = self.child
            return Transform(child, xoffset=self.xpos, yoffset=self.ypos, anchor=anchor)


        def event(self, ev, x, y, st):
            clicking, _, _ = self.get_pressed()
            if not clicking and self.dragging:
                self.dragging = False
                self.clicking = False

            if ev.type == self.MOUSEMOTION and self.clicking:
                self.dragging = True
                last_time = self.time
                self.warperkey_drag_changed(y)
                return True

            self.hovered = False
            if not self.dragging and \
                x >= self.xpos - self.width/2. and x <= self.width/2.+self.xpos and \
                y >= self.ypos - self.yoffset and y <= self.height - self.yoffset +self.ypos:
                self.hovered = True
                if renpy.map_event(ev, "mousedown_1") and not out_of_viewport():
                    self.clicking = True
                    raise renpy.display.core.IgnoreEvent()
                elif not self.dragging and renpy.map_event(ev, "mouseup_1"):
                    self.clicking = False
                    raise renpy.display.core.IgnoreEvent()
            elif self.clicking and renpy.map_event(ev, "mouseup_1"):
                self.dragging = False
                self.clicking = False
                raise renpy.display.core.IgnoreEvent()
            if self.last_hovered != self.hovered:
                self.last_hovered = self.hovered
                return True
            self.last_hovered = self.hovered


        def warperkey_drag_changed(self, y):
            bottom_pos = value_to_pos(self.last_v, self.range, self.force_plus)
            top_pos = value_to_pos(self.v, self.range, self.force_plus)
            if top_pos < bottom_pos:
                top_pos, bottom_pos = bottom_pos, top_pos
            if y >= top_pos:
                y = top_pos
            if y <= bottom_pos:
                y = bottom_pos
            if (top_pos - bottom_pos) == 0:
                k = 0.5
            elif self.v > self.last_v:
                k = (float(y) - bottom_pos) / (top_pos - bottom_pos) 
            else:
                k = 1 - (float(y) - bottom_pos) / (top_pos - bottom_pos) 
            for i, (_, t, _) in enumerate(all_keyframes[self.scene][self.key]):
                if t == self.key_time:
                    break
            for key in self.key_list:
                v, t, w = all_keyframes[self.scene][key][i]
                all_keyframes[self.scene][key][i] = (v, t, "warper_generator([(1, 1, {:.2})])".format(k))
            renpy.restart_interaction()


    class KnotKey():


        def __init__(self, time, key, knot_num, scene, key_time):
            from pygame import MOUSEMOTION, KMOD_CTRL, KMOD_SHIFT
            from pygame.key import get_mods
            from pygame.mouse import get_pressed
            self.child = knot_child
            self.hover_child = knot_hovere_child
            self.time = time
            self.key = key
            self.knot_num = knot_num
            self.scene = scene
            self.key_time = key_time

            self.dragging = False
            self.clicking = False
            self.last_hovered = self.hovered = False

            self.MOUSEMOTION = MOUSEMOTION
            self.get_pressed = get_pressed

            self.barwidth = config.screen_width - c_box_size-50 - key_half_xsize
            self.barheight = config.screen_height*(1-preview_size)-time_column_height
            self.width = key_xsize
            self.height = key_ysize
            self.yoffset = self.height/2.

            # self.key_list = [key]
            if isinstance(key, tuple):
                n, l, p = key
                # for gn, ps in props_groups.items():
                #     if p in ps:
                #         self.key_list = [(n, l, p) for p in props_groups[gn]]
                self.force_plus = p in force_plus
            else:
                # for gn, ps in props_groups.items():
                #     if key in ps:
                #         if gn != "focusing":
                #             self.key_list = props_groups[gn]
                self.force_plus = key in force_plus

            if is_wide_range(key):
                self.range = persistent._graphic_editor_wide_range
            else:
                self.range = persistent._graphic_editor_narrow_range


        def __eq__(self, other):
            # if not isinstance(other, WarperKey):
            #     return False
            if self.key != other.key:
                return False
            if self.time != other.time:
                return False
            if self.knot_num != other.knot_num:
                return False
            if self.scene != other.scene:
                return False
            if self.key_time != other.key_time:
                return False
            return True


        def get_child(self):
            self.xpos = time_to_pos(self.time)
            self.ypos = self.knot_num_to_pos()
            anchor = (0.5, 0.5)
            if self.hovered:
                child = self.hover_child
            else:
                child = self.child
            return Transform(child, xoffset=self.xpos, yoffset=self.ypos, anchor=anchor)


        def knot_num_to_pos(self):
            knots = splines[self.scene][self.key][self.key_time]
            knot = knots[self.knot_num]
            return value_to_pos(knot, self.range, self.force_plus)


        def knot_drag_changed(self, y):
            v = pos_to_value(y, is_wide_range(self.key), self.force_plus)
            if isinstance(v, float):
                v = round(v, 2)
            splines[self.scene][self.key][self.key_time][self.knot_num] = v
            renpy.restart_interaction()


        def event(self, ev, x, y, st):
            clicking, _, _ = self.get_pressed()
            if not clicking and self.dragging:
                self.dragging = False
                self.clicking = False

            if ev.type == self.MOUSEMOTION and self.clicking:
                self.dragging = True
                self.knot_drag_changed(y)
                return True

            self.hovered = False
            if not self.dragging and \
                x >= self.xpos - self.width/2. and x <= self.width/2.+self.xpos and \
                y >= self.ypos - self.yoffset and y <= self.height - self.yoffset +self.ypos:
                self.hovered = True
                if renpy.map_event(ev, "mousedown_1") and not out_of_viewport():
                    self.clicking = True
                    raise renpy.display.core.IgnoreEvent()
                elif not self.dragging and renpy.map_event(ev, "mouseup_1"):
                    self.clicking = False
                    raise renpy.display.core.IgnoreEvent()
            elif self.clicking and renpy.map_event(ev, "mouseup_1"):
                self.dragging = False
                self.clicking = False
                raise renpy.display.core.IgnoreEvent()
            if self.last_hovered != self.hovered:
                self.last_hovered = self.hovered
                return True
            self.last_hovered = self.hovered


    class TimeLineBackground():


        def __init__(self, key=None, in_graphic_mode=False):
            from pygame import MOUSEMOTION
            from pygame.mouse import get_pressed
            from renpy.store import Function, Solid, Fixed
            self.key = key
            # self.scene = scene
            self.in_graphic_mode = in_graphic_mode

            self.key_list = [key]
            if isinstance(key, tuple):
                n, l, p = key
                for gn, ps in props_groups.items():
                    if p in ps:
                        self.key_list = [(n, l, p) for p in props_groups[gn]]
                self.force_plus = p in force_plus
            else:
                for gn, ps in props_groups.items():
                    if key in ps:
                        if gn != "focusing":
                            self.key_list = props_groups[gn]
                self.force_plus = key in force_plus

            if in_graphic_mode:
                self.width  = config.screen_width-c_box_size-50-key_half_xsize
                self.height = int(config.screen_height*(1-preview_size)-time_column_height-key_ysize-10)
                self.xpos = key_half_xsize
                self.ypos = key_half_ysize
            else:
                self.width  = config.screen_width-c_box_size-50-key_half_xsize
                self.height = key_ysize
                self.xpos = key_half_xsize
                self.ypos = 0
            self.child = Solid(time_line_background_color, xsize=self.width, ysize=self.height,  xoffset=self.xpos, yoffset=self.ypos)

            self.MOUSEMOTION = MOUSEMOTION
            self.get_pressed = get_pressed

            self.dragging = False
            self.clicking = False
            self.hovered = False
            self.mark_num = 100


        def __eq__(self, other):
            # if not isinstance(other, TimeLineBackground):
            #     return False
            if self.key != other.key or self.in_graphic_mode != other.in_graphic_mode:
                return False
            return True


        def get_child(self):
            return self.child


        def event(self, ev, x, y, st):
            clicking, _, _ = self.get_pressed()
            if not clicking and self.dragging:
                self.dragging = False
                self.clicking = False

            if ev.type == self.MOUSEMOTION and self.clicking:
                self.dragging = True

            self.hovered = False
            if not self.dragging and x >= self.xpos and x <= self.width + self.xpos \
                and y >= self.ypos and y <= self.height + self.ypos:
                self.hovered = True
                if renpy.map_event(ev, "mousedown_1") and not out_of_viewport():
                    self.clicking = True
                    raise renpy.display.core.IgnoreEvent()
                elif not self.dragging and renpy.map_event(ev, "mouseup_1"):
                    if self.clicking == True:
                        self.clicking = False
                        time = pos_to_time(x)
                        change_time(time)
                        raise renpy.display.core.IgnoreEvent()
                elif renpy.map_event(ev, "button_alternate"):
                    if self.key:
                        if self.in_graphic_mode:
                            time = pos_to_time(x)
                            use_wide_range = is_wide_range(self.key)
                            value = pos_to_value(y, use_wide_range, self.force_plus)
                            generate_changed(self.key)(to_changed_value(value, self.force_plus, use_wide_range), time)
                        else:
                            time = pos_to_time(x)
                            reset(self.key_list, time)
                        raise renpy.display.core.IgnoreEvent()
            elif self.clicking and renpy.map_event(ev, "mouseup_1"):
                self.dragging = False
                self.clicking = False


    class ImagePins(renpy.Displayable):

        def __init__(self):
            super(ImagePins, self).__init__()
            from pygame import MOUSEMOTION
            from renpy.store import Fixed
            if aspect_16_9():
                self.xpos = int(config.screen_width * (1 - preview_size) / 2)
                self.ypos = 0
            else:
                self.xpos = 0
                self.ypos = 0
            self.width = int(preview_size*config.screen_width)
            self.height = int(preview_size*config.screen_height)

            self.children = []
            self.camera_children = []
            self.mark_num = 20


        def __eq__(self, other):
            if not isinstance(other, ImagePins):
                return False
            return True


        def render(self, width, height, st, at):
            new_children = []
            box = Fixed()

            for l in ["master"]:
                state = get_image_state(l)
                for tag in state:
                    ks = self.get_image_keyframes(tag, l)
                    if not ks or (current_time not in ks and ks[-1] > current_time):
                        child = ImagePin(tag, l, current_scene, current_time)
                        new_children.append(child)
                    last_t = None
                    for t in ks:
                        child = ImagePin(tag, l, current_scene, t)
                        new_children.append(child)
                        if last_t is not None:
                            t_diff = (t - last_t)
                            for i in range(1, self.mark_num):
                                box.add(ImageInterpolate(tag, l, current_scene, (i * (t - last_t) / self.mark_num)+last_t).get_child())
                        last_t = t

            children = []
            for new_c in new_children:
                for old_c in self.children:
                    if new_c == old_c:
                        old_c.update(new_c)
                        children.append(old_c)
                        box.add(old_c.get_child())
                        break
                else:
                    children.append(new_c)
                    box.add(new_c.get_child())
            self.children = children

            new_children = []
            ks = self.get_camera_keyframes()
            if not ks or (current_time not in ks and ks[-1] > current_time):
                child = CameraPin(current_scene, current_time)
                new_children.append(child)
            last_t = None
            for t in ks:
                child = CameraPin(current_scene, t)
                new_children.append(child)
                if last_t is not None:
                    for i in range(1, self.mark_num):
                        box.add(CameraInterpolate(current_scene, (i * (t - last_t) / self.mark_num) + last_t).get_child())
                last_t = t

            camera_children = []
            for new_c in new_children:
                for old_c in self.camera_children:
                    if new_c == old_c:
                        old_c.update(new_c)
                        camera_children.append(old_c)
                        box.add(old_c.get_child())
                        break
                else:
                    camera_children.append(new_c)
                    box.add(new_c.get_child())
            self.camera_children = camera_children

            render = box.render(width, height, st, at)
            return render


        def event(self, ev, x, y, st):
            redraw = False
            for c in self.children:
                rv = c.event(ev, x, y, st)
                if rv:
                    redraw = True
            for c in self.camera_children:
                rv = c.event(ev, x, y, st)
                if rv:
                    redraw = True
            if rv:
                redraw = True
            if redraw:
                renpy.redraw(self, 0)


        def per_interact(self):
            if not playing:
                renpy.redraw(self, 0)


        def get_image_keyframes(self, tag, layer):
            result = set()
            for p in ["xpos", "ypos", "zpos"]:
                if (tag, layer, p) not in all_keyframes[current_scene]:
                    continue
                else:
                    for _, t, _ in all_keyframes[current_scene][(tag, layer, p)]:
                        result.add(t)
            
            return sorted(list(result))


        def get_camera_keyframes(self):
            result = set()
            for p in ["xpos", "ypos", "zpos"]:
                if p not in all_keyframes[current_scene]:
                    continue
                else:
                    for _, t, _ in all_keyframes[current_scene][p]:
                        result.add(t)
            return sorted(tuple(result))


    class ImageInterpolate():


        def __init__(self, tag, layer, scene_num, time):
            self.tag = tag
            self.layer = layer
            self.scene_num = scene_num
            self.time = time

            self.barwidth = config.screen_width - c_box_size-50 - key_half_xsize
            self.barheight = config.screen_height*(1-preview_size)-time_column_height


            self.width = 6
            self.height = 6
            box = Fixed(xsize=self.width, ysize=self.height)
            box.add(Solid("#AAA",xsize=self.width, ysize=self.height))
            box.add(Solid("#333",xpos=1, ypos=1, xsize=self.width-2, ysize=self.height-2))
            self.child =box


        def value_to_pos(self):
            xpos = get_value((self.tag, self.layer, "xpos"), self.time, True, self.scene_num)
            if isinstance(xpos, float):
                xpos *= config.screen_width
            xpos *= preview_size

            ypos = get_value((self.tag, self.layer, "ypos"), self.time, True, self.scene_num)
            if isinstance(ypos, float):
                ypos *= config.screen_height
            ypos *= preview_size

            return (xpos, ypos)


        def get_child(self):
            self.xpos, self.ypos = self.value_to_pos()
            anchor = (0.5, 0.5)
            return Transform(self.child, xoffset=self.xpos, yoffset=self.ypos, anchor=anchor)


    class ImagePin(ImageInterpolate):


        def __init__(self, tag, layer, scene_num, time):
            super(ImagePin, self).__init__(tag, layer, scene_num, time)
            from pygame import MOUSEMOTION, KMOD_CTRL, KMOD_SHIFT, KMOD_ALT
            from pygame.key import get_mods
            from pygame.mouse import get_pressed
            from renpy.store import Show, QueueEvent, Function, NullAction
            self.tag = tag
            self.layer = layer
            self.scene_num = scene_num
            self.time = time

            self.clicked = [Show("_new_action_editor", opened={scene_num:[tag, (tag, layer, "Child/Pos    ")]}), Function(change_time, time)] + [QueueEvent("mouseup_1")]
            self.draggable = scene_num == current_scene

            if self.draggable:
                xpos   = get_value((tag, layer, "xpos"), time, True, self.scene_num)
                if isinstance(xpos, float):
                    xpos = round(xpos, 2)
                ypos   = get_value((tag, layer, "ypos"), time, True, self.scene_num)
                if isinstance(ypos, float):
                    ypos = round(ypos, 2)
                zpos   = get_value((tag, layer, "zpos"), time, True, self.scene_num)
                if isinstance(zpos, float):
                    zpos = round(zpos, 2)
                rotate = get_value((tag, layer, "rotate"), time, True, self.scene_num)
                if isinstance(rotate, float):
                    rotate = round(rotate, 2)
                self.x_changed = generate_changed((self.tag, self.layer, "xpos"))
                self.y_changed = generate_changed((self.tag, self.layer, "ypos"))
                self.z_changed = generate_changed((self.tag, self.layer, "zpos"))
                self.r_changed = generate_changed((self.tag, self.layer, "rotate"))
                self.alternate = ShowAlternateMenu(
                        [("{}".format(tag), NullAction()),
                        ("edit: xpos {}".format(xpos), 
                         [Function(edit_value, self.x_changed, is_wide_range((tag, layer, "xpos")), xpos, "xpos" in force_plus, time), Function(change_time, time)]),
                        ("edit: ypos {}".format(ypos),
                         [Function(edit_value, self.y_changed, is_wide_range((tag, layer, "ypos")), ypos, "ypos" in force_plus, time), Function(change_time, time)]),
                        ("edit: zpos {}".format(zpos),
                         [Function(edit_value, self.z_changed, is_wide_range((tag, layer, "zpos")), zpos, "zpos" in force_plus, time), Function(change_time, time)]),
                        ("edit: rotate {}".format(rotate), 
                         [Function(edit_value, self.r_changed, is_wide_range((tag, layer, "rotate")), rotate, "rotate" in force_plus, time), Function(change_time, time)])],
                        style_prefix="_viewers_alternate_menu")

            self.dragging = False
            self.clicking = False
            self.last_hovered = self.hovered = False

            self.MOUSEMOTION = MOUSEMOTION
            self.KMOD_SHIFT = KMOD_SHIFT
            self.KMOD_CTRL = KMOD_CTRL
            self.KMOD_ALT = KMOD_ALT
            self.get_mods = get_mods
            self.get_pressed = get_pressed

            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#07A", xsize=16, ysize=16))
            box.add(Solid("#0CF", align=(.5, .5), xsize=14, ysize=14))
            self.current_child = Transform(rotate=45)(box)
            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#09A", xsize=16, ysize=16))
            box.add(Solid("#2EF", align=(.5, .5), xsize=14, ysize=14))
            self.current_hover_child = Transform(rotate=45)(box)
            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#047", xsize=16, ysize=16))
            box.add(Solid("#09B", align=(.5, .5), xsize=14, ysize=14))
            self.current_other_child = Transform(rotate=45)(box)
            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#078", xsize=16, ysize=16))
            box.add(Solid("#2BC", align=(.5, .5), xsize=14, ysize=14))
            self.current_other_hover_child = Transform(rotate=45)(box)
            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#059", xsize=16, ysize=16))
            box.add(Solid("#09C", align=(.5, .5), xsize=14, ysize=14))
            self.child = Transform(rotate=45)(box)
            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#078", xsize=16, ysize=16))
            box.add(Solid("#2BE", align=(.5, .5), xsize=14, ysize=14))
            self.hover_child = Transform(rotate=45)(box)
            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#014", xsize=16, ysize=16))
            box.add(Solid("#069", align=(.5, .5), xsize=14, ysize=14))
            self.other_child = Transform(rotate=45)(box)
            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#037", xsize=16, ysize=16))
            box.add(Solid("#28B", align=(.5, .5), xsize=14, ysize=14))
            self.other_hover_child = Transform(rotate=45)(box)

            self.width = key_xsize
            self.height = key_ysize


        def __eq__(self, other):
            if self.tag != other.tag:
                return False
            if self.layer != other.layer:
                return False
            if self.scene_num != other.scene_num:
                return False
            if self.time != other.time:
                return False
            if self.draggable != other.draggable:
                return False
            return True


        def update(self, other):
            self.alternate = other.alternate


        def get_child(self):
            self.xpos, self.ypos = self.value_to_pos()
            anchor = (0.5, 0.5)
            if self.hovered:
                if self.scene_num == current_scene:
                    if current_time == self.time:
                        child = self.current_hover_child
                    else:
                        child = self.hover_child
                else:
                    if current_time == self.time:
                        child = self.current_other_scene_hover_child
                    else:
                        child = self.other_scene_hover_child
            else:
                if self.scene_num == current_scene:
                    if current_time == self.time:
                        child = self.current_child
                    else:
                        child = self.child
                else:
                    if current_time == self.time:
                        child = self.current_other_scene_child
                    else:
                        child = self.other_scene_child
            return Transform(child, xoffset=self.xpos, yoffset=self.ypos, anchor=anchor)


        def pos_to_value(self, x, y):
            state = get_image_state(self.layer, self.scene_num)[self.tag]
            r = sqrt((x - self.last_x)**2 + (y - self.last_y)**2)
            if x - self.last_x >= 0:
                r *= -1
            if isinstance(self.last_zpos, int):
                z = int(r)
            else:
                z = round(r, 2)
            if isinstance(self.last_rotate, int):
                r = int(r)
            else:
                r = round(r, 2)

            if "xpos" in state:
                xpos_org = state["xpos"]
            else:
                xpos_org = get_default("xpos")
            x /= preview_size
            if isinstance(xpos_org, int):
                x = int(x)
            else:
                x /= config.screen_width

            if "ypos" in state:
                ypos_org = state["ypos"]
            else:
                ypos_org = get_default("ypos")
            y /= preview_size
            if isinstance(ypos_org, int):
                y = int(y)
            else:
                y /= config.screen_height


            mods = self.get_mods()
            if mods & self.KMOD_SHIFT and mods & self.KMOD_CTRL:
                self.r_changed(to_changed_value(z+self.last_rotate, "rotate" in force_plus, is_wide_range((self.tag, self.layer, "rotate"))))
            elif mods & self.KMOD_CTRL:
                self.y_changed(to_changed_value(y, "ypos" in force_plus, is_wide_range((self.tag, self.layer, "ypos"))))
            elif mods & self.KMOD_SHIFT:
                self.x_changed(to_changed_value(x, "xpos" in force_plus, is_wide_range((self.tag, self.layer, "xpos"))))
            elif mods & self.KMOD_ALT:
                self.z_changed(to_changed_value(z+self.last_zpos, "zpos" in force_plus, is_wide_range((self.tag, self.layer, "zpos"))))
            else:
                self.x_changed(to_changed_value(x, "xpos" in force_plus, is_wide_range((self.tag, self.layer, "xpos"))))
                self.y_changed(to_changed_value(y, "ypos" in force_plus, is_wide_range((self.tag, self.layer, "ypos"))))


        def event(self, ev, x, y, st):
            clicking, _, _ = self.get_pressed()
            if not clicking and self.dragging:
                self.dragging = False
                self.clicking = False
                self.last_x = None
                self.last_y = None
                self.last_zpos = None
                self.last_rotate = None

            if self.draggable and ev.type == self.MOUSEMOTION and self.clicking:
                self.dragging = True
                self.pos_to_value(x, y)
                

            self.hovered = False
            if not self.dragging and \
                x >= self.xpos - self.width/2. and x <= self.width/2.+self.xpos and \
                y >= self.ypos - self.height/2. and y <= self.height/2.+self.ypos and \
                self.xpos + self.width/2. > 0 and self.xpos - self.width/2. < config.screen_width * preview_size and \
                self.ypos + self.height/2. > 0 and self.ypos - self.height/2. < config.screen_height * preview_size:
                self.hovered = True
                if renpy.map_event(ev, "mousedown_1"):
                    self.clicking = True
                    self.last_x = x
                    self.last_y = y
                    self.last_zpos = get_value((self.tag, self.layer, "zpos"), time=self.time, scene_num=self.scene_num)
                    self.last_rotate = get_value((self.tag, self.layer, "rotate"), time=self.time, default=True, scene_num=self.scene_num)
                    raise renpy.display.core.IgnoreEvent()
                elif not self.dragging and renpy.map_event(ev, "mouseup_1"):
                    if self.clicking == True:
                        self.clicking = False
                        rv = renpy.run(self.clicked)
                        if rv is not None:
                            return rv
                        raise renpy.display.core.IgnoreEvent()
                elif renpy.map_event(ev, "button_alternate"):
                    rv = renpy.run(self.alternate)
                    if rv is not None:
                        return rv
                    raise renpy.display.core.IgnoreEvent()
            elif self.clicking and renpy.map_event(ev, "mouseup_1"):
                self.dragging = False
                self.clicking = False
                self.last_x = None
                self.last_y = None
                self.last_zpos = None
                self.last_rotate = None
                raise renpy.display.core.IgnoreEvent()
            if self.last_hovered != self.hovered:
                self.last_hovered = self.hovered
                return True
            self.last_hovered = self.hovered


    class CameraInterpolate():


        def __init__(self, scene_num, time):
            self.scene_num = scene_num
            self.time = time

            self.barwidth = config.screen_width - c_box_size-50 - key_half_xsize
            self.barheight = config.screen_height*(1-preview_size)-time_column_height

            self.width = 6
            self.height = 6
            box = Fixed(xsize=self.width, ysize=self.height)
            box.add(Solid("#AAA",xsize=self.width, ysize=self.height))
            box.add(Solid("#333",xpos=1, ypos=1, xsize=self.width-2, ysize=self.height-2))
            self.child = box
            self.xoffset = int(preview_size * config.screen_width / 2)
            self.yoffset = int(preview_size * config.screen_height / 2)


        def value_to_pos(self):
            xpos = get_value("xpos", self.time, True, self.scene_num)
            if isinstance(xpos, float):
                xpos *= config.screen_width
            xpos *= preview_size
            xpos += self.xoffset

            ypos = get_value("ypos", self.time, True, self.scene_num)
            if isinstance(ypos, float):
                ypos *= config.screen_height
            ypos *= preview_size
            ypos += self.yoffset

            return (xpos, ypos)


        def get_child(self):
            self.xpos, self.ypos = self.value_to_pos()
            anchor = (0.5, 0.5)
            return Transform(self.child, xoffset=self.xpos, yoffset=self.ypos, anchor=anchor)


    class CameraPin(CameraInterpolate):


        def __init__(self, scene_num, time):
            super(CameraPin, self).__init__(scene_num, time)
            from pygame import MOUSEMOTION, KMOD_CTRL, KMOD_SHIFT, KMOD_ALT
            from pygame.key import get_mods
            from pygame.mouse import get_pressed
            from renpy.store import Show, QueueEvent, Function, NullAction
            self.scene_num = scene_num
            self.time = time

            self.clicked = [Show("_new_action_editor", opened={scene_num:["camera", "Child/Pos    "]}), Function(change_time, time)] + [QueueEvent("mouseup_1")]
            self.draggable = scene_num == current_scene
            if self.draggable:
                self.x_changed = generate_changed("xpos")
                self.y_changed = generate_changed("ypos")
                self.z_changed = generate_changed("zpos")
                self.r_changed = generate_changed("rotate")
                xpos   = get_value("xpos", time, True, self.scene_num)
                if isinstance(xpos, float):
                    xpos = round(xpos, 2)
                ypos   = get_value("ypos", time, True, self.scene_num)
                if isinstance(ypos, float):
                    ypos = round(ypos, 2)
                zpos   = get_value("zpos", time, True, self.scene_num)
                if isinstance(zpos, float):
                    zpos = round(zpos, 2)
                rotate = get_value("rotate", time, True, self.scene_num)
                if isinstance(rotate, float):
                    rotate = round(rotate, 2)
                self.alternate = ShowAlternateMenu([
                        ("camera", NullAction()),
                        ("edit: xpos {}".format(xpos), 
                         [Function(edit_value, self.x_changed, is_wide_range("xpos"), xpos, "xpos" in force_plus, time), Function(change_time, time)]),
                        ("edit: ypos {}".format(ypos),
                         [Function(edit_value, self.y_changed, is_wide_range("ypos"), ypos, "ypos" in force_plus, time), Function(change_time, time)]),
                        ("edit: zpos {}".format(zpos),
                         [Function(edit_value, self.z_changed, is_wide_range("zpos"), zpos, "zpos" in force_plus, time), Function(change_time, time)]),
                        ("edit: rotate {}".format(rotate), 
                         [Function(edit_value, self.r_changed, is_wide_range("rotate"), rotate, "rotate" in force_plus, time), Function(change_time, time)])],
                        style_prefix="_viewers_alternate_menu")

            self.dragging = False
            self.clicking = False
            self.last_hovered = self.hovered = False

            self.MOUSEMOTION = MOUSEMOTION
            self.KMOD_SHIFT = KMOD_SHIFT
            self.KMOD_CTRL = KMOD_CTRL
            self.KMOD_ALT = KMOD_ALT
            self.get_mods = get_mods
            self.get_pressed = get_pressed

            self.current_child = Transform(rotate=45)(Solid("#222", xsize=16, ysize=16))
            self.current_hover_child = Transform(rotate=45)(Solid("#555", xsize=16, ysize=16))
            self.child = Transform(rotate=45)(Solid("#444", xsize=16, ysize=16))
            self.hover_child = Transform(rotate=45)(Solid("#666", xsize=16, ysize=16))

            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#555", xsize=16, ysize=16))
            box.add(Solid("#222", align=(.5, .5), xsize=14, ysize=14))
            self.current_child = Transform(rotate=45)(box)
            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#888", xsize=16, ysize=16))
            box.add(Solid("#555", align=(.5, .5), xsize=14, ysize=14))
            self.current_hover_child = Transform(rotate=45)(box)

            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#777", xsize=16, ysize=16))
            box.add(Solid("#444", align=(.5, .5), xsize=14, ysize=14))
            self.child = Transform(rotate=45)(box)
            box = Fixed(xsize=16,ysize=16)
            box.add(Solid("#999", xsize=16, ysize=16))
            box.add(Solid("#666", align=(.5, .5), xsize=14, ysize=14))
            self.hover_child = Transform(rotate=45)(box)

            self.width = key_xsize
            self.height = key_ysize


        def __eq__(self, other):
            if self.scene_num != other.scene_num:
                return False
            if self.time != other.time:
                return False
            if self.draggable != other.draggable:
                return False
            return True


        def update(self, other):
            self.alternate = other.alternate


        def get_child(self):
            self.xpos, self.ypos = self.value_to_pos()
            anchor = (0.5, 0.5)
            if self.hovered:
                if self.scene_num == current_scene:
                    if self.time == current_time:
                        child = self.current_hover_child
                    else:
                        child = self.hover_child
                # else:
                #     child = self.other_scene_hover_child
            else:
                if self.scene_num == current_scene:
                    if self.time == current_time:
                        child = self.current_child
                    else:
                        child = self.child
                # else:
                #     child = self.other_scene_child
            return Transform(child, xoffset=self.xpos, yoffset=self.ypos, anchor=anchor)


        def pos_to_value(self, x, y):
            state = camera_state_org[self.scene_num]
            r = sqrt((x - self.last_x)**2 + (y - self.last_y)**2)
            if x - self.last_x >= 0:
                r *= -1
            if isinstance(self.last_zpos, int):
                z = int(r)
            else:
                z = round(r, 2)
            if isinstance(self.last_rotate, int):
                r = int(r)
            else:
                r = round(r, 2)

            x -= self.xoffset
            if "xpos" in state:
                xpos_org = state["xpos"]
            else:
                xpos_org = get_default("xpos", True)
            x /= preview_size
            if isinstance(xpos_org, int):
                x = int(x)
            else:
                x /= config.screen_width

            y -= self.yoffset
            if "ypos" in state:
                ypos_org = state["ypos"]
            else:
                ypos_org = get_default("ypos", True)
            y /= preview_size
            if isinstance(ypos_org, int):
                y = int(y)
            else:
                y /= config.screen_height


            mods = self.get_mods()
            if mods & self.KMOD_SHIFT and mods & self.KMOD_CTRL:
                self.r_changed(to_changed_value(z+self.last_rotate, "rotate" in force_plus, is_wide_range("rotate")))
            elif mods & self.KMOD_CTRL:
                self.y_changed(to_changed_value(y, "ypos" in force_plus, is_wide_range("ypos")))
            elif mods & self.KMOD_SHIFT:
                self.x_changed(to_changed_value(x, "xpos" in force_plus, is_wide_range("xpos")))
            elif mods & self.KMOD_ALT:
                self.z_changed(to_changed_value(z+self.last_zpos, "zpos" in force_plus, is_wide_range("zpos")))
            else:
                self.x_changed(to_changed_value(x, "xpos" in force_plus, is_wide_range("xpos")))
                self.y_changed(to_changed_value(y, "ypos" in force_plus, is_wide_range("ypos")))


        def event(self, ev, x, y, st):
            clicking, _, _ = self.get_pressed()
            if not clicking and self.dragging:
                self.dragging = False
                self.clicking = False
                self.last_x = None
                self.last_y = None
                self.last_zpos = None
                self.last_rotate = None

            if self.draggable and ev.type == self.MOUSEMOTION and self.clicking:
                self.dragging = True
                self.pos_to_value(x, y)

            self.hovered = False
            if not self.dragging and \
                x >= self.xpos - self.width/2. and x <= self.width/2.+self.xpos and \
                y >= self.ypos - self.height/2. and y <= self.height/2.+self.ypos and \
                self.xpos + self.width/2. > 0 and self.xpos - self.width/2. < config.screen_width * preview_size and \
                self.ypos + self.height/2. > 0 and self.ypos - self.height/2. < config.screen_height * preview_size:
                self.hovered = True
                if renpy.map_event(ev, "mousedown_1"):
                    self.clicking = True
                    self.last_x = x
                    self.last_y = y
                    self.last_zpos = get_value("zpos", default=True, scene_num=self.scene_num)
                    self.last_rotate = get_value("rotate", default=True, scene_num=self.scene_num)
                    raise renpy.display.core.IgnoreEvent()
                elif not self.dragging and renpy.map_event(ev, "mouseup_1"):
                    if self.clicking == True:
                        self.clicking = False
                        rv = renpy.run(self.clicked)
                        if rv is not None:
                            return rv
                        raise renpy.display.core.IgnoreEvent()
                elif renpy.map_event(ev, "button_alternate"):
                    rv = renpy.run(self.alternate)
                    if rv is not None:
                        return rv
                    raise renpy.display.core.IgnoreEvent()
            elif self.clicking and renpy.map_event(ev, "mouseup_1"):
                self.dragging = False
                self.clicking = False
                self.last_x = None
                self.last_y = None
                self.last_zpos = None
                self.last_rotate = None
                raise renpy.display.core.IgnoreEvent()
            if self.last_hovered != self.hovered:
                self.last_hovered = self.hovered
                return True
            self.last_hovered = self.hovered


    class CameraIcon(renpy.Displayable):

        def __init__(self, child, **properties):
            super(CameraIcon, self).__init__(**properties)
            # The child.
            self.child = renpy.displayable(child)
            self.dragging = False


        def init(self, int_x=True, int_y=True):
            self.int_x = int_x
            self.int_y = int_y
            if self.int_x:
                self.x_range = persistent._wide_range
            else:
                self.x_range = persistent._narrow_range
            if self.int_y:
                self.y_range = persistent._wide_range
            else:
                self.y_range = persistent._narrow_range

            self.x = (0.5 + get_property("offsetX")/(2.*self.x_range))*config.screen_width
            self.cx =  self.x
            self.y = (0.5 + get_property("offsetY")/(2.*self.y_range))*config.screen_height
            self.cy =  self.y


        def render(self, width, height, st, at):
            # Create a render from the child.
            child_render = renpy.render(self.child, width, height, st, at)
            # Get the size of the child.
            self.width, self.height = child_render.get_size()
            # Create the render we will return.
            render = renpy.Render(config.screen_width, config.screen_height)
            # Blit (draw) the child's render to our render.
            render.blit(child_render, (self.x-self.width/2., self.y-self.height/2.))
            # Return the render.
            return render


        def event(self, ev, x, y, st):

            if renpy.map_event(ev, "mousedown_1"):
                if self.x-self.width/2. <= x and x <= self.x+self.width/2. \
                    and self.y-self.height/2. <= y and y <= self.y+self.height/2.:
                    self.dragging = True
            elif renpy.map_event(ev, "mouseup_1"):
                self.dragging = False

            if get_property("offsetX") != int(self.cx) or get_property("offsetY") != int(self.cy):
                self.x = (0.5 + get_property("offsetX")/(2.*self.x_range))*config.screen_width
                self.y = (0.5 + get_property("offsetY")/(2.*self.y_range))*config.screen_height
                renpy.redraw(self, 0)

            if self.dragging:
                if self.x != x or self.y != y:
                    self.cx = 2*self.x_range*float(x)/config.screen_width
                    self.cy = 2*self.y_range*float(y)/config.screen_height
                    if self.int_x:
                        self.cx = int(self.cx)
                    if self.int_y:
                        self.cy = int(self.cy)
                    if self.cx != get_property("offsetX") or self.cy != get_property("offsetY"):
                        generate_changed("offsetX")(self.cx)
                        generate_changed("offsetY")(self.cy)
                    self.x, self.y = x, y
                    renpy.redraw(self, 0)


        def per_interact(self):
            renpy.redraw(self, 0)


        def visit(self):
            return [ self.child ]
    camera_icon = CameraIcon("camera.png")


    def generate_sound_menu(channel, time):
        from renpy.store import Function, _
        v = sound_keyframes[channel][time]
        button_list = [
            (_("edit value: [{}".format(v)),  #]"
             [Function(edit_playing_file, channel, time=time), Function(change_time, time)]),
            (_("edit time: {}".format(time)),
             Function(edit_move_keyframe, keys=channel, old=time, is_sound=True)),
            (_("remove"),
             Function(remove_keyframe, remove_time=time, key=channel, is_sound=True)),
            ]
        return button_list


    def generate_menu(key, check_point, use_wide_range=False, change_func=None, opened=None, in_graphic_mode=[]):
        from renpy.store import ToggleDict, Function, SelectedIf, SensitiveIf, Show
        check_points = all_keyframes[current_scene][key]
        i = check_points.index(check_point)
        (v, t, w) = check_point
        if isinstance(key, tuple):
            n, l, p = key
            k_list = [key]
            check_points_list = [check_points]
            loop_button_action = [ToggleDict(loops[current_scene], key)]
            for gn, ps in props_groups.items():
                if p in ps:
                    k_list = [(n, l, p) for p in props_groups[gn]]
                    check_points_list = [all_keyframes[current_scene][k2] for k2 in k_list]
                    loop_button_action = [ToggleDict(loops[current_scene], k2) for k2 in k_list+[(n, l, gn)]]
        else:
            k_list = [key]
            p = key
            check_points_list = [check_points]
            loop_button_action = [ToggleDict(loops[current_scene], key)]
            for gn, ps in props_groups.items():
                if p in ps:
                    if gn != "focusing":
                        k_list = props_groups[gn]
                        check_points_list = [all_keyframes[current_scene][k2] for k2 in k_list]
                        loop_button_action = [ToggleDict(loops[current_scene], k2) for k2 in k_list+[gn]]

        button_list = []

        if p == "child":
            button_list.append((("edit child: {}".format(v[0])), 
                Function(change_child, n, l, time=t, default=v[0])))
            button_list.append((("edit transform: {}".format(v[1])), 
                Function(edit_transition, n, l, time=t)))
        elif p in boolean_props + any_props:
            button_list.append((("edit value: {}".format(v)), 
                Function(edit_any, key, time=t)))
        else:
            button_list.append(( _("edit value: {}".format(v)),
                [Function(edit_value, change_func, default=v, use_wide_range=use_wide_range, force_plus=p in force_plus, time=t),
                Function(change_time, t)]))
            if w.startswith("warper_generator"):
                button_list.append(( _("open warper selecter: warper_generator"),
                    [Function(edit_warper, check_points=check_points_list, old=t, value_org=w)]))
            else:
                button_list.append(( _("open warper selecter: {}".format(w)),
                    [Function(edit_warper, check_points=check_points_list, old=t, value_org=w)]))
            if i > 0 and in_graphic_mode:
                button_list.append(( _("use warper generator"),
                    [SelectedIf(w.startswith("warper_generator")), Function(use_warper_generator, check_points=check_points_list, old=t)]))
            if p not in [prop for ps in props_groups.values() for prop in ps]:
                if i > 0:
                    button_list.append(( _("spline editor"),
                        [SelectedIf(t in splines[current_scene][key]), 
                        Show("_spline_editor", change_func=change_func, 
                            key=key, prop=p, pre=check_points[i-1], post=check_points[i], default=v, 
                            use_wide_range=use_wide_range, force_plus=p in force_plus, time=t)]))
                if len(check_points) >= 2:
                    if key in in_graphic_mode:
                        _in_graphic_mode = in_graphic_mode[:]
                        _in_graphic_mode.remove(key)
                    else:
                        _in_graphic_mode = in_graphic_mode + [key]
                    button_list.append(( _("toggle graphic editor"), [SelectedIf(key in in_graphic_mode), Show("_new_action_editor", opened=opened, in_graphic_mode=_in_graphic_mode)]))
            button_list.append(( _("reset"), Function(reset, key)))

        button_list.append(( _("edit time: {}".format(t)), Function(edit_move_keyframe, keys=k_list, old=t)))
        button_list.append(( _("remove"),
            [SensitiveIf(t > 0 or len(check_points) == 1), Function(remove_keyframe, remove_time=t, key=k_list)]))
        button_list.append(( _("toggle loop"), loop_button_action))
        return button_list


    def use_warper_generator(check_points, old):
        if not isinstance(check_points[0], list):
            check_points = [check_points]
        for cs in check_points:
            for i, (v, t, w) in enumerate(cs):
                if t == old:
                    cs[i] = (v, t, "warper_generator([(1., 1., 0.5)])")
                    break
        renpy.restart_interaction()


    @renpy.pure
    class CurrentTime(BarValue, DictEquality):

        def __init__(self, range):
            self.range = range
            self.adjustment = None
            self.lock = False


        def get_adjustment(self):
            self.adjustment = ui.adjustment(value=current_time, range=self.range, adjustable=True, changed=self.changed)
            return self.adjustment


        def changed(self, v):
            if not self.lock:
                change_time(v)


        def periodic(self, st):

            self.lock = True
            self.adjustment.change(current_time)
            self.lock = False

            return 0.01
