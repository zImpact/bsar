init python:
    bsar_insomnia_gallery = Gallery()
    bsar_insomnia_gallery_page = 0
    bsar_insomnia_gallery.transition = fade
    bsar_insomnia_gallery.locked_button = bsar_gui_path + "misc/insomnia_gallery_locked_button.png"
    bsar_insomnia_gallery.navigation = False

    bsar_insomnia_gallery_bg_list = [
    "ext_camp_entrance_winter_day", "ext_camp_entrance_winter_night", "ext_clubs_winter_night",
    "ext_dining_hall_away_winter_day", "ext_dining_hall_near_winter_day", "ext_house_of_mt_fog", 
    "ext_house_of_mt_winter_night2", "ext_houses_winter_day", "ext_houses_winter_night", 
    "ext_houst_of_mt_winter_day", "ext_library_winter_day", "ext_musclub_winter_night", 
    "ext_old_building_fog", "ext_path2_fog", "ext_road_winter_day", "ext_square_fog", "ext_square_winter_day",
    "ext_square_winter_night", "int_old_building_night_edited", 
    "ext_winter_forest", 
    "us_dv_confrontation"
    ]

    for bg in bsar_insomnia_gallery_bg_list:
        bsar_insomnia_gallery.button(bg)
        bsar_insomnia_gallery.image(im.Crop("bsar/images/bg/" + bg + ".png", (0, 0, 1920, 1080)))
        bsar_insomnia_gallery.unlock("bg " + bsar_prefix + bg)

    bsar_insomnia_music_box = {
        "Domitori Taranofu — Slow Pulse": bsar_domitori_taranofu_slow_pulse,
        "Katawa Shoujo OST — Afternoon": bsar_afternoon,
        "Katawa Shoujo OST — Ease": bsar_ease,
        "Katawa Shoujo OST — Stride": bsar_stride,
        "Lucas King — Isolation": bsar_lucas_king_isolation,
        "Domitori Taranofu — Trouble": bsar_domitori_taranofu_trouble,
        "Lucius OST — Piano": bsar_lucius_OST_piano,
        "Katawa Shoujo OST — Everyday Fantasy": bsar_everyday_fantasy,
        "Over The Time — Sandy Winter": bsar_over_the_time_sandy_winter,
        "Insomnia — Standing Tail": bsar_standing_tall,
        "Cyprinid — Floating": bsar_cyprinid_floating,
        "K.S. OST — Painful History": bsar_painful_history,
        "Domitori Taranofu — Planet Of Colds": bsar_domitori_taranofu_planet_of_colds,
        "Katawa Shoujo OST — Fripperies": bsar_fripperies,
        "Domitori Taranofu — Winter Night": bsar_domitori_taranofu_winter_night,
        "Insomnia — Dark Shades": bsar_dark_shades,
        "Domitori Taranofu — Lullaby": bsar_domitori_taranofu_lullaby
    }

    bsar_insomnia_mr = MusicRoom(fadeout=1.0)

    for music_name in bsar_insomnia_music_box.values():
        bsar_insomnia_mr.add(music_name)

