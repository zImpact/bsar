init python:
    class InsomniaFunctionCallback(Action):
        def __init__(self,function, *arguments):
            self.function = function
            self.arguments = arguments

        def __call__(self):
            return self.function(self.arguments)

    def insomnia_on_load_callback(slot):
        try:
            if persistent.insomnia_on_save_timeofday[slot]:
                persistent.timeofday = persistent.insomnia_on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.insomnia_on_save_timeofday[slot][1]
                persistent.font_size = persistent.insomnia_on_save_timeofday[slot][2]
                _preferences.volumes["music"] = persistent.insomnia_on_save_timeofday[slot][3]
                _preferences.volumes["sfx"] = persistent.insomnia_on_save_timeofday[slot][4]
                _preferences.volumes["voice"] = persistent.insomnia_on_save_timeofday[slot][5]
    
        except:
            pass

    def insomnia_on_save_callback(slot):
        if not persistent.insomnia_on_save_timeofday:
            persistent.insomnia_on_save_timeofday = {}

        persistent.insomnia_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes["music"], _preferences.volumes["sfx"], _preferences.volumes["voice"])
    
    def insomnia_screen_save():
        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[("insomnia_old_" + screen_name, None)] = renpy.display.screen.screens[(screen_name, None)]
    
    def insomnia_screen_act():
        config.window_title = u"Бессонница"
        config.name = "Insomnia"
        config.version = "2.0"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("insomnia_" + screen_name, None)]

        layout.LOADING = "Потерять несохраненые данные?"

        renpy.free_memory()
        
        config.overlay_functions.append(insomnia_set_timeofday_cursor)
        config.main_menu_music = insomnia_domitori_taranofu_lullaby
        config.linear_saves_page_size = None
        persistent._file_page = "insomnia_FilePage_1"  

    def insomnia_screens_diact():
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.2"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("insomnia_old_" + screen_name, None)]

        layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"

        renpy.free_memory()
        config.overlay_functions.remove(insomnia_set_timeofday_cursor)

        persistent.timeofday = "day"
        config.mouse_displayable = MouseDisplayable('images/misc/mouse/1.png', 0, 0)
        config.main_menu_music = "sound/music/blow_with_the_fires.ogg"

        persistent._file_page = 1
        renpy.music.stop("ambience")
        renpy.music.stop("music")
        renpy.music.stop("sound")
        renpy.music.stop("sound_loop")
        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def insomnia_screens_save_act():
        insomnia_screen_save()
        insomnia_screen_act()