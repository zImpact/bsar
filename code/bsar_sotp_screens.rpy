init python:
    bsar_sotp_gallery = Gallery()
    bsar_sotp_gallery_page = 0
    bsar_sotp_gallery.transition = fade
    bsar_sotp_gallery.locked_button = bsar_gui_path + "misc/sotp_gallery_locked_button.png"
    bsar_sotp_gallery.navigation = False

    bsar_sotp_gallery_bg_list = [
        "ext_lane", "ext_living_buildings", "ext_living_buildings_fence",
        "ext_prosecutor_office", "ext_roof", "ext_winter_park",
        "ext_winter_street", "form", "int_abandoned_workshop",
        "int_alcotable", "int_cammunal", "int_float",
        "int_kitchen_bw", "int_od_cabinet", "int_protagonist_room",
        "int_tish_interrogation", "makarov_pistol", "medical_room_celling",
        "skazaev_prosecutor_office", "thermal_power_plant"
    ]

    for bg in bsar_sotp_gallery_bg_list:
        bsar_sotp_gallery.button(bg)
        bsar_sotp_gallery.image(im.Crop("bsar/images/bg/" + bg + ".png", (0, 0, 1920, 1080)))
        bsar_sotp_gallery.unlock("bg " + bsar_prefix + bg)

screen bsar_sotp_main_menu():
    tag menu 
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "bsar_sotp_main_menu_bg"

    add bsar_gui_path + "sotp_main_menu/main_menu_vingette.png"

    on "show" action Play("music", ["<silence 1.5>", bsar_master_of_spirits_shadows_main_theme], if_changed=True)
    
    if bsar_sotp_main_menu_var:
        text "Тени прошлого":
            size 170
            xalign 0.5
            ypos 40
            font bsar_yanone_kaffeesatz_regular
            text_align 0.5
            antialias True
            kerning 2
            
        imagebutton:
            auto bsar_gui_path + "sotp_main_menu/buttons/choose_story_%s.png" 
            xalign 0.5
            yalign 0.35
            action ShowMenu("bsar_sotp_choose_story")
                
        imagebutton:
            auto bsar_gui_path + "sotp_main_menu/buttons/load_%s.png"
            xalign 0.5
            yalign 0.475
            action [
                SetVariable("bsar_sotp_main_menu_var", False), 
                ShowMenu("bsar_sotp_load_main_menu")
            ]
            
        imagebutton:
            auto bsar_gui_path + "sotp_main_menu/buttons/preferences_%s.png"
            xalign 0.5
            yalign 0.6
            action [
                SetVariable("bsar_sotp_main_menu_var", False),
                ShowMenu("bsar_sotp_preferences_main_menu")
            ]

        imagebutton:
            auto bsar_gui_path + "sotp_main_menu/buttons/extra_%s.png"
            xalign 0.5
            yalign 0.725
            action [
                SetVariable("bsar_sotp_main_menu_var", False), 
                ShowMenu("bsar_sotp_extra")
            ]
                
        imagebutton:
            auto bsar_gui_path + "sotp_main_menu/buttons/quit_%s.png"
            xalign 0.5
            yalign 0.85
            action [
                SetVariable("bsar_sotp_main_menu_var", False),
                Hide("bsar_sotp_main_menu"), 
                Function(bsar_screens_diact), 
                ShowMenu("main_menu")
            ]

        imagebutton:
            auto bsar_gui_path + "sotp_main_menu/to_insomnia_%s.png"
            xpos 130
            ypos 755
            action [
                SetField(persistent, "bsar_current_story", "insomnia"),
                Stop("music", fadeout=1.0),
                Hide("bsar_sotp_main_menu"),
                Function(bsar_toggle_main_menu),
                ShowMenu("bsar_insomnia_main_menu", _transition=bsar_fadehold),
                Play("music", ["<silence 1.5>", bsar_domitori_taranofu_lullaby], fadein=1.0)
            ]

        imagebutton:
            auto bsar_gui_path + "sotp_main_menu/logowhite_%s.png"
            xpos 1520
            ypos 800
            action OpenURL("https://vk.com/public176281709")

