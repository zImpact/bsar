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
            right_bar bsar_gui_path + "/preferences/sotp_main_menu/bsar_bar_null.png"
            left_bar bsar_gui_path + "/preferences/sotp_main_menu/bsar_bar_full.png"
            thumb bsar_gui_path + "/preferences/sotp_main_menu/bsar_vthumb.png"
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