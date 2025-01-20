init python:
    bsar_g_rows = 4
    bsar_g_cols = 3
    bsar_g_cells = bsar_g_rows * bsar_g_cols
    
    bsar_qte_buttons_dict = {
        "↑": "K_UP",
        "↓": "K_DOWN",
        "→": "K_RIGHT" 
    }

    bsar_bar_full = Frame(bsar_gui_path + "bar_null.png")
    bsar_bar_null = Frame(bsar_gui_path + "bar_full.png")

    bsar_qte_true_button = []
    bsar_qte_true_button_pl = []
    bsar_qte_score = 0

    def bsar_qte_clear():
        global bsar_qte_score

        bsar_qte_true_button = []
        bsar_qte_true_button_pl = []
        bsar_qte_score = 0

    def bsar_qte_current_button(button, count):
        global bsar_qte_true_button, bsar_qte_true_button_pl                              
        
        for i in range(count): 
            for j in range(len(button)):
                for key, value in bsar_qte_buttons_dict.iteritems():
                    if key == button[j]:
                        bsar_qte_true_button_pl.append(key)
                        bsar_qte_true_button.append(value)

        renpy.restart_interaction()

    def bsar_qte_next_button():
        global bsar_qte_score

        del bsar_qte_true_button[0]

        bsar_qte_score += 1

        try: 
            del bsar_qte_true_button_pl[0]

        except: 
            pass

        renpy.restart_interaction()
 
    bsar_qte_current_button_curried = renpy.curry(bsar_qte_current_button)
    bsar_qte_next_button_curried = renpy.curry(bsar_qte_next_button)

screen bsar_qte_time_bar(time):
    bar:
        keyboard_focus False
        left_bar bsar_bar_full
        right_bar bsar_bar_null
        xalign 0.5
        yalign 0.1
        left_gutter 230
        right_gutter 230
        ymaximum 300 
        ysize 300

        value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=time)

    timer time action Jump("bsar_insomnia_day1_stroll_failed")

screen bsar_qte(button, count, time):
    tag game
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()
        
    key "K_SCROLLOCK":
        action NullAction()
        
    key "mouseup_3":
        action NullAction()
        
    key "mouseup_4":
        action NullAction()
        
    key "K_PAGEUP":
        action NullAction()
    
    key "repeat_K_PAGEUP":
        action NullAction()
    
    key "K_AC_BACK":
        action NullAction()

    key "mouseup_2":
        action NullAction()

    key "h":
        action NullAction()

    key "K_RETURN":
        action NullAction()

    key "K_SPACE":
        action NullAction()

    key "K_KP_ENTER":
        action NullAction()
        
    key "K_SELECT":
        action NullAction()

    use bsar_qte_time_bar(time)

    on "show" action bsar_qte_current_button_curried(button, count)     
    
    if len(bsar_qte_true_button) != 0:
        text (u"x%s" % len(bsar_qte_true_button)) align(.5, .1) style "bsar_qte_text"

        add "circle_full" align (.5, .62)

        if len(bsar_qte_true_button_pl) != 0:
            text bsar_qte_true_button_pl[0].upper() align(.5, .6) size 84 color "#ffffff" at bsar_zoom_qte_text

        else:
            text bsar_qte_true_button[0].upper() align(.5, .6) size 84 color "#ffffff" at bsar_zoom_qte_text
        
        key "{}".format(bsar_qte_true_button[0]) action bsar_qte_next_button_curried()

    else:
        $ bsar_qte_clear()
        timer .01 action Return(True)