screen bsar_insomnia_main_menu():
    tag menu 
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "bsar_insomnia_main_menu_bg"

    on "show" action Play("music", ["<silence 1.5>", bsar_domitori_taranofu_lullaby], if_changed=True)
    
    if bsar_insomnia_main_menu_var:
        add bsar_gui_path + "insomnia_main_menu/main_menu_frame.png" xalign 0.5 ypos 290

        text "Бессонница":
            size 170
            xalign 0.5
            ypos 40
            font bsar_diamond_girl_skinny
            text_align 0.5
            antialias True
            kerning 2
            
        textbutton "Начать игру" at bsar_buttons_atl():
            style "bsar_insomnia_main_menu_text_style"
            text_style "bsar_insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.35
            action [
                SetVariable("bsar_lock_quit_game_main_menu_var", False), 
                Start("bsar_insomnia_day1")
            ]
                
        textbutton "Загрузить" at bsar_buttons_atl():
            style "bsar_insomnia_main_menu_text_style"
            text_style "bsar_insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.475
            action [
                SetVariable("bsar_insomnia_main_menu_var", False), 
                ShowMenu("bsar_insomnia_load_main_menu")
            ]
            
        textbutton "Настройки" at bsar_buttons_atl():
            style "bsar_insomnia_main_menu_text_style"
            text_style "bsar_insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.6
            action [
                SetVariable("bsar_insomnia_main_menu_var", False), 
                ShowMenu("bsar_insomnia_preferences_main_menu")
            ]

        textbutton "Дополнительно" at bsar_buttons_atl():
            style "bsar_insomnia_main_menu_text_style"
            text_style "bsar_insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.725
            action [
                SetVariable("bsar_insomnia_main_menu_var", False), 
                ShowMenu("bsar_insomnia_extra")
            ]
                
        textbutton "Выход" at bsar_buttons_atl():
            style "bsar_insomnia_main_menu_text_style"
            text_style "bsar_insomnia_main_menu_text_style"
            xalign 0.5
            yalign 0.85
            action [
                SetVariable("bsar_insomnia_main_menu_var", False), 
                Hide("bsar_insomnia_main_menu"), 
                Function(bsar_screens_diact), 
                ShowMenu("main_menu")
            ]
        
        if bsar_check_sotp("allow"):
            imagebutton:
                auto bsar_gui_path + "insomnia_main_menu/to_sotp_%s.png"
                xpos 130
                ypos 755
                action [
                    SetField(persistent, "bsar_current_story", "sotp"),
                    Stop("music", fadeout=1.0),
                    Hide("bsar_insomnia_main_menu"),
                    Function(bsar_toggle_main_menu),
                    ShowMenu("bsar_sotp_main_menu", _transition=bsar_fadehold),
                    Play("music", ["<silence 1.5>", bsar_master_of_spirits_shadows_main_theme], fadein=1.0)
                ]
            
        imagebutton:
            auto bsar_gui_path + "insomnia_main_menu/logowhite_%s.png"
            xpos 1520
            ypos 800
            action OpenURL("https://vk.com/public176281709")
        
screen bsar_insomnia_preferences_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not bsar_insomnia_main_menu_var:        
        text "Настройки":
            font bsar_diamond_girl_skinny
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        text "Режим экрана":
            font bsar_diamond_girl_skinny
            size 70
            xalign 0.5
            ypos 200
            
        textbutton "На весь экран":
            style "bsar_button_none"
            text_style "bsar_insomnia_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.15
            ypos 280
            action Preference("display", "fullscreen")
            
        textbutton "В окне":
            style "bsar_button_none"
            text_align 0.5
            xalign 0.8
            ypos 280

            if not _preferences.fullscreen:
                text_style "bsar_insomnia_preferences_main_menu_text_style_inverse"

            else:
                text_style "bsar_insomnia_preferences_main_menu_text_style"

            action Preference("display", "window")

        text "Размер шрифта":
            font bsar_diamond_girl_skinny
            size 70
            xalign 0.5
            ypos 360
                
        textbutton "Обычный":
            style "bsar_button_none"
            text_style "bsar_insomnia_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.175
            ypos 440
            action SetField(persistent, "font_size", "small")
                
        textbutton "Большой":
            style "bsar_button_none"
            text_style "bsar_insomnia_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.82
            ypos 440
            action SetField(persistent, "font_size", "large")
                
        text "Пропускать":
            font bsar_diamond_girl_skinny
            size 70
            xalign 0.5
            ypos 520

        if not _preferences.skip_unseen:
            textbutton "Виденное ранее":
                style "bsar_button_none"
                text_style "bsar_insomnia_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "Весь текст":
                style "bsar_button_none"
                text_style "bsar_insomnia_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.83
                ypos 600
                action Preference("skip", "all")
                            
        if _preferences.skip_unseen:
            textbutton "Виденное ранее":
                style "bsar_button_none"
                text_style "bsar_insomnia_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "Весь текст":
                style "bsar_button_none"
                text_style "bsar_insomnia_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.83
                ypos 600
                action Preference("skip", "all")    
            
        text "Громкость музыки":
            font bsar_diamond_girl_skinny
            size 70
            xpos 430
            ypos 820
        bar:
            value Preference("music volume")
            right_bar bsar_gui_path + "preferences/insomnia_main_menu/bar_null.png"
            left_bar bsar_gui_path + "preferences/insomnia_main_menu/bar_full.png"
            thumb bsar_gui_path + "preferences/insomnia_main_menu/vthumb.png"
            xpos 975
            ypos 827
            xmaximum 400
            ymaximum 85

        textbutton "Назад" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [
                SetVariable("bsar_insomnia_main_menu_var", True),
                Hide("bsar_insomnia_preferences_main_menu"),
                ShowMenu("bsar_insomnia_main_menu")
            ]
        
