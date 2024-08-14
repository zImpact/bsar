init python:
    mods["bsar_start"] = u"{font=[bsar_diamond_girl_skinny]}{size=45}Между сном и явью{/font}{/size}"

    try:
        modsImages["bsar_start"] = ("bsar/images/gui/misc/bsar_tabular_list_preview.png", False)

    except:
        pass

label bsar_start:
    $ bsar_set_time('night')
    $ bsar_set_dynamic_cursor('main_menu')
    $ bsar_onload('lock')
    $ bsar_screens_save_act()
    $ renpy.pause(3, hard=True)
    show bsar_insomnia_intro_logo
    show bsar_blank_skip
    with Dissolve(3)
    play sound sfx_intro_bus_transition
    $ renpy.pause(5, hard=True)
    scene bg black with Dissolve(2)
    $ renpy.pause(2, hard=True)
    $ bsar_onload("unlock")

    label bsar_after_intro:
        $ renpy.transition(dissolve)