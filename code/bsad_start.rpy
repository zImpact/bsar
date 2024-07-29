init python:
    mods["insomnia_start"] = u"{font=[insomnia_diamond_girl_skinny]}{size=45}Бессонница{/font}{/size}"

    try:
        modsImages["insomnia_start"] = ("insomnia/images/gui/misc/insomnia_tabular_list_preview.png", False)

    except:
        pass

label insomnia_start:
    $ persistent.timeofday = "winter_day"
    $ persistent.sprite_time = "day"
    $ insomnia_set_main_menu_cursor()
    $ insomnia_onload("lock")
    $ insomnia_screens_save_act()
    $ renpy.pause(3, hard = True)
    show insomnia_intro_logo
    show expression renpy.display.behavior.ImageButton(insomnia_gui_path + '/main_menu/insomnia_skip_idle.png', insomnia_gui_path + '/main_menu/insomnia_skip_hover.png', clicked=[Jump('insomnia_after_intro')]) at insomnia_skip_pos
    with Dissolve(3)
    play sound sfx_intro_bus_transition
    $ renpy.pause(5, hard = True)
    scene bg black with Dissolve(2)
    #$ insomnia_loading_screen()
    #scene bg black with Dissolve(2)
    $ renpy.pause(2, hard = True)
    $ insomnia_onload("unlock")

    label insomnia_after_intro:
        $ renpy.transition(dissolve)