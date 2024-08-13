init python:
    bsar_g = Gallery()
    bsar_page = 0
    bsar_g.transition = fade
    bsar_g.locked_button = bsar_gui_path + "/save_load/main_menu/save_load_button_idle.png"
    bsar_g.navigation = False

    bsar_rows = 4
    bsar_cols = 3
    bsar_cells = bsar_rows * bsar_cols

    bsar_gallery_bg_list = [
    "bsar_ext_camp_entrance_winter_day", "bsar_ext_camp_entrance_winter_night", "bsar_ext_clubs_winter_night", "bsar_ext_dining_hall_away_winter_day", "bsar_ext_dining_hall_near_winter_day",
    "bsar_ext_house_of_mt_fog", "bsar_ext_house_of_mt_winter_night2", "bsar_ext_houses_winter_day", "bsar_ext_houses_winter_night", "bsar_ext_houst_of_mt_winter_day",
    "bsar_ext_library_winter_day", "bsar_ext_musclub_winter_night", "bsar_ext_old_building_fog", "bsar_ext_path2_fog", "bsar_ext_road_winter_day",
    "bsar_ext_road_winter_night", "bsar_ext_square_fog", "bsar_ext_square_winter_day", "bsar_ext_square_winter_night", "bsar_ext_winter_park", "bsar_ext_winter_street",
    "bsar_form", "bsar_int_kitchen_bw", "bsar_int_old_building_night_edited", "bsar_lane", "bsar_makarov_pistol", "bsar_medical_room_celling", "bsar_prosecutor_office",
    "bsar_roof", "bsar_ext_winter_forest", "bsar_us_dv_confrontation"
    ]

    for bg in bsar_gallery_bg_list:
        bsar_g.button(bg)
        bsar_g.image(im.Crop("bsar/images/bg/" + bg + ".png", (0, 0, 1920, 1080)))
        bsar_g.unlock("bg " + bg)

    bsar_bar_full = Frame(bsar_gui_path + "bar_null.png")
    bsar_bar_null = Frame(bsar_gui_path + "bar_full.png")
    
    bsar_qte_buttons_dict = {
        "↑": "K_UP",
        "↓": "K_DOWN",
        "→": "K_RIGHT" 
    }

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

        value AnimatedValue(old_value = 1.0, value = 0.0, range = 1.0, delay = time)

    timer time action Jump("bsar_day1_stroll_failed")

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

screen bsar_main_menu():
    tag menu 
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "bsar_insomnia_main_menu_bg"
    
    if bsar_main_menu_var:
        add "bsar_main_menu_frame" xalign 0.5 ypos 290

        text "{font=[bsar_diamond_girl_skinny]}Бессонница{/font}":
            size 170
            text_align 0.5
            xalign 0.5
            ypos 40
            antialias True
            kerning 2
            
        textbutton ["Начать игру"] at bsar_buttons_atl():
            style "bsar_main_menu_text_style"
            text_style "bsar_main_menu_text_style"
            xalign 0.5
            yalign 0.35
            action [bsar_set_dynamic_cursor('null'), SetVariable("bsar_lock_quit_game_main_menu_var", False), Start("bsar_insomnia_day1")]
                
        textbutton ["Загрузить"] at bsar_buttons_atl():
            style "bsar_main_menu_text_style"
            text_style "bsar_main_menu_text_style"
            xalign 0.5
            yalign 0.475
            action [SetVariable("bsar_main_menu_var", False), ShowMenu("bsar_load_main_menu")]
            
        textbutton "[bsar_preferences_text]" at bsar_buttons_atl():
            style "bsar_main_menu_text_style"
            text_style "bsar_main_menu_text_style"
            xalign 0.5
            yalign 0.6
            action [SetVariable("bsar_main_menu_var", False), ShowMenu("bsar_preferences_main_menu")]

        textbutton "[bsar_extra_text]" at bsar_buttons_atl():
            style "bsar_main_menu_text_style"
            text_style "bsar_main_menu_text_style"
            xalign 0.5
            yalign 0.725
            action [SetVariable("bsar_main_menu_var", False), ShowMenu("bsar_extra")]
                
        textbutton ["Выход"] at bsar_buttons_atl():
            style "bsar_main_menu_text_style"
            text_style "bsar_main_menu_text_style"
            xalign 0.5
            yalign 0.85
            action [SetVariable("bsar_main_menu_var", False), Hide("bsar_main_menu"), (Function(bsar_screens_diact)), ShowMenu("main_menu")]
            
        imagebutton:
            idle "bsar_logowhite_idle"
            hover "bsar_logowhite_hover"
            xpos 1520
            ypos 800
            action OpenURL("https://vk.com/public176281709")
        