screen bsar_insomnia_load_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not bsar_insomnia_main_menu_var:        
        text "Загрузка":
            font bsar_diamond_girl_skinny
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        textbutton "Назад" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.1
            ypos 970
            action [
                SetVariable("bsar_insomnia_main_menu_var", True),
                Hide("bsar_insomnia_load_main_menu"),
                ShowMenu("bsar_insomnia_main_menu")
            ]
                    
        textbutton "Загрузить" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [
                BsarFunctionCallback(bsar_on_load_callback, selected_slot), 
                FileLoad(selected_slot, confirm=False)
            ]
                 
        textbutton "Удалить" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.9
            ypos 970
            action FileDelete(selected_slot, confirm=False)
            
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
                        style "bsar_insomnia_save_load_button_main_menu"

                        fixed:
                            text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty= " Пусто") + "\n" + FileSaveName(i)):
                                style "bsar_text_save_load_main_menu"
                                xpos 15
                                ypos 15
        
screen bsar_insomnia_extra():
    modal True

    key "K_F1":
        action NullAction()
    
    if not bsar_insomnia_main_menu_var:
        add bsar_gui_path + "insomnia_main_menu/main_menu_frame.png" xalign 0.5 ypos 290

        text "Дополнительно":
            size 150
            text_align 0.5
            xalign 0.5
            ypos 40
            font bsar_diamond_girl_skinny
            antialias True
            kerning 2

        textbutton "Музыка" at bsar_buttons_atl():
            style "bsar_button_none"
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.5
            yalign 0.35
            action [
                Hide("bsar_insomnia_extra"),
                ShowMenu("bsar_insomnia_music_room")
            ]

        textbutton "Галерея" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.5
            yalign 0.5
            action [
                Hide("bsar_insomnia_extra"),
                ShowMenu("bsar_insomnia_background_gallery")
            ]

        textbutton "Достижения" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.5
            yalign 0.65
            action [
                Hide("bsar_insomnia_extra"),
                ShowMenu("bsar_insomnia_achievements")
            ]

        textbutton "Назад" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.5
            yalign 0.85
            action [
                SetVariable("bsar_insomnia_main_menu_var", True),
                Hide("bsar_insomnia_extra"), 
                ShowMenu("bsar_insomnia_main_menu")
            ]

screen bsar_insomnia_achievements():
    modal True

    if not bsar_insomnia_main_menu_var:
        text "Достижения":
            font bsar_diamond_girl_skinny
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        add bsar_gui_path + "insomnia_main_menu/achievements_frame.png" xpos 90 ypos 190

        add bsar_gui_path + "insomnia_main_menu/achievements_frame.png" xpos 697 ypos 190

        add bsar_gui_path + "insomnia_main_menu/achievements_frame.png" xpos 1304 ypos 190

        $ insomnia_achievements = {
            "paradise": {
                "ach_xpos": 140,
                "text": "Как бы сладок не\nбыл сон, но за ним\nвсегда следует\nпробуждение.\nВозвращение из\nмира грёз, надежд и\nфантазий в суровую\nреальность...",
                "text_xpos": 185
            },
            "awakening": {
                "ach_xpos": 747,
                "text": "У каждого человека\nесть воспоминание, в\nкотором он бы хотел\nостаться навсегда.\nГрустная правда\nжизни в том, что в\nнашем мире это\nневозможно.",
                "text_xpos": 767
            },
            "murderous_snowball": {
                "ach_xpos": 1354,
                "text": "Тут нет морали или\nжитейской мудрости.\nПросто напоминание\nо том, человек\nсмертен. Проблема в\nтом, что он\nиногда\nвнезапно смертен.",
                "text_xpos": 1369
            }
        }

        for achievement, info in insomnia_achievements.items():
            if persistent.bsar_achievements.get("insomnia_" + achievement, False):
                add bsar_gui_path + "achievements/insomnia/" + achievement + ".png" xpos info["ach_xpos"] ypos 265

                text info["text"]:
                    font bsar_flow_ext
                    size 40
                    xpos info["text_xpos"]
                    ypos 405
            else:
                add bsar_gui_path + "achievements/insomnia/locked.png" xpos info["ach_xpos"] ypos 490

        textbutton "Назад" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [
                Hide("bsar_insomnia_achievements"),
                ShowMenu("bsar_insomnia_extra")
            ]

