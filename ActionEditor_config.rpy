init 1600 python in _viewers:
    #this is used for default transition
    #デフォルトで使用されるトランジションの文字列です。Noneも指定可能です。
    default_transition = "dissolve"
init -1600 python in _viewers:
    #hide winodw during animation in clipboard data
    #アニメーション中ウィンドウを隠すようにクリップボードを出力するか決定します
    #シーンが1つのとき動作します。
    hide_window_in_animation = True
    #If this is True and hide_window_in_animation is True, allow animation to be skipped
    #アニメーションをスキップできる形式でクリップボードに出力します。hide_window_in_animationがTrueかつ
    #シーンが1つのとき動作します。
    allow_animation_skip = True
    #this is used for default warper
    #デフォルトで使用されるwarper関数名の文字列を指定します。
    default_warper = "linear"
    # If True, show rot default.
    #True, なら格子をデフォルトで表示します。
    default_rot = True
    # If True, simulate defpth of field and focusing is enable by default.
    # Trueならカメラブラーを再現するフォーカシングをデフォルトで有効にします。
    focusing = False
    # If True, show icons which is dragged to move camera or iamges by default
    # Trueならドラッグでカメラや画像を移動できるアイコンをデフォルトで表示します。
    default_show_camera_icon = True
    # If True, One line includes only one property in clipboard data
    # Trueならクリップボードデータで一行に1つのプロパティーのみ記述します。
    default_one_line_one_prop = False
    # If True, use legacy action editor screen
    # Trueなら以前のレイアウトでActionEditorを表示します。
    default_legacy_gui = False
    # If True, set camera keymap FPS(wasd), otherwise vim(hjkl)
    #Trueなら、カメラはWASD, wasdで、Falseならhjkl, HJKLで移動します。
    fps_keymap = True
    # If True, only one page is opened at once. this has no effect for legacy gui
    #Trueなら、一度に１つの項目のみ開きます。これはレガシーGUIでは無効です。
    default_open_only_one_page = False
    # the number of tabs shown at onece(In legacy GUI).
    #一度に表示する画像タグ数を設定します(レガシーGUIのみ)。
    tab_amount_in_page = 5
    #The blur value where the distance from focus position is dof.
    #フォーカシングでフォーカス位置からDOF離れた場所でのブラー量を設定します。
    _camera_blur_amount = 2.0 
    #warper function name which is used for the distance from focus position and blur amount.
    #フォーカス位置からの距離とカメラブラーの効きを決定するwarper関数名の文字列です
    _camera_blur_warper = "linear" 
    # the range of values of properties for int type(In legacy GUI)
    #エディターのバーに表示する整数の範囲です(レガシーGUIのみ)。
    wide_range = 1500
    # the range of values of properties for float type(In legacy GUI)
    #エディターのバーに表示する浮動小数の範囲です(レガシーGUIのみ)。
    narrow_range = 7.0
    # change per pix
    #Set the amount of change per pixel when dragging the value of the float property(In new GUI)
    narrow_drag_speed = 1./200
    #Set the amount of change per pixel when dragging the value of the integer property(In new GUI)
    #整数プロパティーの値をドラッグしたときの1pixelごとの変化量を設定します(新GUIのみ)。
    wide_drag_speed = int(config.screen_width/200)
    # the range of time
    #エディターのバーに表示する時間の範囲です。
    time_range = 7.0
    # the list of channel for playing
    # ActionEditorで使用するチャンネルのリストです
    default_channel_list = ["sound"]

    default_graphic_editor_narrow_range = 2.
    default_graphic_editor_wide_range = 2000

    preview_size=0.6
    preview_background_color="#111"

    props_sets = (
            ("Child/Pos    ", ("child", "xpos", "ypos", "zpos", "xalignaround", "yalignaround", "radius", "angle", "rotate")), 
            ("3D Matrix    ", ("offsetX", "offsetY", "offsetZ", "rotateX", "rotateY", "rotateZ")),
            ("Anchor/Offset", ("xanchor", "yanchor", "matrixanchorX", "matrixanchorY", "xoffset", "yoffset")), 
            ("Zoom/Crop    ", ("xzoom", "yzoom", "zoom", "cropX", "cropY", "cropW", "cropH")), 
            ("Effect       ", ("alpha", "blur", "additive", "invert", "contrast", "saturate", "bright", "hue", "dof", "focusing")),
            ("Misc         ", ("zzoom", "perspective", "xpan", "ypan", "xtile", "ytile")),
            )

    props_groups = {
        "alignaround":["xalignaround", "yalignaround"], 
        "matrixtransform":["rotateX", "rotateY", "rotateZ", "offsetX", "offsetY", "offsetZ"], 
        "matrixanchor":["matrixanchorX", "matrixanchorY"], 
        "matrixcolor":["invert", "contrast", "saturate", "bright", "hue"], 
        "crop":["cropX", "cropY", "cropW", "cropH"], 
        "focusing":["focusing", "dof"], 
    }

    special_props = ["child"]

    force_float = ("zoom", "xzoom", "yzoom", "alpha", "additive", "blur", "invert", "contrast", "saturate", "bright", "xalignaround", "yalignaround")
    force_wide_range = ("rotate", "rotateX", "rotateY", "rotateZ", "offsetX", "offsetY", "offsetZ", "zpos", "xoffset", "yoffset", "hue", "dof", "focusing", "angle", "xpan", "ypan")
    force_plus = ("additive", "blur", "alpha", "invert", "contrast", "saturate", "cropW", "cropH", "dof", "focusing", "xtile", "ytile")
    #crop doesn't work when perspective True and rotate change the pos of image when perspective is not True
    not_used_by_default = ("rotate", "cropX", "cropY", "cropW", "cropH", "xpan", "ypan")
    boolean_props = ["zzoom"]
    any_props = []
    exclusive = (
            ({"xpos", "ypos"}, {"xalignaround", "yalignaround", "radius", "angle"}), 
            ({"xtile", "ytile"}, {"xpan", "ypan"}), 
        )
    xygroup = {"pos": ("xpos", "ypos"), "anchor": ("xanchor", "yanchor"), "offset": ("xoffset", "yoffset")}

    #The order of properties in clipboard data.
    #この順番でクリップボードデータが出力されます
    sort_order_list = (
    "pos",
    "anchor",
    "offset",
    "xpos", 
    "xanchor", 
    "xoffset", 
    "ypos", 
    "yanchor", 
    "yoffset", 
    "alignaround",
    "radius",
    "angle",
    "zpos", 
    "matrixtransform", 
    "matrixanchor", 
    "rotate", 
    "xzoom", 
    "yzoom", 
    "zoom", 
    "crop", 
    "alpha", 
    "additive", 
    "blur", 
    "matrixcolor", 
    "xpan", 
    "ypan", 
    "xtile", 
    "ytile", 
    )

