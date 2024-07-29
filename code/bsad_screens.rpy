init python:
    insomnia_g = Gallery()
    insomnia_page = 0
    insomnia_g.transition = fade
    insomnia_g.locked_button = insomnia_gui_path + "/save_load/main_menu/save_load_button_idle.png"
    insomnia_g.navigation = False

    insomnia_rows = 4
    insomnia_cols = 3
    insomnia_cells = insomnia_rows * insomnia_cols

    insomnia_gallery_bg_list = [
    "insomnia_ext_camp_entrance_winter_day", "insomnia_ext_camp_entrance_winter_night", "insomnia_ext_clubs_winter_night", "insomnia_ext_dining_hall_away_winter_day", "insomnia_ext_dining_hall_near_winter_day",
    "insomnia_ext_house_of_mt_fog", "insomnia_ext_house_of_mt_winter_night2", "insomnia_ext_houses_winter_day", "insomnia_ext_houses_winter_night", "insomnia_ext_houst_of_mt_winter_day",
    "insomnia_ext_library_winter_day", "insomnia_ext_musclub_winter_night", "insomnia_ext_old_building_fog", "insomnia_ext_path2_fog", "insomnia_ext_road_winter_day",
    "insomnia_ext_road_winter_night", "insomnia_ext_square_fog", "insomnia_ext_square_winter_day", "insomnia_ext_square_winter_night", "insomnia_ext_winter_park", "insomnia_ext_winter_street",
    "insomnia_form", "insomnia_int_kitchen_bw", "insomnia_int_old_building_night_edited", "insomnia_lane", "insomnia_makarov_pistol", "insomnia_medical_room_celling", "insomnia_prosecutor_office",
    "insomnia_roof", "insomnia_ext_winter_forest", "insomnia_us_dv_confrontation"
    ]

    for bg in insomnia_gallery_bg_list:
        insomnia_g.button(bg)
        insomnia_g.image(im.Crop("insomnia/images/bg/" + bg + ".png", (0, 0, 1920, 1080)))
        insomnia_g.unlock("bg " + bg)

    insomnia_bar_full = Frame(insomnia_gui_path + "bar_null.png")
    insomnia_bar_null = Frame(insomnia_gui_path + "bar_full.png")
    
    insomnia_qte_buttons_dict = {
        "↑": "K_UP",
        "↓": "K_DOWN",
        "→": "K_RIGHT" 
    }

    insomnia_qte_true_button = []
    insomnia_qte_true_button_pl = []
    insomnia_qte_score = 0

    def insomnia_qte_clear():
        global insomnia_qte_score

        insomnia_qte_true_button = []
        insomnia_qte_true_button_pl = []
        insomnia_qte_score = 0

    def insomnia_qte_current_button(button, count):
        global insomnia_qte_true_button, insomnia_qte_true_button_pl                              
        
        for i in range(count): 
            for j in range(len(button)):
                for key, value in insomnia_qte_buttons_dict.iteritems():
                    if key == button[j]:
                        insomnia_qte_true_button_pl.append(key)
                        insomnia_qte_true_button.append(value)

        renpy.restart_interaction()

    def insomnia_qte_next_button():
        global insomnia_qte_score

        del insomnia_qte_true_button[0]

        insomnia_qte_score += 1

        try: 
            del insomnia_qte_true_button_pl[0]

        except: 
            pass

        renpy.restart_interaction()
 
    insomnia_qte_current_button_curried = renpy.curry(insomnia_qte_current_button)
    insomnia_qte_next_button_curried = renpy.curry(insomnia_qte_next_button)

screen insomnia_qte_time_bar(time):
    bar:
        keyboard_focus False
        left_bar insomnia_bar_full
        right_bar insomnia_bar_null
        xalign 0.5
        yalign 0.1
        left_gutter 230
        right_gutter 230
        ymaximum 300 
        ysize 300

        value AnimatedValue(old_value = 1.0, value = 0.0, range = 1.0, delay = time)

    timer time action Jump("insomnia_day1_stroll_failed")