screen bsar_preferences():
    tag menu
    modal True
    
    key "K_F1":
        action NullAction()
    
    add bsar_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"
    
    text "Настройки":
        size 70
        xalign 0.5
        yalign 0.062
        font bsar_flow_ext
        antialias True
        kerning 2
        
    text "Режим экрана":
        font bsar_flow_ext
        size 65
        xalign 0.5
        ypos 190
        
    textbutton "На весь экран":
        style "bsar_button_none"
        text_style "bsar_text_preferences_" + persistent.timeofday
        xalign 0.15
        ypos 270
        action Preference("display", "fullscreen")
        
    textbutton "В окне":
        style "bsar_button_none"
        text_style "bsar_text_preferences_" + persistent.timeofday
        xalign 0.8
        ypos 275

        if not _preferences.fullscreen:
            text_style "bsar_text_inverse_preferences_" + persistent.timeofday

        else:
            text_style "bsar_text_preferences_" + persistent.timeofday

        action Preference("display", "window")

    text "Размер шрифта":
        font bsar_flow_ext
        size 65
        xalign 0.5
        ypos 395
        
    textbutton "Обычный":
        style "bsar_button_none"
        text_style "bsar_text_preferences_" + persistent.timeofday
        xalign 0.175
        ypos 475
        action SetField(persistent, "font_size", "small")
        
    textbutton "Большой":
        style "bsar_button_none"
        text_style "bsar_text_preferences_" + persistent.timeofday
        xalign 0.82
        ypos 475
        action SetField(persistent, "font_size", "large")
        
    textbutton "Музыка":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xpos 430
        ypos 665
    bar:
        value Preference("music volume")
        right_bar bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_bar_null.png"
        left_bar bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_bar_full.png"
        thumb bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_thumb.png"
        xpos 975
        ypos 670
        xmaximum 400
        ymaximum 85
        
    textbutton "Звуки":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xpos 425
        ypos 779
    bar:
        value Preference("sound volume")
        right_bar bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_bar_null.png"
        left_bar bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_bar_full.png"
        thumb bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_thumb.png"
        xpos 975
        ypos 785
        xmaximum 400
        ymaximum 85

    textbutton "Эмбиент":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xpos 422
        ypos 895
    bar:
        value Preference("voice volume")
        right_bar bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_bar_null.png"
        left_bar bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_bar_full.png"
        thumb bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_thumb.png"
        xpos 975
        ypos 901
        xmaximum 400
        ymaximum 85     

    textbutton "Назад":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xpos 235
        ypos 970
        action [Hide("bsar_preferences"), Return()]

screen bsar_save():
    tag menu
    modal True
    
    add bsar_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"

    text "Сохранение":
        size 70
        xalign 0.5
        yalign 0.062
        font bsar_flow_ext
        antialias True
        kerning 2

    textbutton "Назад": 
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.12 
        yalign 0.97
        action Return()

    textbutton "Сохранить": 
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.5
        yalign 0.97
        action (BsarFunctionCallback(bsar_on_save_callback, selected_slot), FileSave(selected_slot))

    textbutton "Удалить": 
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.88
        yalign 0.97
        action FileDelete(selected_slot)

    grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
        transpose False
        xfill True
        yfill True

        for i in range(1, 13):
            fixed:
                add FileScreenshot(i) xpos 10 ypos 10

                button:
                    action SetVariable("selected_slot", i)
                    xfill False
                    yfill False
                    style "bsar_save_load_button_" + persistent.timeofday
                    has fixed
                    text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" +FileSaveName(i)) style "bsar_text_save_load_main_menu" xpos 15 ypos 15
    
screen bsar_load():
    tag menu
    modal True
    
    add bsar_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"

    text "Загрузка":
        size 70
        xalign 0.5
        yalign 0.062
        font bsar_flow_ext
        antialias True
        kerning 2

    textbutton "Назад":
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.12 
        yalign 0.97 
        action Return()

    textbutton "Загрузить":
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.5
        yalign 0.97
        action (BsarFunctionCallback(bsar_on_load_callback, selected_slot), FileLoad(selected_slot, confirm=False))
    
    textbutton "Удалить":
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.88
        yalign 0.97
        action FileDelete(selected_slot)

    grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
        transpose False
        xfill True
        yfill True

        for i in range(1, 13):
            fixed:
                add FileScreenshot(i) xpos 10 ypos 10

                button:
                    action SetVariable("selected_slot", i)
                    xfill False
                    yfill False
                    style "bsar_save_load_button_" + persistent.timeofday
                    has fixed
                    text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" + FileSaveName(i)) style "bsar_text_save_load_main_menu" xpos 15 ypos 15
                                