init 1600 python in _viewers:
    #The properties used in image tag tab
    #画像タブに表示されるプロパティー
    #(property name,  default value)
    transform_props = (
    ("child", (None, None)), 
    ("xpos", 0), 
    ("ypos", 0), 
    ("zpos", 0.), 
    # ("xalignaround", 0.),
    # ("yalignaround", 0.),
    # ("radius", 0),
    # ("angle", 0),
    ("xanchor", 0), 
    ("yanchor", 0), 
    ("matrixanchorX", 0.5), 
    ("matrixanchorY", 0.5), 
    ("xoffset", 0), 
    ("yoffset", 0), 
    ("rotate", 0,),
    ("xzoom", 1.), 
    ("yzoom", 1.), 
    ("zoom", 1.), 
    ("cropX", 0.), 
    ("cropY", 0.), 
    ("cropW", 1.), 
    ("cropH", 1.), 
    ("offsetX", 0.),
    ("offsetY", 0.),
    ("offsetZ", 0.),
    ("rotateX", 0.),
    ("rotateY", 0.),
    ("rotateZ", 0.),
    ("dof", 400),
    ("focusing", renpy.config.perspective[1]), 
    ("alpha", 1.), 
    ("additive", 0.), 
    ("blur", 0.), 
    ("hue", 0.), 
    ("bright", 0.), 
    ("saturate", 1.), 
    ("contrast", 1.), 
    ("invert", 0.), 
    ("zzoom", False),
    ("xpan", 0.), 
    ("ypan", 0.), 
    ("xtile", 1), 
    ("ytile", 1), 
    )

    #The properties used in camera tab
    #カメラタブに表示されるプロパティー
    #(property name,  default value)
    camera_props = (
    ("xpos", 0.), 
    ("ypos", 0.), 
    ("zpos", 0.), 
    # ("xalignaround", 0.),
    # ("yalignaround", 0.),
    # ("radius", 0),
    # ("angle", 0),
    ("xanchor", 0.), 
    ("yanchor", 0.), 
    ("matrixanchorX", 0.5), 
    ("matrixanchorY", 0.5), 
    ("xoffset", 0), 
    ("yoffset", 0), 
    ("rotate", 0,),
    ("xzoom", 1.), 
    ("yzoom", 1.), 
    ("zoom", 1.), 
    ("cropX", 0.), 
    ("cropY", 0.), 
    ("cropW", 1.), 
    ("cropH", 1.), 
    ("offsetX", 0.),
    ("offsetY", 0.),
    ("offsetZ", 0.),
    ("rotateX", 0.),
    ("rotateY", 0.),
    ("rotateZ", 0.),
    ("dof", 400),
    ("focusing", renpy.config.perspective[1]), 
    ("alpha", 1.), 
    ("additive", 0.), 
    ("blur", 0.), 
    ("hue", 0.), 
    ("bright", 0.), 
    ("saturate", 1.), 
    ("contrast", 1.), 
    ("invert", 0.), 
    ("xpan", 0.), 
    ("ypan", 0.), 
    ("xtile", 1), 
    ("ytile", 1), 
    ("perspective", None),
    )

    generate_groups_value = {}
    def generate_matrixtransform_value(rotateX, rotateY, rotateZ, offsetX, offsetY, offsetZ):
        return Matrix.offset(offsetX, offsetY, offsetZ)*Matrix.rotate(rotateX, rotateY, rotateZ)
    generate_groups_value["matrixtransform"] = generate_matrixtransform_value

    def generate_matrixanchor_value(matrixanchorX, matrixanchorY):
        return (matrixanchorX, matrixanchorY)
    generate_groups_value["matrixanchor"] = generate_matrixanchor_value

    def generate_matrixcolor_value(invert, contrast, saturate, bright, hue):
        return InvertMatrix(invert)*ContrastMatrix(contrast)*SaturationMatrix(saturate)*BrightnessMatrix(bright)*HueMatrix(hue)
    generate_groups_value["matrixcolor"] = generate_matrixcolor_value

    def generate_crop_value(cropX, cropY, cropW, cropH):
        return (cropX, cropY, cropW, cropH)
    generate_groups_value["crop"] = generate_crop_value

    def generate_alignaround_value(xalignaround, yalignaround):
        return (xalignaround, yalignaround)
    generate_groups_value["alignaround"] = generate_alignaround_value


    generate_groups_clipboard = {}
    def generate_matrixtransform_clipboard(rotateX, rotateY, rotateZ, offsetX, offsetY, offsetZ):
        v = "OffsetMatrix(%s, %s, %s)*RotateMatrix(%s, %s, %s)"
        return v % (offsetX, offsetY, offsetZ, rotateX, rotateY, rotateZ)
    generate_groups_clipboard["matrixtransform"] = generate_matrixtransform_clipboard

    def generate_matrixanchor_clipboard(matrixanchorX, matrixanchorY):
        v = "(%s, %s)"
        return v % (matrixanchorX, matrixanchorY)
    generate_groups_clipboard["matrixanchor"] = generate_matrixanchor_clipboard

    def generate_matrixcolor_clipboard(invert, contrast, saturate, bright, hue):
        v = "InvertMatrix(%s)*ContrastMatrix(%s)*SaturationMatrix(%s)*BrightnessMatrix(%s)*HueMatrix(%s)"
        return v % (invert, contrast, saturate, bright, hue)
    generate_groups_clipboard["matrixcolor"] = generate_matrixcolor_clipboard

    def generate_crop_clipboard(cropX, cropY, cropW, cropH):
        v = "(%s, %s, %s, %s)"
        return v % (cropX, cropY, cropW, cropH)
    generate_groups_clipboard["crop"] = generate_crop_clipboard

    def generate_alignaround_clipboard(xalignaround, yalignaround):
        v = "(%s, %s)"
        return v % (xalignaround, yalignaround)
    generate_groups_clipboard["alignaround"] = generate_alignaround_clipboard