screen insomnia_qte(button, count, time):
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

    use insomnia_qte_time_bar(time)

    on "show" action insomnia_qte_current_button_curried(button, count)     
    
    if len(insomnia_qte_true_button) != 0:
        text (u"x%s" % len(insomnia_qte_true_button)) align(.5, .1) style "insomnia_qte_text"

        add "circle_full" align (.5, .62)

        if len(insomnia_qte_true_button_pl) != 0:
            text insomnia_qte_true_button_pl[0].upper() align(.5, .6) size 84 color "#ffffff" at insomnia_zoom_qte_text

        else:
            text insomnia_qte_true_button[0].upper() align(.5, .6) size 84 color "#ffffff" at insomnia_zoom_qte_text
        
        key "{}".format(insomnia_qte_true_button[0]) action insomnia_qte_next_button_curried()

    else:
        $ insomnia_qte_clear()
        timer .01 action Return(True)

screen insomnia_main_menu():
    tag menu 
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "insomnia_main_menu_bg"
    
    if insomnia_main_menu_var:
        add "insomnia_main_menu_frame" xalign 0.5 ypos 290

        text "{font=[insomnia_diamond_girl_skinny]}Бессонница{/font}":
            size 170
            text_align 0.5
            xalign 0.5
            ypos 40
            antialias True
            kerning 2
            
        textbutton ["Начать игру"] at insomnia_buttons_atl():
            style "insomnia_main_menu_text_style"
            text_style "insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.35
            action [insomnia_set_null_cursor_curried(), SetVariable("insomnia_lock_quit_game_main_menu_var", False), Start("insomnia_day1")]
                
        textbutton "[insomnia_load_text]" at insomnia_buttons_atl():
            style "insomnia_main_menu_text_style"
            text_style "insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.475
            action [SetVariable("insomnia_main_menu_var", False), ShowMenu("insomnia_load_main_menu")]
            
        textbutton "[insomnia_preferences_text]" at insomnia_buttons_atl():
            style "insomnia_main_menu_text_style"
            text_style "insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.6
            action [SetVariable("insomnia_main_menu_var", False), ShowMenu("insomnia_preferences_main_menu")]

        textbutton "[insomnia_extra_text]" at insomnia_buttons_atl():
            style "insomnia_main_menu_text_style"
            text_style "insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.725
            action [SetVariable("insomnia_main_menu_var", False), ShowMenu("insomnia_extra")]
                
        textbutton ["Выход"] at insomnia_buttons_atl():
            style "insomnia_main_menu_text_style"
            text_style "insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.85
            action [SetVariable("insomnia_main_menu_var", False), Hide("insomnia_main_menu"), (Function(insomnia_screens_diact)), ShowMenu("main_menu")]
            
        imagebutton:
            idle "insomnia_logowhite_idle"
            hover "insomnia_logowhite_hover"
            xpos 1520
            ypos 800
            action OpenURL("https://vk.com/public176281709")
        