screen bsar_say(what, who):    
    window background None id "window":
        if persistent.font_size == "large":
            add bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box_large.png" xpos -6 ypos 770

            imagebutton:
                idle bsar_gui_path + "dialogue_box/backward_idle.png"
                hover bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_hover.png"
                xpos 38 
                ypos 924 
                action ShowMenu("bsar_text_history")

            if not config.skipping:
                imagebutton:
                    idle bsar_gui_path + "dialogue_box/forward_idle.png"
                    hover bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_hover.png"
                    xpos 1768 
                    ypos 924 
                    action Skip()

            else:
                imagebutton: 
                    idle bsar_gui_path + "dialogue_box/fast_forward_idle.png"
                    hover bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_hover.png"
                    xpos 1768 
                    ypos 924 
                    action Skip()

            text what:
                id "what" 
                xpos 194 
                ypos 914 
                xmaximum 1541 
                size 30
                line_spacing 1

            if who:
                text who:
                    id "who" 
                    xpos 194 
                    ypos 877 
                    size 35 
                    line_spacing 1

        elif persistent.font_size == "small":
            add bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box.png" xpos -6 ypos 800

            imagebutton:
                idle bsar_gui_path + "dialogue_box/backward_idle.png"
                hover bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_hover.png"
                xpos 38 
                ypos 949 
                action ShowMenu("bsar_text_history")

            if not config.skipping:
                imagebutton:
                    idle bsar_gui_path + "dialogue_box/forward_idle.png"
                    hover bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_hover.png"
                    xpos 1768 
                    ypos 949 
                    action Skip()

            else:
                imagebutton:
                    idle bsar_gui_path + "dialogue_box/fast_forward_idle.png"
                    hover bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_hover.png"
                    xpos 1768 
                    ypos 949 
                    action Skip()

            text what:
                id "what" 
                xpos 194 
                ypos 964 
                xmaximum 1541 
                size 25
                line_spacing 2

            if who:
                text who:
                    id "who" 
                    xpos 194 
                    ypos 931 
                    size 28 
                    line_spacing 2