screen bsar_preferences_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not bsar_main_menu_var:        
        text "[bsar_preferences_text]":
            font bsar_diamond_girl_skinny
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        text "[bsar_display_preferences_text]":
            font bsar_diamond_girl_skinny
            size 70
            xalign 0.5
            ypos 200
            
        textbutton ["На весь экран"]:
            style "bsar_button_none"
            text_style "bsar_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.15
            ypos 280
            action Preference("display", "fullscreen")
            
        textbutton ["В окне"]:
            style "bsar_button_none"
            text_align 0.5
            xalign 0.8
            ypos 280

            if not _preferences.fullscreen:
                text_style "bsar_preferences_main_menu_text_style_inverse"

            else:
                text_style "bsar_preferences_main_menu_text_style"

            action Preference("display", "window")

        text "{font=[bsar_diamond_girl_skinny]}Размер шрифта{/font}":
            size 70
            xalign 0.5
            ypos 360
                
        textbutton ["Обычный"]:
            style "bsar_button_none"
            text_style "bsar_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.175
            ypos 440
            action SetField(persistent, "font_size", "small")
                
        textbutton ["Большой"]:
            style "bsar_button_none"
            text_style "bsar_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.82
            ypos 440
            action SetField(persistent, "font_size", "large")
                
        text "{font=[bsar_diamond_girl_skinny]}Пропускать{/font}":
            size 70
            xalign 0.5
            ypos 520

        if not _preferences.skip_unseen:
            textbutton ["Виденное ранее"]:
                style "bsar_button_none"
                text_style "bsar_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton ["Весь текст"]:
                style "bsar_button_none"
                text_style "bsar_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.83
                ypos 600
                action Preference("skip", "all")
                            
        if _preferences.skip_unseen:
            textbutton ["Виденное ранее"]:
                style "bsar_button_none"
                text_style "bsar_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton ["Весь текст"]:
                style "bsar_button_none"
                text_style "bsar_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.83
                ypos 600
                action Preference("skip", "all")    
            
        text "{font=[bsar_diamond_girl_skinny]}Громкость музыки{/font}":
            size 70
            xpos 430
            ypos 820
        bar:
            value Preference("music volume")
            right_bar bsar_gui_path + "/preferences/main_menu/bsar_bar_null.png"
            left_bar bsar_gui_path + "/preferences/main_menu/bsar_bar_full.png"
            thumb bsar_gui_path + "/preferences/main_menu/bsar_vthumb.png"
            xpos 975
            ypos 827
            xmaximum 400
            ymaximum 85

        textbutton "[bsar_return_text]" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [SetVariable("bsar_main_menu_var", True), Hide("bsar_preferences_main_menu"), ShowMenu("bsar_main_menu")]
        
screen bsar_load_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not bsar_main_menu_var:        
        text "{font=[bsar_diamond_girl_skinny]}Загрузка{/font}":
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        textbutton "[bsar_return_text]" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.1
            ypos 970
            action [SetVariable("bsar_main_menu_var", True), Hide("bsar_load_main_menu"), ShowMenu("bsar_main_menu")]
                    
        textbutton ["Загрузить"] at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action (BsarFunctionCallback(bsar_on_load_callback, selected_slot), FileLoad(selected_slot, confirm=False))
                 
        textbutton "[bsar_delete_text]" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.9
            ypos 970
            action FileDelete(selected_slot, confirm = False)
            
        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True

            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "bsar_save_load_button_main_menu"

                        fixed:
                            text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " " + "Пусто") + "\n" + FileSaveName(i)):
                                style "bsar_text_save_load_main_menu"
                                xpos 15
                                ypos 15
        
screen bsar_extra():
    modal True

    key "K_F1":
        action NullAction()
    
    if not bsar_main_menu_var:
        add "bsar_main_menu_frame" xalign 0.5 ypos 290

        text ["Дополнительно"]:
            size 150
            text_align 0.5
            xalign 0.5
            ypos 40
            font bsar_diamond_girl_skinny
            antialias True
            kerning 2

        textbutton ["Тени прошлого"] at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.5
            ypos 387
            action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2694121607")

        textbutton ["Галерея"] at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.5
            ypos 539
            action [Hide("bsar_extra"), ShowMenu("bsar_background_gallery")]

        textbutton ["Достижения"] at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.5
            ypos 677
            action [Hide("bsar_extra"), ShowMenu("bsar_achievements")]

        textbutton "[bsar_return_text]" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.5
            ypos 822
            action [SetVariable("bsar_main_menu_var", True), Hide("bsar_extra"), ShowMenu("bsar_main_menu")]