screen bsar_sotp_choose_story():
    tag menu 
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add bsar_gui_path + "sotp_main_menu/main_menu_choice_stories.png"
    add bsar_gui_path + "sotp_main_menu/main_menu_choice_stories_desc_substrate.png" ypos 499
    add bsar_gui_path + "sotp_main_menu/three_deaths_desc.png" xpos 47 ypos 525
    add bsar_gui_path + "sotp_main_menu/shadows_desc.png" xpos 1206 ypos 525

    textbutton "Три смерти":
        style "bsar_sotp_choose_story_text_style"
        text_style "bsar_sotp_choose_story_text_style"
        xpos 271
        yalign 0.35
        action Start("bsar_sotp_three_deaths")

    textbutton "Тени":
        style "bsar_sotp_choose_story_text_style"
        text_style "bsar_sotp_choose_story_text_style"
        xpos 1376
        yalign 0.35
        action Start("bsar_sotp_shadows")

    imagebutton:
        auto bsar_gui_path + "sotp_main_menu/back_%s.png"
        xpos 80
        ypos 980
        action [
            Hide("bsar_sotp_choose_story"),
            ShowMenu("bsar_sotp_main_menu")
        ]

screen bsar_sotp_load_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not bsar_sotp_main_menu_var:        
        text "Загрузка":
            font bsar_yanone_kaffeesatz_regular
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        textbutton "Назад":
            style "bsar_button_none" 
            text_style "bsar_sotp_main_menu_text_style" 
            xalign 0.1
            ypos 970
            action [
                SetVariable("bsar_sotp_main_menu_var", True),
                Hide("bsar_sotp_load_main_menu"),
                ShowMenu("bsar_sotp_main_menu")
            ]
                    
        textbutton "Загрузить":
            style "bsar_button_none" 
            text_style "bsar_sotp_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [
                BsarFunctionCallback(bsar_on_load_callback, selected_slot),
                FileLoad(selected_slot, confirm=False)
            ]
                 
        textbutton "Удалить":
            style "bsar_button_none" 
            text_style "bsar_sotp_main_menu_text_style" 
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
                        style "bsar_sotp_save_load_button_main_menu"

                        fixed:
                            text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" + FileSaveName(i)):
                                style "bsar_sotp_text_save_load_main_menu"
                                xpos 15
                                ypos 15

screen bsar_sotp_preferences_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not bsar_sotp_main_menu_var:        
        text "Настройки":
            font bsar_yanone_kaffeesatz_regular
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        text "Режим экрана":
            font bsar_yanone_kaffeesatz_regular
            size 70
            xalign 0.5
            ypos 200
            
        textbutton "На весь экран":
            style "bsar_button_none"
            text_style "bsar_sotp_preferences_main_menu_text_style"
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
                text_style "bsar_sotp_preferences_main_menu_text_style_inverse"

            else:
                text_style "bsar_sotp_preferences_main_menu_text_style"

            action Preference("display", "window")

        text "Размер шрифта":
            font bsar_yanone_kaffeesatz_regular
            size 70
            xalign 0.5
            ypos 360
                
        textbutton "Обычный":
            style "bsar_button_none"
            text_style "bsar_sotp_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.175
            ypos 440
            action SetField(persistent, "font_size", "small")
                
        textbutton "Большой":
            style "bsar_button_none"
            text_style "bsar_sotp_preferences_main_menu_text_style"
            text_align 0.5
            xalign 0.82
            ypos 440
            action SetField(persistent, "font_size", "large")
                
        text "Пропускать":
            font bsar_yanone_kaffeesatz_regular
            size 70
            xalign 0.5
            ypos 520

        if not _preferences.skip_unseen:
            textbutton "Виденное ранее":
                style "bsar_button_none"
                text_style "bsar_sotp_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "Весь текст":
                style "bsar_button_none"
                text_style "bsar_sotp_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.83
                ypos 600
                action Preference("skip", "all")
                            
        if _preferences.skip_unseen:
            textbutton "Виденное ранее":
                style "bsar_button_none"
                text_style "bsar_sotp_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "Весь текст":
                style "bsar_button_none"
                text_style "bsar_sotp_preferences_main_menu_text_style"
                text_align 0.5
                xalign 0.83
                ypos 600
                action Preference("skip", "all")    
            
        text "Громкость музыки":
            font bsar_yanone_kaffeesatz_regular
            size 70
            xpos 430
            ypos 820
        bar:
            value Preference("music volume")
            right_bar bsar_gui_path + "preferences/sotp_main_menu/bar_null.png"
            left_bar bsar_gui_path + "preferences/sotp_main_menu/bar_full.png"
            thumb bsar_gui_path + "preferences/sotp_main_menu/vthumb.png"
            xpos 975
            ypos 827
            xmaximum 400
            ymaximum 85

        textbutton "Назад":
            style "bsar_button_none" 
            text_style "bsar_sotp_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [
                SetVariable("bsar_sotp_main_menu_var", True),
                Hide("bsar_sotp_preferences_main_menu"),
                ShowMenu("bsar_sotp_main_menu")
            ]