screen bsar_nvl(items, dialogue):
    window background Frame((bsar_gui_path + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
        has vbox

        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10

                if persistent.font_size == "large":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 38

                    text what:
                        id what_id 
                        size 35

                elif persistent.font_size == "small":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 31

                    text what:
                        id what_id 
                        size 28

        if items:
            vbox:
                id "menu"

                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"

                    else:
                        text caption style "nvl_dialogue"

    imagebutton:
        idle bsar_gui_path + "dialogue_box/backward_idle.png"
        hover bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_hover.png"
        xpos 38 
        ypos 924
        action ShowMenu("bsar_text_history")

    if not config.skipping:
        imagebutton:
            idle bsar_gui_path + "dialogue_box/forward_idle.png"
            hover bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_hover.png"
            xpos 1768
            ypos 949
            action Skip()

    else:
        imagebutton:
            idle bsar_gui_path + "dialogue_box/fast_forward_idle.png"
            hover bsar_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_hover.png"
            xpos 1768
            ypos 949
            action Skip()

screen bsar_game_menu_selector():
    tag menu
    modal True

    if bsar_lock_quick_menu:
        timer 0.01 action Return()

    else:
        button style "blank_button" xfill True yfill True action Return()

        add bsar_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_ground.png" xalign 0.5 yalign 0.5
    
        text "{font=[bsar_flow_ext]}Пауза{/font}":
            size 80
            xalign 0.5
            ypos 274
            antialias True
            kerning 2
            
        textbutton "В главное меню":
            style "bsar_button_none"
            text_style "bsar_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 418
            action [Function(bsar_set_dynamic_cursor, "main_menu"), MainMenu(confirm=False)]
            
        textbutton "Сохранить":
            style "bsar_button_none"
            text_style "bsar_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 505
            action ShowMenu("bsar_save")
            
        textbutton "Загрузить":
            style "bsar_button_none"
            text_style "bsar_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 593
            action ShowMenu("bsar_load")
            
        textbutton "Настройки":
            style "bsar_button_none"
            text_style "bsar_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 680
            action ShowMenu("bsar_preferences")
            
        textbutton "Выход":
            style "bsar_button_none"
            text_style "bsar_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 765
            action [(Function(bsar_screens_diact)), ShowMenu("main_menu")]

screen bsar_quit():
    tag menu
    modal True

    if bsar_lock_quit:
        timer 0.01 action Return()

    elif bsar_lock_quit_game_main_menu_var:
        timer 0.01 action Quit(confirm=False)

    else:
        add bsar_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"
            
        text "Вы действительно \nхотите выйти?":
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2
            font bsar_diamond_girl_skinny
            
        textbutton "Да":
            style "bsar_button_none"
            text_style "bsar_text_" + persistent.timeofday
            xalign 0.3
            ypos 650
            action [(Function(bsar_screens_diact)), ShowMenu("main_menu")]
            
        textbutton "Нет":
            style "bsar_button_none"
            text_style "bsar_text_" + persistent.timeofday
            xalign 0.7
            ypos 650
            action [Hide("bsar_quit"), Return()]

screen bsar_yesno_prompt(yes_action, message, no_action):
    modal True

    add bsar_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"

    $ bsar_yesno_prompt_colors = {
        "winter_day": "#64483c",
        "winter_night": "#161d3d",
        "fog": "#008193",
        "bw": "#5a3525"
    }

    text _(message):
        text_align 0.5 
        yalign 0.46 
        xalign 0.5
        font bsar_diamond_girl_skinny 
        size 100

    textbutton "Да": 
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        yalign 0.68 
        xalign 0.3 
        action yes_action

    textbutton "Нет": 
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        yalign 0.68 
        xalign 0.7 
        action no_action

screen bsar_text_history():
    tag menu
    predict False

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    $ bsar_text_history_color = {                        
        "winter_day": "#2171b8",
        "winter_night": "#0143b3",
        "fog": "#c2dded",
        "bw": "#dcd168"
                            }

    if persistent.font_size == "small":
        $ history_text_size = 28
        $ history_name_size = 29

    elif persistent.font_size == "large":
        $ history_text_size = 36
        $ history_name_size = 37

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame(bsar_gui_path + "choice/" + persistent.timeofday + "/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:
        viewport id "bsar_text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:
                if h.who:
                    text h.who:
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        
                        if "color" in h.who_args:
                            color h.who_args["color"]

                textbutton h.what:
                    text_size history_text_size
                    style "bsar_button_none" 
                    text_style "bsar_text_history" 
                    xpos 100                    
                    xmaximum xmax
                    text_hover_color bsar_text_history_color[persistent.timeofday]                    
                    action RollbackToIdentifier(h.rollback_identifier) 
        
        vbar value YScrollValue("bsar_text_history_screen") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb bsar_gui_path + "preferences/" + persistent.timeofday + "/bsar_thumb.png" xoffset 1700  

screen bsar_choice(items):
    modal True

    $ bsar_choice_color = "#ffffff"
    $ bsar_choice_color_selected = "#808080"
    $ bsar_choice_colors_hover = {                        
        "winter_day": "#2171b8",
        "winter_night": "#0143b3",
        "fog": "#c2dded",
        "bw": "#dcd168"
                        }

    window background Frame((bsar_gui_path + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yalign 0.5 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:
        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:
                button background None:
                    xalign 0.5
                    action action

                    if persistent.licensed:
                        if caption in persistent.choices and caption != "Налево" and caption != "Направо" and caption != "Go left" and caption != "Go right" and caption != "Ir a la izquierda" and caption != "Ir a la derecha":
                            text caption font header_font size 37 hover_size 37 color bsar_choice_color_selected hover_color bsar_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5
                            
                        else:
                            text caption font header_font size 37 hover_size 37 color bsar_choice_color hover_color bsar_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5

                    else:
                        text caption font header_font size 37 hover_size 37 color bsar_choice_color hover_color bsar_choice_colors_hover[persistent.timeofday] xalign 0.5

            else:
                if persistent.licensed:
                    text caption font header_font size 60 color bsar_choice_color text_align 0.5 xcenter 0.5

                else:
                    text caption font header_font size 40 color bsar_choice_color xalign 0.5 text_align 0.5 xcenter 0.5

screen bsar_help():
    tag menu
    modal True
    
    add bsar_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"
    
    text "Информация":
        size 70
        xalign 0.5
        ypos 33
        antialias True
        kerning 2
        font bsar_diamond_girl_skinny

    textbutton "Группа VK":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5
        ypos 280
        action OpenURL("https://vk.com/public176281709")
            
    textbutton "Яна":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5
        ypos 410
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2239853287")

    textbutton "Один украденный день":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5
        ypos 530
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=1746278653")   
            
    textbutton "Петля времени":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5
        ypos 650
        action OpenURL("https://youtu.be/x2KBAuBKWL8")

    add "bsar_logowhite_hover" xpos 1520 ypos 880

    textbutton "Назад":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5 
        yalign 0.92 
        action Return()