screen insomnia_preferences_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not insomnia_main_menu_var:        
        text "[insomnia_preferences_text]":
            font insomnia_diamond_girl_skinny
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        text "[insomnia_display_preferences_text]":
            font insomnia_diamond_girl_skinny
            size 70
            xalign 0.5
            ypos 200
            
        textbutton ["На весь экран"]:
            style "insomnia_button_none"
            text_style "insomnia_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.15
            ypos 280
            action Preference("display", "fullscreen")
            
        textbutton ["В окне"]:
            style "insomnia_button_none"
            text_align 0.5
            xalign 0.8
            ypos 280

            if not _preferences.fullscreen:
                text_style "insomnia_preferences_main_menu_text_style_inverse"

            else:
                text_style "insomnia_preferences_main_menu_text_style"

            action Preference("display", "window")

        text "{font=[insomnia_diamond_girl_skinny]}Размер шрифта{/font}":
            size 70
            xalign 0.5
            ypos 360
                
        textbutton ["Обычный"]:
            style "insomnia_button_none"
            text_style "insomnia_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.175
            ypos 440
            action SetField(persistent, "font_size", "small")
                
        textbutton ["Большой"]:
            style "insomnia_button_none"
            text_style "insomnia_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.82
            ypos 440
            action SetField(persistent, "font_size", "large")
                
        text "{font=[insomnia_diamond_girl_skinny]}Пропускать{/font}":
            size 70
            xalign 0.5
            ypos 520

        if not _preferences.skip_unseen:
            textbutton ["Виденное ранее"]:
                style "insomnia_button_none"
                text_style "insomnia_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton ["Весь текст"]:
                style "insomnia_button_none"
                text_style "insomnia_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.83
                ypos 600
                action Preference("skip", "all")
                            
        if _preferences.skip_unseen:
            textbutton ["Виденное ранее"]:
                style "insomnia_button_none"
                text_style "insomnia_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton ["Весь текст"]:
                style "insomnia_button_none"
                text_style "insomnia_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.83
                ypos 600
                action Preference("skip", "all")    
            
        text "{font=[insomnia_diamond_girl_skinny]}Громкость музыки{/font}":
            size 70
            xpos 430
            ypos 820
        bar:
            value Preference("music volume")
            right_bar insomnia_gui_path + "/preferences/main_menu/insomnia_bar_null.png"
            left_bar insomnia_gui_path + "/preferences/main_menu/insomnia_bar_full.png"
            thumb insomnia_gui_path + "/preferences/main_menu/insomnia_vthumb.png"
            xpos 975
            ypos 827
            xmaximum 400
            ymaximum 85

        textbutton "[insomnia_return_text]" at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [SetVariable("insomnia_main_menu_var", True), Hide("insomnia_preferences_main_menu"), ShowMenu("insomnia_main_menu")]
        
screen insomnia_load_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not insomnia_main_menu_var:        
        text "{font=[insomnia_diamond_girl_skinny]}Загрузка{/font}":
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        textbutton "[insomnia_return_text]" at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
            xalign 0.1
            ypos 970
            action [SetVariable("insomnia_main_menu_var", True), Hide("insomnia_load_main_menu"), ShowMenu("insomnia_main_menu")]
                    
        textbutton "[insomnia_load_text]" at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action (InsomniaFunctionCallback(insomnia_on_load_callback,selected_slot), FileLoad(selected_slot, confirm = False))
                 
        textbutton "[insomnia_delete_text]" at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
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
                        style "insomnia_save_load_button_main_menu"

                        fixed:
                            text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " " + "Пусто") + "\n" + FileSaveName(i)):
                                style "insomnia_text_save_load_main_menu"
                                xpos 15
                                ypos 15
        
screen insomnia_extra():
    modal True

    key "K_F1":
        action NullAction()
    
    if not insomnia_main_menu_var:
        add "insomnia_main_menu_frame" xalign 0.5 ypos 290

        text ["Дополнительно"]:
            size 150
            text_align 0.5
            xalign 0.5
            ypos 40
            font insomnia_diamond_girl_skinny
            antialias True
            kerning 2

        textbutton ["Тени прошлого"] at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 387
            action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2694121607")

        textbutton ["Галерея"] at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 539
            action [Hide("insomnia_extra"), ShowMenu("insomnia_background_gallery")]

        textbutton ["Достижения"] at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 677
            action [Hide("insomnia_extra"), ShowMenu("insomnia_achievements")]

        textbutton "[insomnia_return_text]" at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 822
            action [SetVariable("insomnia_main_menu_var", True), Hide("insomnia_extra"), ShowMenu("insomnia_main_menu")]

screen insomnia_achievements:
    modal True

    if not insomnia_main_menu_var:
        text ["Достижения"]:
            font insomnia_diamond_girl_skinny
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        if not persistent.insomnia_achievements["insomnia_murderous_snowball"]:
            add "insomnia_locked" xalign 0.5 ypos 268

        else:
            add "insomnia_murderous_snowball" xalign 0.5 ypos 268

        if not persistent.insomnia_achievements["insomnia_awakening"]:
            add "insomnia_locked" xalign 0.5 ypos 507

        else:
            add "insomnia_awakening" xalign 0.5 ypos 507

        if not persistent.insomnia_achievements["insomnia_paradise"]:
            add "insomnia_locked" xalign 0.5 ypos 745

        else:
            add "insomnia_paradise" xalign 0.5 ypos 745

        textbutton "[insomnia_return_text]" at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [Hide("insomnia_achievements"), ShowMenu("insomnia_extra")]