screen bsar_achievements:
    modal True

    if not bsar_main_menu_var:
        text ["Достижения"]:
            font bsar_diamond_girl_skinny
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        if not persistent.bsar_achievements["bsar_murderous_snowball"]:
            add "bsar_locked" xalign 0.5 ypos 268

        else:
            add "bsar_murderous_snowball" xalign 0.5 ypos 268

        if not persistent.bsar_achievements["bsar_awakening"]:
            add "bsar_locked" xalign 0.5 ypos 507

        else:
            add "bsar_awakening" xalign 0.5 ypos 507

        if not persistent.bsar_achievements["bsar_paradise"]:
            add "bsar_locked" xalign 0.5 ypos 745

        else:
            add "bsar_paradise" xalign 0.5 ypos 745

        textbutton "[bsar_return_text]" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [Hide("bsar_achievements"), ShowMenu("bsar_extra")]

screen bsar_background_gallery():
    modal True

    if not bsar_main_menu_var:
        $ bsar_gallery_table = bsar_gallery_bg_list

        $ bsar_len_table = len(bsar_gallery_bg_list)

        text "{font=[bsar_diamond_girl_skinny]}Галерея{/font}":
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        textbutton "[bsar_return_text]" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [Hide("bsar_background_gallery"), ShowMenu("bsar_extra")]

        grid bsar_rows bsar_cols xpos 0.09 ypos 0.18:
            $ bsar_bg_displayed = 0
            $ bsar_next_page = bsar_page + 1

            if bsar_next_page > int(bsar_len_table / bsar_cells):
                $ bsar_next_page = 0

            for n in range(bsar_len_table):
                if n < (bsar_page + 1) * bsar_cells and n >= bsar_page * bsar_cells:
                    $ _bsar_t = im.Crop("bsar/images/bg/" + bsar_gallery_table[n] + ".png", (0, 0, 1920, 1080))
                            
                    $ _bsar_img_scaled = im.Scale(_bsar_t, 320, 180)

                    $ bsar_img = im.Composite((336, 196), (8, 8), im.Alpha(_bsar_img_scaled, 0.9), (0, 0), im.Image(bsar_gui_path + "/save_load/main_menu/save_load_button_idle.png"))
                    $ bsar_imgh = im.Composite((336, 196), (8, 8), _bsar_img_scaled, (0, 0), im.Image(bsar_gui_path + "/save_load/main_menu/save_load_button_hover.png"))

                    add bsar_g.make_button(bsar_gallery_table[n], get_image("gui/gallery/blank.png"), None, bsar_imgh, bsar_img , style = "blank_button", bottom_margin = 50, right_margin = 50)

                    $ bsar_bg_displayed += 1

                    if n + 1 == bsar_len_table:
                        $ bsar_next_page = 0

            for j in range(0, bsar_cells - bsar_bg_displayed):
                null

        if bsar_page != 0:
            imagebutton:
                idle "bsar/images/gui/dialogue_box/backward_idle.png"
                hover "bsar/images/gui/dialogue_box/winter_night/backward_hover.png"
                yalign 0.5 
                xalign 0.01 
                action [SetVariable("bsar_page", bsar_page - 1), ShowMenu("bsar_background_gallery")]

        if bsar_page != int(bsar_page_counter(bsar_len_table, bsar_cells)) - 1:
            imagebutton: 
                idle "bsar/images/gui/dialogue_box/forward_idle.png"
                hover "bsar/images/gui/dialogue_box/winter_night/forward_hover.png"
                yalign 0.5 
                xalign 0.99 
                action [SetVariable("bsar_page", bsar_next_page), ShowMenu("bsar_background_gallery")]
        
screen bsar_preferences():
    tag menu
    modal True
    
    key "K_F1":
        action NullAction()
    
    add bsar_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"
    
    text ["Настройки"]:
        size 70
        xalign 0.5
        yalign 0.062
        font bsar_flow_ext
        antialias True
        kerning 2
        
    text ["Режим экрана"]:
        font bsar_flow_ext
        size 65
        xalign 0.5
        ypos 190
        
    textbutton ["На весь экран"]:
        style "bsar_button_none"
        text_style "bsar_text_preferences_" + persistent.timeofday
        xalign 0.15
        ypos 270
        action Preference("display", "fullscreen")
        
    textbutton ["В окне"]:
        style "bsar_button_none"
        text_style "bsar_text_preferences_" + persistent.timeofday
        xalign 0.8
        ypos 275

        if not _preferences.fullscreen:
            text_style "bsar_text_inverse_preferences_" + persistent.timeofday

        else:
            text_style "bsar_text_preferences_" + persistent.timeofday

        action Preference("display", "window")

    text ["Размер шрифта"]:
        font bsar_flow_ext
        size 65
        xalign 0.5
        ypos 395
        
    textbutton ["Обычный"]:
        style "bsar_button_none"
        text_style "bsar_text_preferences_" + persistent.timeofday
        xalign 0.175
        ypos 475
        action SetField(persistent, "font_size", "small")
        
    textbutton ["Большой"]:
        style "bsar_button_none"
        text_style "bsar_text_preferences_" + persistent.timeofday
        xalign 0.82
        ypos 475
        action SetField(persistent, "font_size", "large")
        
    textbutton ["Музыка"]:
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
        
    textbutton ["Звуки"]:
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

    textbutton ["Эмбиент"]:
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

    textbutton ["Назад"]:
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xpos 235
        ypos 970
        action [Hide("bsar_preferences"), Return()]

