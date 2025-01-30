init python:
    class BsarFunctionCallback(Action):
        def __init__(self, function, *arguments):
            self.function = function
            self.arguments = arguments

        def __call__(self):
            return self.function(self.arguments)

    def bsar_on_load_callback(slot):
        try:
            if persistent.bsar_on_save_timeofday[slot]:
                persistent.timeofday = persistent.bsar_on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.bsar_on_save_timeofday[slot][1]
                persistent.font_size = persistent.bsar_on_save_timeofday[slot][2]
                persistent.bsar_current_story = persistent.bsar_on_save_timeofday[slot][3]
                _preferences.volumes["music"] = persistent.bsar_on_save_timeofday[slot][4]
                _preferences.volumes["sfx"] = persistent.bsar_on_save_timeofday[slot][5]
                _preferences.volumes["voice"] = persistent.bsar_on_save_timeofday[slot][6]
                bsar_toggle_main_menu()
                bsar_set_dynamic_cursor("timeofday")
    
        except:
            pass

    def bsar_on_save_callback(slot):
        if not persistent.bsar_on_save_timeofday:
            persistent.bsar_on_save_timeofday = {}

        persistent.bsar_on_save_timeofday[slot] = (
            persistent.timeofday,
            persistent.sprite_time, 
            persistent.font_size, 
            persistent.bsar_current_story,
            _preferences.volumes["music"],
            _preferences.volumes["sfx"], 
            _preferences.volumes["voice"]
        )
    
    def bsar_screen_save():
        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[("bsar_old_" + screen_name, None)] = renpy.display.screen.screens[(screen_name, None)]
    
    def bsar_screen_act():
        config.window_title = u"Между сном и явью"
        config.name = "BetweenSleepAndReality"
        config.version = "1.0"

        main_menu_screen = "insomnia_main_menu" if persistent.bsar_current_story == "insomnia" else "sotp_main_menu"
        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("bsar_" + main_menu_screen, None)]

        for screen_name in ["quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("bsar_" + screen_name, None)]

        layout.LOADING = "Потерять несохраненые данные?"
        renpy.free_memory()
        config.linear_saves_page_size = None
        persistent._file_page = "bsar_FilePage_1"  

    def bsar_screens_diact():
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.2"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("bsar_old_" + screen_name, None)]

        layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
        renpy.free_memory()
        persistent.timeofday = "day"
        config.mouse_displayable = MouseDisplayable("images/misc/mouse/1.png", 0, 0)
        config.main_menu_music = music_list["blow_with_the_fires"]

        persistent._file_page = 1

        for channel in ["ambience", "music", "sound", "sound_loop"]:
            renpy.music.stop(channel)
            
        renpy.play(music_list["blow_with_the_fires"], channel="music")

    def bsar_screens_save_act():
        bsar_screen_save()
        bsar_screen_act()