screen bsar_sotp_extra():
    modal True

    key "K_F1":
        action NullAction()
    
    if not bsar_sotp_main_menu_var:
        text "Дополнительно":
            font bsar_yanone_kaffeesatz_regular
            size 150
            text_align 0.5
            xalign 0.5
            ypos 40
            antialias True
            kerning 2

        textbutton "Музыка":
            style "bsar_button_none"
            text_style "bsar_sotp_main_menu_text_style" 
            xalign 0.5
            yalign 0.35
            action [
                Hide("bsar_sotp_extra"),
                ShowMenu("bsar_sotp_music_room")
            ]

        textbutton "Галерея":
            style "bsar_button_none" 
            text_style "bsar_sotp_main_menu_text_style" 
            xalign 0.5
            yalign 0.5
            action [
                Hide("bsar_sotp_extra"),
                ShowMenu("bsar_sotp_background_gallery")
            ]

        textbutton "Достижения":
            style "bsar_button_none" 
            text_style "bsar_sotp_main_menu_text_style" 
            xalign 0.5
            yalign 0.65
            action [
                Hide("bsar_sotp_extra"),
                ShowMenu("bsar_sotp_achievements")
            ]

        textbutton "Назад":
            style "bsar_button_none" 
            text_style "bsar_sotp_main_menu_text_style" 
            xalign 0.5
            yalign 0.85
            action [
                SetVariable("bsar_sotp_main_menu_var", True),
                Hide("bsar_sotp_extra"), 
                ShowMenu("bsar_sotp_main_menu")
            ]

screen bsar_sotp_achievements():
    modal True

    if not bsar_sotp_main_menu_var:
        text "Достижения":
            font bsar_yanone_kaffeesatz_regular
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        add bsar_gui_path + "sotp_main_menu/achievements_frame.png" xpos 310 ypos 190

        add bsar_gui_path + "sotp_main_menu/achievements_frame.png" xpos 1090 ypos 190

        $ sotp_achievements = {
            "begining_and_end": {
                "ach_xpos": 372,
                "text": "У всего есть начало и конец.\nИ очень часто сложно понять,\nгде заканчивается одно и\nначинается другое. Нам\nхочется верить, что всё\nциклично. Что-то должно\nумереть, чтобы проросло\nновое.",
                "text_xpos": 375
            },
            "better": {
                "ach_xpos": 1152,
                "text": "Всякий раз оглядываясь назад\nмы надеемся, что там,\nвпереди, нас ждёт что-то\nлучшее. Кто-то делает всё для\nэтого, кто-то лишь\nподстраивается под\nдействительность, но всякий\nверит в то, что всё наладится.",
                "text_xpos": 1150
            }
        }

        for achievement, info in sotp_achievements.items():
            if persistent.bsar_achievements.get("sotp_" + achievement, False):
                add bsar_gui_path + "achievements/sotp/" + achievement + ".png" xpos info["ach_xpos"] ypos 265

                text info["text"]:
                    font bsar_yanone_kaffeesatz_light
                    size 40
                    xpos info["text_xpos"]
                    ypos 405
            else:
                add bsar_gui_path + "achievements/sotp/locked.png" xpos info["ach_xpos"] ypos 490

        textbutton "Назад":
            style "bsar_button_none" 
            text_style "bsar_sotp_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [
                Hide("bsar_sotp_achievements"),
                ShowMenu("bsar_sotp_extra")
            ]