screen bsar_insomnia_background_gallery():
    modal True

    if not bsar_insomnia_main_menu_var:
        $ bsar_insomnia_gallery_table = bsar_insomnia_gallery_bg_list
        $ bsar_insomnia_len_table = len(bsar_insomnia_gallery_bg_list)

        text "Галерея":
            font bsar_diamond_girl_skinny
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        textbutton "Назад" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [
                Hide("bsar_insomnia_background_gallery"),
                ShowMenu("bsar_insomnia_extra")
            ]

        grid bsar_gallery_rows bsar_gallery_cols xpos 0.09 ypos 0.18:
            $ bsar_insomnia_gallery_bg_displayed = 0
            $ bsar_insomnia_gallery_next_page = bsar_insomnia_gallery_page + 1

            if bsar_insomnia_gallery_next_page > int(bsar_insomnia_len_table / bsar_gallery_cells):
                $ bsar_insomnia_gallery_next_page = 0

            for n in range(bsar_insomnia_len_table):
                if n < (bsar_insomnia_gallery_page + 1) * bsar_gallery_cells and n >= bsar_insomnia_gallery_page * bsar_gallery_cells:
                    $ _bsar_t = im.Crop(
                        "bsar/images/bg/" + bsar_insomnia_gallery_table[n] + ".png",
                        (0, 0, 1920, 1080)
                    )
                            
                    $ _bsar_img_scaled = im.Scale(_bsar_t, 320, 180)

                    $ bsar_img = im.Composite(
                        (336, 196),
                        (8, 8),
                        im.Alpha(_bsar_img_scaled, 0.9),
                        (0, 0),
                        im.Image(bsar_gui_path + "save_load/insomnia_main_menu/save_load_button_idle.png")
                    )

                    $ bsar_imgh = im.Composite(
                        (336, 196),
                        (8, 8),
                        _bsar_img_scaled,
                        (0, 0),
                        im.Image(bsar_gui_path + "save_load/insomnia_main_menu/save_load_button_hover.png")
                    )

                    add bsar_insomnia_gallery.make_button(
                        bsar_insomnia_gallery_table[n], 
                        get_image("gui/gallery/blank.png"), 
                        None,
                        bsar_imgh,
                        bsar_img,
                        style="blank_button",
                        bottom_margin=50,
                        right_margin=50
                    )

                    $ bsar_insomnia_gallery_bg_displayed += 1

                    if n + 1 == bsar_insomnia_len_table:
                        $ bsar_insomnia_gallery_next_page = 0

            for j in range(0, bsar_gallery_cells - bsar_insomnia_gallery_bg_displayed):
                null

        if bsar_insomnia_gallery_page != 0:
            imagebutton:
                idle bsar_gui_path + "dialogue_box/backward_idle.png"
                hover bsar_gui_path + "dialogue_box/winter_night/backward_hover.png"
                yalign 0.5 
                xalign 0.01 
                action [
                    SetVariable("bsar_insomnia_gallery_page", bsar_insomnia_gallery_page - 1),
                    ShowMenu("bsar_insomnia_background_gallery")
                ]

        if bsar_insomnia_gallery_page != int(bsar_gallery_page_counter(bsar_insomnia_len_table, bsar_gallery_cells)) - 1:
            imagebutton: 
                idle bsar_gui_path + "dialogue_box/forward_idle.png"
                hover bsar_gui_path + "dialogue_box/winter_night/forward_hover.png"
                yalign 0.5 
                xalign 0.99 
                action [
                    SetVariable("bsar_insomnia_gallery_page", bsar_insomnia_gallery_next_page), 
                    ShowMenu("bsar_insomnia_background_gallery")
                ]

screen bsar_insomnia_music_room():
    modal True

    if not bsar_insomnia_main_menu_var:
        text "Музыка":
            font bsar_diamond_girl_skinny
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        frame:
            background None

            side "c r":
                area (0.3, 0.25, 0.65, 0.73)

                viewport:
                    id "bsar_insomnia_music_box"
                    draggable True
                    mousewheel True
                    scrollbars None
                    
                    grid 1 len(bsar_insomnia_music_box):
                        for name, track in sorted(bsar_insomnia_music_box.iteritems()):
                            textbutton name:
                                style "bsar_button_none"
                                text_style "bsar_insomnia_main_menu_music_text_style"
                                xalign 0.5
                                action bsar_insomnia_mr.Play(track)

                vbar:
                    value YScrollValue("bsar_insomnia_music_box")
                    bottom_bar bsar_gui_path + "insomnia_main_menu/main_menu_vbar_null.png"
                    top_bar bsar_gui_path + "insomnia_main_menu/main_menu_vbar_full.png"
                    thumb None
                    xmaximum 52

        textbutton "Назад" at bsar_buttons_atl():
            style "bsar_button_none" 
            text_style "bsar_insomnia_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [
                Hide("bsar_insomnia_music_room"),
                ShowMenu("bsar_insomnia_extra")
            ]

        on "replaced" action Play("music", bsar_domitori_taranofu_lullaby)