screen bsar_save():
    tag menu
    modal True
    
    add bsar_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"

    text ["Сохранение"]:
        size 70
        xalign 0.5
        yalign 0.062
        font bsar_flow_ext
        antialias True
        kerning 2

    textbutton "[bsar_return_text]": 
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.12 
        yalign 0.97
        action Return()

    textbutton ["Сохранить"]: 
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.5
        yalign 0.97
        action (BsarFunctionCallback(bsar_on_save_callback,selected_slot), FileSave(selected_slot))

    textbutton "[bsar_delete_text]": 
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
                    text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " " +translation_new["Empty_slot"]) + "\n" +FileSaveName(i)) style "bsar_text_save_load_main_menu" xpos 15 ypos 15
    
screen bsar_load():
    tag menu
    modal True
    
    add bsar_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"

    text ["Загрузка"]:
        size 70
        xalign 0.5
        yalign 0.062
        font bsar_flow_ext
        antialias True
        kerning 2

    textbutton "[bsar_return_text]":
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.12 
        yalign 0.97 
        action Return()

    textbutton ["Загрузить"]:
        style "bsar_button_none"
        text_style "bsar_save_load_" + persistent.timeofday
        xalign 0.5
        yalign 0.97
        action (BsarFunctionCallback(bsar_on_load_callback,selected_slot), FileLoad(selected_slot, confirm=False))
    
    textbutton "[bsar_delete_text]":
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
                    text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" " + translation_new["Empty_slot"]) + "\n" + FileSaveName(i)) style "bsar_text_save_load_main_menu" xpos 15 ypos 15
                                
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
            
        textbutton ["В главное меню"]:
            style "bsar_button_none"
            text_style "bsar_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 418
            action [bsar_set_main_menu_cursor_curried(), MainMenu(confirm = False)]
            
        textbutton ["Сохранить"]:
            style "bsar_button_none"
            text_style "bsar_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 505
            action ShowMenu("bsar_save")
            
        textbutton ["Загрузить"]:
            style "bsar_button_none"
            text_style "bsar_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 593
            action ShowMenu("bsar_load")
            
        textbutton ["Настройки"]:
            style "bsar_button_none"
            text_style "bsar_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 680
            action ShowMenu("bsar_preferences")
            
        textbutton ["Выход"]:
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
            
        text ["Вы действительно \nхотите выйти?"]:
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2
            font bsar_diamond_girl_skinny
            
        textbutton "[bsar_yes_text]":
            style "bsar_button_none"
            text_style "bsar_text_" + persistent.timeofday
            xalign 0.3
            ypos 650
            action [(Function(bsar_screens_diact)), ShowMenu("main_menu")]
            
        textbutton "[bsar_no_text]":
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

    textbutton "[bsar_yes_text]": 
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        yalign 0.68 
        xalign 0.3 
        action yes_action

    textbutton "[bsar_no_text]": 
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
    
    text ["Информация"]:
        size 70
        xalign 0.5
        ypos 33
        antialias True
        kerning 2
        font bsar_diamond_girl_skinny

    textbutton ["Группа VK"]:
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5
        ypos 280
        action OpenURL("https://vk.com/public176281709")
            
    textbutton ["Яна"]:
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5
        ypos 410
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2239853287")

    textbutton ["Один украденный день"]:
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5
        ypos 530
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=1746278653")   
            
    textbutton ["Петля времени"]:
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5
        ypos 650
        action OpenURL("https://youtu.be/x2KBAuBKWL8")

    add "bsar_logowhite_hover" xpos 1520 ypos 880

    textbutton "[bsar_return_text]":
        style "bsar_button_none"
        text_style "bsar_text_" + persistent.timeofday
        xalign 0.5 
        yalign 0.92 
        action Return()