screen insomnia_background_gallery():
    modal True

    if not insomnia_main_menu_var:
        $ insomnia_gallery_table = insomnia_gallery_bg_list

        $ insomnia_len_table = len(insomnia_gallery_bg_list)

        text "{font=[insomnia_diamond_girl_skinny]}Галерея{/font}":
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        textbutton "[insomnia_return_text]" at insomnia_buttons_atl():
            style "insomnia_button_none" 
            text_style "insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [Hide("insomnia_background_gallery"), ShowMenu("insomnia_extra")]

        grid insomnia_rows insomnia_cols xpos 0.09 ypos 0.18:
            $ insomnia_bg_displayed = 0
            $ insomnia_next_page = insomnia_page + 1

            if insomnia_next_page > int(insomnia_len_table / insomnia_cells):
                $ insomnia_next_page = 0

            for n in range(insomnia_len_table):
                if n < (insomnia_page + 1) * insomnia_cells and n >= insomnia_page * insomnia_cells:
                    $ _insomnia_t = im.Crop("insomnia/images/bg/" + insomnia_gallery_table[n] + ".png", (0, 0, 1920, 1080))
                            
                    $ _insomnia_img_scaled = im.Scale(_insomnia_t, 320, 180)

                    $ insomnia_img = im.Composite((336, 196), (8, 8), im.Alpha(_insomnia_img_scaled, 0.9), (0, 0), im.Image(insomnia_gui_path + "/save_load/main_menu/save_load_button_idle.png"))
                    $ insomnia_imgh = im.Composite((336, 196), (8, 8), _insomnia_img_scaled, (0, 0), im.Image(insomnia_gui_path + "/save_load/main_menu/save_load_button_hover.png"))

                    add insomnia_g.make_button(insomnia_gallery_table[n], get_image("gui/gallery/blank.png"), None, insomnia_imgh, insomnia_img , style = "blank_button", bottom_margin = 50, right_margin = 50)

                    $ insomnia_bg_displayed += 1

                    if n + 1 == insomnia_len_table:
                        $ insomnia_next_page = 0

            for j in range(0, insomnia_cells - insomnia_bg_displayed):
                null

        if insomnia_page != 0:
            imagebutton:
                idle "insomnia/images/gui/dialogue_box/backward_idle.png"
                hover "insomnia/images/gui/dialogue_box/winter_night/backward_hover.png"
                yalign 0.5 
                xalign 0.01 
                action [SetVariable("insomnia_page", insomnia_page - 1), ShowMenu("insomnia_background_gallery")]

        if insomnia_page != int(insomnia_page_counter(insomnia_len_table, insomnia_cells)) - 1:
            imagebutton: 
                idle "insomnia/images/gui/dialogue_box/forward_idle.png"
                hover "insomnia/images/gui/dialogue_box/winter_night/forward_hover.png"
                yalign 0.5 
                xalign 0.99 
                action [SetVariable("insomnia_page", insomnia_next_page), ShowMenu("insomnia_background_gallery")]
        