screen bsar_sotp_background_gallery():
    modal True

    if not bsar_sotp_main_menu_var:
        $ bsar_sotp_gallery_table = bsar_sotp_gallery_bg_list
        $ bsar_sotp_len_table = len(bsar_sotp_gallery_bg_list)

        text "Галерея":
            font bsar_yanone_kaffeesatz_regular
            size 150
            xalign 0.5
            ypos 5
            antialias True
            kerning 2

        textbutton "Назад":
            style "bsar_button_none" 
            text_style "bsar_sotp_main_menu_text_style" 
            xalign 0.5
            ypos 970
            action [
                Hide("bsar_sotp_background_gallery"),
                ShowMenu("bsar_sotp_extra")
            ]

        grid bsar_gallery_rows bsar_gallery_cols xpos 0.09 ypos 0.18:
            $ bsar_sotp_gallery_bg_displayed = 0
            $ bsar_sotp_gallery_next_page = bsar_sotp_gallery_page + 1

            if bsar_sotp_gallery_next_page > int(bsar_sotp_len_table / bsar_gallery_cells):
                $ bsar_sotp_gallery_next_page = 0

            for n in range(bsar_sotp_len_table):
                if n < (bsar_sotp_gallery_page + 1) * bsar_gallery_cells and n >= bsar_sotp_gallery_page * bsar_gallery_cells:
                    $ _bsar_t = im.Crop(
                        "bsar/images/bg/" + bsar_sotp_gallery_table[n] + ".png",
                        (0, 0, 1920, 1080)
                    )
                            
                    $ _bsar_img_scaled = im.Scale(_bsar_t, 320, 180)

                    $ bsar_img = im.Composite(
                        (336, 196),
                        (8, 8),
                        im.Alpha(_bsar_img_scaled, 0.9),
                        (0, 0),
                        im.Image(bsar_gui_path + "save_load/sotp_main_menu/save_load_button_idle.png")
                    )

                    $ bsar_imgh = im.Composite(
                        (336, 196),
                        (8, 8),
                        _bsar_img_scaled,
                        (0, 0),
                        im.Image(bsar_gui_path + "save_load/sotp_main_menu/save_load_button_hover.png")
                    )

                    add bsar_sotp_gallery.make_button(
                        bsar_sotp_gallery_table[n], 
                        get_image("gui/gallery/blank.png"), 
                        None,
                        bsar_imgh,
                        bsar_img,
                        style="blank_button",
                        bottom_margin=50,
                        right_margin=50
                    )

                    $ bsar_sotp_gallery_bg_displayed += 1

                    if n + 1 == bsar_sotp_len_table:
                        $ bsar_sotp_gallery_next_page = 0

            for j in range(0, bsar_gallery_cells - bsar_sotp_gallery_bg_displayed):
                null

        if bsar_sotp_gallery_page != 0:
            imagebutton:
                idle bsar_gui_path + "dialogue_box/backward_idle.png"
                hover bsar_gui_path + "dialogue_box/bw/backward_hover.png"
                yalign 0.5 
                xalign 0.01 
                action [
                    SetVariable("bsar_sotp_gallery_page", bsar_sotp_gallery_page - 1),
                    ShowMenu("bsar_sotp_background_gallery")
                ]

        if bsar_sotp_gallery_page != int(bsar_gallery_page_counter(bsar_sotp_len_table, bsar_gallery_cells)) - 1:
            imagebutton: 
                idle bsar_gui_path + "dialogue_box/forward_idle.png"
                hover bsar_gui_path + "dialogue_box/bw/forward_hover.png"
                yalign 0.5 
                xalign 0.99 
                action [
                    SetVariable("bsar_sotp_gallery_page", bsar_sotp_gallery_next_page), 
                    ShowMenu("bsar_sotp_background_gallery")
                ]