screen insomnia_preferences():
    tag menu
    modal True
    
    key "K_F1":
        action NullAction()
    
    add insomnia_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"
    
    text ["Настройки"]:
        size 70
        xalign 0.5
        yalign 0.062
        font insomnia_flow_ext
        antialias True
        kerning 2
        
    text ["Режим экрана"]:
        font insomnia_flow_ext
        size 65
        xalign 0.5
        ypos 190
        
    textbutton ["На весь экран"]:
        style "insomnia_button_none"
        text_style "insomnia_text_preferences_" + persistent.timeofday
        xalign 0.15
        ypos 270
        action Preference("display", "fullscreen")
        
    textbutton ["В окне"]:
        style "insomnia_button_none"
        text_style "insomnia_text_preferences_" + persistent.timeofday
        xalign 0.8
        ypos 275

        if not _preferences.fullscreen:
            text_style "insomnia_text_inverse_preferences_" + persistent.timeofday

        else:
            text_style "insomnia_text_preferences_" + persistent.timeofday

        action Preference("display", "window")

    text ["Размер шрифта"]:
        font insomnia_flow_ext
        size 65
        xalign 0.5
        ypos 395
        
    textbutton ["Обычный"]:
        style "insomnia_button_none"
        text_style "insomnia_text_preferences_" + persistent.timeofday
        xalign 0.175
        ypos 475
        action SetField(persistent, "font_size", "small")
        
    textbutton ["Большой"]:
        style "insomnia_button_none"
        text_style "insomnia_text_preferences_" + persistent.timeofday
        xalign 0.82
        ypos 475
        action SetField(persistent, "font_size", "large")
        
    textbutton ["Музыка"]:
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        xpos 430
        ypos 665
    bar:
        value Preference("music volume")
        right_bar insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_bar_null.png"
        left_bar insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_bar_full.png"
        thumb insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_thumb.png"
        xpos 975
        ypos 670
        xmaximum 400
        ymaximum 85
        
    textbutton ["Звуки"]:
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        xpos 425
        ypos 779
    bar:
        value Preference("sound volume")
        right_bar insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_bar_null.png"
        left_bar insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_bar_full.png"
        thumb insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_thumb.png"
        xpos 975
        ypos 785
        xmaximum 400
        ymaximum 85

    textbutton ["Эмбиент"]:
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        xpos 422
        ypos 895
    bar:
        value Preference("voice volume")
        right_bar insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_bar_null.png"
        left_bar insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_bar_full.png"
        thumb insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_thumb.png"
        xpos 975
        ypos 901
        xmaximum 400
        ymaximum 85     

    textbutton ["Назад"]:
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        xpos 235
        ypos 970
        action [Hide("insomnia_preferences"), Return()]

screen insomnia_save():
    tag menu
    modal True
    
    add insomnia_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"

    text ["Сохранение"]:
        size 70
        xalign 0.5
        yalign 0.062
        font insomnia_flow_ext
        antialias True
        kerning 2

    textbutton "[insomnia_return_text]": 
        style "insomnia_button_none"
        text_style "insomnia_save_load_" + persistent.timeofday
        xalign 0.12 
        yalign 0.97
        action Return()

    textbutton ["Сохранить"]: 
        style "insomnia_button_none"
        text_style "insomnia_save_load_" + persistent.timeofday
        xalign 0.5
        yalign 0.97
        action (InsomniaFunctionCallback(insomnia_on_save_callback,selected_slot), FileSave(selected_slot))

    textbutton "[insomnia_delete_text]": 
        style "insomnia_button_none"
        text_style "insomnia_save_load_" + persistent.timeofday
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
                    style "insomnia_save_load_button_" + persistent.timeofday
                    has fixed
                    text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " " +translation_new["Empty_slot"]) + "\n" +FileSaveName(i)) style "insomnia_text_save_load_main_menu" xpos 15 ypos 15
    
screen insomnia_load():
    tag menu
    modal True
    
    add insomnia_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"

    text ["Загрузка"]:
        size 70
        xalign 0.5
        yalign 0.062
        font insomnia_flow_ext
        antialias True
        kerning 2

    textbutton "[insomnia_return_text]":
        style "insomnia_button_none"
        text_style "insomnia_save_load_" + persistent.timeofday
        xalign 0.12 
        yalign 0.97 
        action Return()

    textbutton ["Загрузить"]:
        style "insomnia_button_none"
        text_style "insomnia_save_load_" + persistent.timeofday
        xalign 0.5
        yalign 0.97
        action (InsomniaFunctionCallback(insomnia_on_load_callback,selected_slot), FileLoad(selected_slot, confirm = False))
    
    textbutton "[insomnia_delete_text]":
        style "insomnia_button_none"
        text_style "insomnia_save_load_" + persistent.timeofday
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
                    style "insomnia_save_load_button_" + persistent.timeofday
                    has fixed
                    text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " " + translation_new["Empty_slot"]) + "\n" + FileSaveName(i)) style "insomnia_text_save_load_main_menu" xpos 15 ypos 15
                                
screen insomnia_say(what, who):    
    window background None id "window":
        if persistent.font_size == "large":
            add insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box_large.png" xpos -6 ypos 770

            imagebutton:
                idle insomnia_gui_path + "dialogue_box/backward_idle.png"
                hover insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_hover.png"
                xpos 38 
                ypos 924 
                action ShowMenu("insomnia_text_history")

            if not config.skipping:
                imagebutton:
                    idle insomnia_gui_path + "dialogue_box/forward_idle.png"
                    hover insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_hover.png"
                    xpos 1768 
                    ypos 924 
                    action Skip()

            else:
                imagebutton: 
                    idle insomnia_gui_path + "dialogue_box/fast_forward_idle.png"
                    hover insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_hover.png"
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
            add insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box.png" xpos -6 ypos 800

            imagebutton:
                idle insomnia_gui_path + "dialogue_box/backward_idle.png"
                hover insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_hover.png"
                xpos 38 
                ypos 949 
                action ShowMenu("insomnia_text_history")

            if not config.skipping:
                imagebutton:
                    idle insomnia_gui_path + "dialogue_box/forward_idle.png"
                    hover insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_hover.png"
                    xpos 1768 
                    ypos 949 
                    action Skip()

            else:
                imagebutton:
                    idle insomnia_gui_path + "dialogue_box/fast_forward_idle.png"
                    hover insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_hover.png"
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

screen insomnia_nvl(items, dialogue):
    window background Frame((insomnia_gui_path + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
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
        idle insomnia_gui_path + "dialogue_box/backward_idle.png"
        hover insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_hover.png"
        xpos 38 
        ypos 924
        action ShowMenu("insomnia_text_history")

    if not config.skipping:
        imagebutton:
            idle insomnia_gui_path + "dialogue_box/forward_idle.png"
            hover insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_hover.png"
            xpos 1768
            ypos 949
            action Skip()

    else:
        imagebutton:
            idle insomnia_gui_path + "dialogue_box/fast_forward_idle.png"
            hover insomnia_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_hover.png"
            xpos 1768
            ypos 949
            action Skip()

screen insomnia_game_menu_selector():
    tag menu
    modal True

    if insomnia_lock_quick_menu:
        timer 0.01 action Return()

    else:
        button style "blank_button" xfill True yfill True action Return()

        add insomnia_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_ground.png" xalign 0.5 yalign 0.5
    
        text "{font=[insomnia_flow_ext]}Пауза{/font}":
            size 80
            xalign 0.5
            ypos 274
            antialias True
            kerning 2
            
        textbutton ["В главное меню"]:
            style "insomnia_button_none"
            text_style "insomnia_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 418
            action [insomnia_set_main_menu_cursor_curried(), MainMenu(confirm = False)]
            
        textbutton ["Сохранить"]:
            style "insomnia_button_none"
            text_style "insomnia_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 505
            action ShowMenu("insomnia_save")
            
        textbutton ["Загрузить"]:
            style "insomnia_button_none"
            text_style "insomnia_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 593
            action ShowMenu("insomnia_load")
            
        textbutton ["Настройки"]:
            style "insomnia_button_none"
            text_style "insomnia_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 680
            action ShowMenu("insomnia_preferences")
            
        textbutton ["Выход"]:
            style "insomnia_button_none"
            text_style "insomnia_quick_menu_style_" + persistent.timeofday
            xalign 0.5
            ypos 765
            action [(Function(insomnia_screens_diact)), ShowMenu("main_menu")]

screen insomnia_quit():
    tag menu
    modal True

    if insomnia_lock_quit:
        timer 0.01 action Return()

    elif insomnia_lock_quit_game_main_menu_var:
        timer 0.01 action Quit(confirm = False)

    else:
        add insomnia_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"
            
        text ["Вы действительно \nхотите выйти?"]:
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2
            font insomnia_diamond_girl_skinny
            
        textbutton "[insomnia_yes_text]":
            style "insomnia_button_none"
            text_style "insomnia_text_" + persistent.timeofday
            xalign 0.3
            ypos 650
            action [(Function(insomnia_screens_diact)), ShowMenu("main_menu")]
            
        textbutton "[insomnia_no_text]":
            style "insomnia_button_none"
            text_style "insomnia_text_" + persistent.timeofday
            xalign 0.7
            ypos 650
            action [Hide("insomnia_quit"), Return()]

screen insomnia_yesno_prompt(yes_action, message, no_action):
    modal True

    add insomnia_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"

    $ insomnia_yesno_prompt_colors = {
        "winter_day": "#64483c",
        "winter_night": "#161d3d",
        "fog": "#008193",
        "bw": "#5a3525"
    }

    text _(message):
        text_align 0.5 
        yalign 0.46 
        xalign 0.5
        font insomnia_diamond_girl_skinny 
        size 100

    textbutton "[insomnia_yes_text]": 
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        yalign 0.68 
        xalign 0.3 
        action yes_action

    textbutton "[insomnia_no_text]": 
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        yalign 0.68 
        xalign 0.7 
        action no_action

screen insomnia_text_history():
    tag menu
    predict False

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    $ insomnia_text_history_color = {                        
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

    window background Frame(insomnia_gui_path + "choice/" + persistent.timeofday + "/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:
        viewport id "insomnia_text_history_screen":
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
                    style "insomnia_button_none" 
                    text_style "insomnia_text_history" 
                    xpos 100                    
                    xmaximum xmax
                    text_hover_color insomnia_text_history_color[persistent.timeofday]                    
                    action RollbackToIdentifier(h.rollback_identifier) 
        
        vbar value YScrollValue("insomnia_text_history_screen") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb insomnia_gui_path + "preferences/" + persistent.timeofday + "/insomnia_thumb.png" xoffset 1700  

screen insomnia_choice(items):
    modal True

    $ insomnia_choice_color = "#ffffff"

    $ insomnia_choice_color_selected = "#808080"

    $ insomnia_choice_colors_hover = {                        
        "winter_day": "#2171b8",
        "winter_night": "#0143b3",
        "fog": "#c2dded",
        "bw": "#dcd168"
                        }

    window background Frame((insomnia_gui_path + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yalign 0.5 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:
        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:
                button background None:
                    xalign 0.5
                    action action

                    if persistent.licensed:
                        if caption in persistent.choices and caption != "Налево" and caption != "Направо" and caption != "Go left" and caption != "Go right" and caption != "Ir a la izquierda" and caption != "Ir a la derecha":
                            text caption font header_font size 37 hover_size 37 color insomnia_choice_color_selected hover_color insomnia_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5
                            
                        else:
                            text caption font header_font size 37 hover_size 37 color insomnia_choice_color hover_color insomnia_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5

                    else:
                        text caption font header_font size 37 hover_size 37 color insomnia_choice_color hover_color insomnia_choice_colors_hover[persistent.timeofday] xalign 0.5

            else:
                if persistent.licensed:
                    text caption font header_font size 60 color insomnia_choice_color text_align 0.5 xcenter 0.5

                else:
                    text caption font header_font size 40 color insomnia_choice_color xalign 0.5 text_align 0.5 xcenter 0.5

screen insomnia_help():
    tag menu
    modal True
    
    add insomnia_gui_path + "save_load_preferences/" + persistent.timeofday + "/save_load_preferences_bg.png"
    
    text ["Информация"]:
        size 70
        xalign 0.5
        ypos 33
        antialias True
        kerning 2
        font insomnia_diamond_girl_skinny

    textbutton ["Группа VK"]:
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        xalign 0.5
        ypos 280
        action OpenURL("https://vk.com/public176281709")
            
    textbutton ["Яна"]:
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        xalign 0.5
        ypos 410
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2239853287")

    textbutton ["Один украденный день"]:
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        xalign 0.5
        ypos 530
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=1746278653")   
            
    textbutton ["Петля времени"]:
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        xalign 0.5
        ypos 650
        action OpenURL("https://youtu.be/x2KBAuBKWL8")

    add "insomnia_logowhite_hover" xpos 1520 ypos 880

    textbutton "[insomnia_return_text]":
        style "insomnia_button_none"
        text_style "insomnia_text_" + persistent.timeofday
        xalign 0.5 
        yalign 0.92 
        action Return()