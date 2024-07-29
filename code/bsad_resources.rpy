init python:
    from os import path, environ
    import random
    import time

    for file_name in renpy.list_files():
        if "bsad" in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith("bsad/images/bg/"):
                renpy.image("bg " + file_path, file_name)

            elif file_name.startswith("bsad/images/gui/"):
                renpy.image(file_path, file_name)

            elif file_name.startswith("bsad/images/sprites/"):
                renpy.image(file_path, ConditionSwitch("persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), True, file_name))

            elif file_name.startswith("bsad/sounds/"):
                globals()[file_path] = file_name

    bsad_std_set_for_preview = {}
    bsad_std_set = {}
    store.bsad_colors = {}
    store.bsad_names = {}
    store.bsad_names_list = []
    bsad_speaker_color = "speaker_color"

    store.bsad_names_list.append("bsad_narrator")

    store.bsad_names_list.append("bsad_th")

    bsad_colors["bsad_protagonist"] = {"speaker_color": "#cccc7b"}
    bsad_names["bsad_protagonist"] = "Я"
    store.bsad_names_list.append("bsad_protagonist")

    bsad_colors["bsad_he"] = {"speaker_color": "#ffffff"}
    bsad_names["bsad_he"] = "Он"
    store.bsad_names_list.append("bsad_he")

    bsad_colors["bsad_us"] = {"speaker_color": "#ff3200"}
    bsad_names["bsad_us"] = "Ульяна"
    store.bsad_names_list.append("bsad_us")

    bsad_colors["bsad_usp"] = {"speaker_color": "#ff3200"}
    bsad_names["bsad_usp"] = "Пионерка"
    store.bsad_names_list.append("bsad_usp")

    bsad_colors["bsad_she"] = {"speaker_color": "#ffffff"}
    bsad_names["bsad_she"] = "Она"
    store.bsad_names_list.append("bsad_she")

    bsad_colors["bsad_she_red"] = {"speaker_color": "#ff3200"}
    bsad_names["bsad_she_red"] = "Она"
    store.bsad_names_list.append("bsad_she_red")

    bsad_colors["bsad_dv"] = {"speaker_color": "#ffaa00"}
    bsad_names["bsad_dv"] = "Алиса"
    store.bsad_names_list.append("bsad_dv")

    bsad_colors["bsad_fox"] = {"speaker_color": "#ffffff"}
    bsad_names["bsad_fox"] = "Лис"
    store.bsad_names_list.append("bsad_fox")

    bsad_colors["bsad_fox_orange"] = {"speaker_color": "#ffaa00"}
    bsad_names["bsad_fox_orange"] = "Лис"
    store.bsad_names_list.append("bsad_fox_orange")

    bsad_colors["bsad_sl"] = {"speaker_color": "#ffd200"}
    bsad_names["bsad_sl"] = "Славя"
    store.bsad_names_list.append("bsad_sl")

    bsad_colors["bsad_sister"] = {"speaker_color": "#ffffff"}
    bsad_names["bsad_sister"] = "Сестра"
    store.bsad_names_list.append("bsad_sister")

    bsad_colors["bsad_mz"] = {"speaker_color": "#4a86ff"}
    bsad_names["bsad_mz"] = "Женя"
    store.bsad_names_list.append("bsad_mz")

    bsad_colors["bsad_mt"] = {"speaker_color": "#00ea32"}
    bsad_names["bsad_mt"] = "Ольга Дмитриевна"
    store.bsad_names_list.append("bsad_mt")

    bsad_colors["bsad_un"] = {"speaker_color": "#b956ff"}
    bsad_names["bsad_un"] = "Лена"
    store.bsad_names_list.append("bsad_un")

    bsad_colors["bsad_doctor"] = {"speaker_color": "#ffffff"}
    bsad_names["bsad_doctor"] = "Доктор"
    store.bsad_names_list.append("bsad_doctor")

    bsad_colors["bsad_voice"] = {"speaker_color": "#ffffff"}
    bsad_names["bsad_voice"] = "Голос"
    store.bsad_names_list.append("bsad_voice")

    def bsad_char_define(character_name, is_nvl = False):
        global DynamicCharacter
        global nvl
        global bsad_store
        global bsad_speaker_color
        bsad_gl = globals()
        
        if character_name == "bsad_narrator":
            if is_nvl:
                bsad_gl["bsad_narrator"] = Character(None, kind = nvl, what_style = "bsad_text_style")
            
            else:
                bsad_gl["bsad_narrator"] = Character(None, what_style = "bsad_text_style")
            
            return
        
        if character_name == "bsad_th":
            if is_nvl:
                bsad_gl["bsad_th"] = Character(None, kind = nvl, what_style = "bsad_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            else:
                bsad_gl["bsad_th"] = Character(None, what_style = "bsad_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            return
        
        if is_nvl:
            bsad_gl[character_name] = DynamicCharacter("%s_name" % character_name, color = store.bsad_colors[character_name][bsad_speaker_color], kind = nvl, what_style = "bsad_text_style", who_suffix = ":")
            bsad_gl["%s_name" % character_name] = store.bsad_names[character_name]
        
        else:
            bsad_gl[character_name] = DynamicCharacter("%s_name" % character_name, color = store.bsad_colors[character_name][bsad_speaker_color], what_style = "bsad_text_style")
            bsad_gl["%s_name" % character_name] = store.bsad_names[character_name]

    def bsad_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global bsad_store
        
        for character_name in store.bsad_names_list:
            bsad_char_define(character_name)

    def bsad_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global bsad_narrator
        global bsad_th
        bsad_narrator_nvl = bsad_narrator
        th_nvl = bsad_th
        
        global bsad_store
        
        for character_name in store.bsad_names_list:
            bsad_char_define(character_name, True)

    def bsad_reload_names():
        global bsad_store
        
        for character_name in store.bsad_names_list:
            bsad_char_define(character_name)

    bsad_reload_names()

    def bsad_page_counter(n, k):
        l = float(n) / float(k)
        
        if l - int(l) > 0:
            return int(l) + 1

        else:
            return l

    def bsad_heartbeat_animation(image_name, power, zoom2, transition = None):
        renpy.show(image_name, at_list = [bsad_heartbeat_anim(image_name, power, zoom2)], tag = image_name + "_2")
        renpy.with_statement(transition)

    def bsad_set_timeofday_cursor():
        global bsad_set_timeofday_cursor_var

        if bsad_set_timeofday_cursor_var:
            config.mouse_displayable = MouseDisplayable(bsad_gui_path + "cursors/" + persistent.timeofday + "/cursor.png", 0, 0)

    bsad_set_timeofday_cursor_curried = renpy.curry(bsad_set_timeofday_cursor)

    def bsad_set_main_menu_cursor():
        config.mouse_displayable = MouseDisplayable(bsad_gui_path + "cursors/main_menu/cursor.png", 0, 0)

    bsad_set_main_menu_cursor_curried = renpy.curry(bsad_set_main_menu_cursor)

    def bsad_set_null_cursor():
        config.mouse_displayable = MouseDisplayable(bsad_gui_path + "misc/bsad_none.png", 0, 0)

    bsad_set_null_cursor_curried = renpy.curry(bsad_set_null_cursor)

    def bsad_onload(type):
        global bsad_lock_quit
        global bsad_lock_quick_menu

        if type == "lock":
            renpy.config.skipping = None
            bsad_lock_quit = True
            bsad_lock_quick_menu = True
            config.allow_skipping = False

        elif type == "unlock":
            bsad_lock_quit = False
            bsad_lock_quick_menu = False
            config.allow_skipping = True       

    def bsad_show_random_words(list, k = 0):
        global randow_word

        count = len(list)

        for i in range(count + 1 + k):
            randow_word = random.choice(list)
            renpy.show("bsad_words_move_style randow_word", at_list=[bsad_words_move(random.uniform(0.1, 0.5), random.random(), random.random())], tag="text_" + str(i))

    def bsad_show_centered_text(text, transition = None, pause = True, style = style.bsad_centered_text_style):
        renpy.show("text", what = Text(text, slow = True, style = style, xalign = 0.5, yalign = 0.5))
        renpy.with_statement(transition)

        if pause:
            renpy.pause()

    def bsad_hide_centered_text(transition=None):
        renpy.hide("text")
        renpy.with_statement(transition)

    def bsad_heart_monitor_phrases_f(phrase):
        renpy.play(bsad_heart_monitor_sound, "sound")
        renpy.show(phrase + "_left", behind = ["bsad_heart_monitor_frame"], at_list = [bsad_heart_monitor_phrases_position(0)])
        renpy.with_statement(bsad_heart_monitor_transition)
        bsad_show_centered_text(bsad_heart_monitor_phrases[phrase][0], transition = bsad_heart_monitor_transition, pause = False, style = style.bsad_centered_text_style_heart_monitor)
        renpy.show(phrase + "_right", behind = ["bsad_heart_monitor_frame"], at_list = [bsad_heart_monitor_phrases_position(bsad_heart_monitor_phrases[phrase][1])])
        renpy.with_statement(bsad_heart_monitor_transition)
        renpy.pause()
        renpy.hide(phrase + "_left")
        renpy.hide("text")
        renpy.hide(phrase + "_right")
        renpy.with_statement(bsad_heart_monitor_transition)

        renpy.pause(0.5, hard = True)

    def bsad_frame_animation(image_name, frames_count, retention, loop, transition, start = 1, **properties):
        anim_args = []
        
        for i in range(start, start + frames_count):
            anim_args.append(renpy.display.im.image(image_name + "_" + str(i) + ".png"))
            
            if loop:
                anim_args.append(retention)
                anim_args.append(transition)
        
        return anim.TransitionAnimation(*anim_args, **properties)

    # def bsad_predict_screens():
    #     for screen_name in bsad_screens_list:
    #         renpy.start_predict_screen(screen_name)

    # def bsad_predict_resources():
    #     for folder_name in bsad_folders_list:
    #         renpy.start_predict(folder_name)

    # def bsad_stop_predict_screens():
    #     for screen_name in bsad_screens_list:
    #         renpy.stop_predict_screen(screen_name)

    # def bsad_stop_predict_resources():
    #     for folder_name in bsad_folders_list:
    #         renpy.stop_predict(folder_name)

    # def bsad_predict_resources_d():
    #     bsad_rightnow_r = time.time()

    #     while time.time() - bsad_rightnow_r < 6:
    #         bsad_predict_resources()
            
    #         renpy.show("bsad_first_dot_image", at_list = [bsad_first_dot_pos])
    #         renpy.pause(0.7, hard = True)
    #         renpy.show("bsad_second_dot_image", at_list = [bsad_second_dot_pos])
    #         renpy.pause(0.7, hard = True)
    #         renpy.show("bsad_third_dot_image", at_list = [bsad_third_dot_pos])
    #         renpy.pause(0.7, hard = True)
    #         renpy.hide("bsad_first_dot_image")
    #         renpy.hide("bsad_second_dot_image")
    #         renpy.hide("bsad_third_dot_image")
    #         renpy.pause(0.7, hard = True)

    # def bsad_predict_screens_d():
    #     bsad_rightnow_s = time.time()

    #     while time.time() - bsad_rightnow_s < 3:
    #         bsad_predict_screens()

    #         renpy.show("bsad_first_dot_image", at_list = [bsad_first_dot_pos])
    #         renpy.pause(0.7, hard = True)
    #         renpy.show("bsad_second_dot_image", at_list = [bsad_second_dot_pos])
    #         renpy.pause(0.7, hard = True)
    #         renpy.show("bsad_third_dot_image", at_list = [bsad_third_dot_pos])
    #         renpy.pause(0.7, hard = True)
    #         renpy.hide("bsad_first_dot_image")
    #         renpy.hide("bsad_second_dot_image")
    #         renpy.hide("bsad_third_dot_image")
    #         renpy.pause(0.7, hard = True)

    #     renpy.show("bsad_first_dot_image", at_list = [bsad_first_dot_pos])
    #     renpy.music.stop("ambience", 2)

    # def bsad_predicting():
    #     bsad_predict_resources_d()
    #     bsad_predict_screens_d()

    # def bsad_loading_screen():
    #     renpy.pause(2, hard = True)
    #     renpy.show("bg bsad_ext_road_winter_night", at_list = [bsad_zoom_in_center])
    #     renpy.show("bsad_name_header", at_list = [bsad_name_header_pos])
    #     renpy.show("bsad_loading_text", at_list = [bsad_loading_text_pos])
    #     renpy.music.play("bsad/sounds/ambience/bsad_winter_wind.mp3", "ambience", fadein = 2)
    #     renpy.show("bsad_loading_icon", at_list = [bsad_full_rotate_repeat(1.1, 0.8, 0.5, 0.5)])
    #     renpy.transition(Dissolve(2))
    #     renpy.pause(2.0, hard = True)
    #     bsad_predicting()

    class bsad_disp_text_style():
        def __init__(self):
            self.alpha = None
            self.font = None
            self.size = None
            self.bold = False
            self.italic = False
            self.underline = False
            self.strikethrough = False
            self.plain = False
            self.color = None
            self.user_style = None
            self.outline_color = None
            self.bsad_scare_tag = None

        def bsad_add_tags(self, char):
            tag, _, value = char.partition("=")
            
            if tag == "b":
                self.bold = True
                return True

            elif tag == "/b":
                self.bold = False
                return True

            elif tag == "s":
                self.strikethrough = True
                return True

            elif tag == "/s":
                self.strikethrough = False
                return True

            elif tag == "u":
                self.underline = True
                return True

            elif tag == "/u":
                self.underline = False
                return True

            elif tag == "i":
                self.italic = True
                return True

            elif tag == "/i":
                self.italic = False
                return True

            elif tag == "color":
                self.color = char
                return True

            elif tag == "/color":
                self.color = None
                return True

            elif tag == "alpha":
                self.alpha = char
                return True

            elif tag == "/alpha":
                self.alpha = None
                return True

            elif tag == "font":
                self.font = char
                return True

            elif tag == "/font":
                self.font = None
                return True

            elif tag == "":
                self.user_style = char
                return True

            elif tag == "/":
                self.user_style = None
                return True

            elif tag == "size":
                self.size = char
                return True

            elif tag == "/size":
                self.size = None
                return True

            elif tag == "outlinecolor":
                self.outline_color = char
                return True

            elif tag == "/outlinecolor":
                self.outline_color = None
                return True

            elif tag == "plain":
                self.plain = True
                return True

            elif tag == "/plain":
                self.plain = False
                return True

            elif tag == "sc":
                self.bsad_scare_tag = char
                return True

            elif tag == "/sc":
                self.bsad_scare_tag = None
                return True

            return False

        def bsad_apply_style(self, char):
            new_string = ""

            if self.bsad_scare_tag is not None:
                new_string += "{" + self.bsad_scare_tag + "}"
                
            if self.user_style is not None:
                new_string += "{" + self.user_style + "}"

            if self.bold:
                new_string += "{b}"

            if self.strikethrough:
                new_string += "{s}"

            if self.underline:
                new_string += "{u}"

            if self.italic:
                new_string += "{i}"

            if self.color is not None:
                new_string += "{" + self.color + "}"

            if self.alpha is not None:
                new_string += "{" + self.alpha + "}"

            if self.font is not None:
                new_string += "{" + self.font + "}"

            if self.size is not None:
                new_string += "{" + self.size + "}"

            if self.outline_color is not None:
                new_string += "{" + self.outline_color + "}"

            if self.plain:
                new_string += "{plain}"

            new_string += char

            if self.bsad_scare_tag is not None:
                new_string += "{/" + self.bsad_scare_tag + "}"

            return new_string

        def bsad_start_tags(self):
            new_string = ""

            if self.bsad_scare_tag is not None:
                new_string += "{" + self.bsad_scare_tag + "}"

            if self.user_style is not None:
                new_string += "{" + self.user_style + "}"

            if self.bold:
                new_string += "{b}"

            if self.strikethrough:
                new_string += "{s}"

            if self.underline:
                new_string += "{u}"

            if self.italic:
                new_string += "{i}"

            if self.color is not None:
                new_string += "{" + self.color + "}"

            if self.alpha is not None:
                new_string += "{" + self.alpha + "}"

            if self.font is not None:
                new_string += "{" + self.font + "}"

            if self.size is not None:
                new_string += "{" + self.size + "}"

            if self.outline_color is not None:
                new_string += "{" + self.outline_color + "}"

            if self.plain:
                new_string += "{plain}"

            return new_string

        def bsad_end_tags(self):
            new_string = ""

            if self.bsad_scare_tag is not None:
                new_string += "{/" + self.bsad_scare_tag + "}"

            return new_string

    class bsad_scare_text(renpy.Displayable):
        def __init__(self, child, square = 2, **kwargs):
            super(bsad_scare_text, self).__init__(**kwargs)

            self.child = child

            self.square = square

        def render(self, width, height, st, at):
            xoff = (random.random() - .5) * float(self.square)
            yoff = (random.random() - .5) * float(self.square)

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            render.subpixel_blit(child_render, (xoff, yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [self.child]

    def bsad_scare_tag(tag, argument, contents):
        new_list = [ ]

        if argument == "":
            argument = 5

        scare_style = bsad_disp_text_style()

        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(scare_style.bsad_apply_style(char))
                    char_disp = bsad_scare_text(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))

            elif kind == renpy.TEXT_TAG:
                if not scare_style.bsad_add_tags(text):
                    new_list.append((kind, text))

            else:
                new_list.append((kind,text))

        return new_list    

    config.custom_text_tags["isc"] = bsad_scare_tag

    if persistent.bsad_achievements == None:
        persistent.bsad_achievements = {
            "bsad_paradise": False,
            "bsad_awakening": False,
            "bsad_murderous_snowball": False
            }

    def bsad_show_achievement(achievement_name):
        renpy.play(sfx_achievement)
        renpy.show(achievement_name, [bsad_achievement_transform])
        renpy.pause(4, hard = True)
        renpy.hide(achievement_name)

init:
    $ bsad_paradise_ending_v = 0
    $ bsad_day1_stroll = False
    $ bsad_day2_intervene = False
    $ bsad_day2_after_qte = False

    $ bsad_day2_amnesia_scene = ["Мог ли я быть знаком с Ульяной? ", "Чем занимаются родители?", "Где учусь?", "???"]

    $ bsad_heart_monitor_phrases = {
        "bsad_military_service": ["Служба в армии", 1179],
        "bsad_composure": ["Хладнокровие", 1149],
        "bsad_institute": ["Институт", 1089],
        "bsad_meeting_with_her": ["Встреча с ней", 1155],
        "bsad_love": ["Пветёа4", 1069],
        "bsad_police_work": ["Работа в полиции", 1215],
        "bsad_0apv4": ["0 АПВ 4", 978],
        "bsad_fox": ["Лис", 1038],
        "bsad_friendship": ["Дружба", 1061],
        "bsad_rest": ["Покой", 975],
        "bsad_easy_money": ["Лёгкие деньги", 1163],
        "bsad_protection": ["12-18-29-26-6-3-1-15-10-6", 1373],
        "bsad_drug_trafficking": ["15-1-18-12-16-16-2-16-18-16-20", 1516],
        "bsad_sisters_death": ["Шулчщг шлшщчв7", 946],
        "bsad_nightmares": ["Кошмары", 1059],
        "bsad_doubts": ["Сомнения", 976],
        "bsad_new_deal": ["15-16-3-1-33 19-5-6-13-12-1", 1404],
        "bsad_her_death": ["Её смерть", 1086],
        "bsad_sleep_that_knows_no_breaking": ["Сон", 1038]
    }

    $ bsad_heart_monitor_transition = ImageDissolve("bsad/images/gui/misc/heart_monitor/bsad_hm_trans.png", 0.6, ramplen = 8, reverse = False, alpha = True)
    $ bsad_flash = Fade(0.45, 1.0, 0.45, color = "#ffff")

    $ bsad_titles_text = '''Спасибо за прочтение! Вот уже прошло практически два года как мы начали делать модификации и именно этот проект является важной вехой нашей деятельности, ибо с него всё и начиналось.

Искренне надеемся, что ремейк Бессонницы вам понравился.

Над модом работали:
СЦЕНАРИЙ
Ева Миронова

КОД
Андрей Катаев

ВИЗУАЛЬНАЯ СОСТАВЛЯЮЩАЯ
Егор Бобков
Лиза Степанцова
Егор Козаченко
Anna Monster
Семён Персунов
Александр Ларин

МУЗЫКАЛЬНОЕ СОПРОВОЖДЕНИЕ
Дмитрий Таранов
Алан Кокоев

ОТДЕЛЬНЫЕ БЛАГОДАРНОСТИ
Александр Милютин
Родион Егоров
Саша Шмелев
Илья Можайкин
Женя Двойкин

Спасибо всем за поддержку. Ваши оценки и отзывы очень важны для нас и мотивируют работать дальше! С уважением, команда Zero Impact.

С новым годом!'''

    image bsad_titles_final = ParameterizedText(style = "bsad_titles_style", size = 40, xalign = 0.5)

    image bsad_heavy_snow_day = Snow(bsad_gui_path + "bsad_snow_particle_day.png", max_particles = 500)
    image bsad_normal_snow_day = Snow(bsad_gui_path + "bsad_snow_particle_day.png")

    image bsad_heavy_snow_night = Snow(bsad_gui_path + "bsad_snow_particle_night.png", max_particles = 500)
    image bsad_normal_snow_night = Snow(bsad_gui_path + "bsad_snow_particle_night.png")

    $ bsad_main_menu_var = True
    $ bsad_set_timeofday_cursor_var = False
    $ bsad_lock_quit = False
    $ bsad_lock_quick_menu = False
    $ bsad_lock_quit_game_main_menu_var = True

    $ bsad_screens_list = [
        "bsad_main_menu", "bsad_preferences_main_menu", "bsad_load_main_menu", "bsad_achievements", "bsad_quit_main_menu", "bsad_preferences", 
        "bsad_save", "bsad_load", "bsad_say", "bsad_nvl", "bsad_game_menu_selector", "bsad_quit", "bsad_yesno_prompt", "bsad_text_history", "bsad_choice", "bsad_help"
    ]

    $ bsad_folders_list = ["bsad/images/bg*.*", "bsad/images/sprites*.*"]

    image bsad_name_header = Text("Бессонница", size = 170, font = bsad_diamond_girl_skinny)
    image bsad_loading_text = Text("Загрузка", size = 110, font = bsad_diamond_girl_skinny)
    image bsad_first_dot_image = Text(".", size = 110, font = bsad_diamond_girl_skinny)
    image bsad_second_dot_image = Text(".", size = 110, font = bsad_diamond_girl_skinny)
    image bsad_third_dot_image = Text(".", size = 110, font = bsad_diamond_girl_skinny)

    image bsad_static_noise_anim = bsad_frame_animation("bsad/images/bg/bsad_static_noise_anim/bsad_static_noise", 5, 0.2, True, Dissolve(0.2))

    image bsad_main_menu_bg = Movie(fps = 30, play = "bsad/images/gui/main_menu/bsad_main_menu_background.ogv")

    image bsad_words_move_style = ParameterizedText(style = "settings_link", size = 100, color = "fff")

    image bsad_she_night = im.MatrixColor("bsad/images/sprites/she/bsad_she.png", im.matrix.tint(0.63, 0.78, 0.82))

    image bg bsad_int_house_of_mt_day_blurred = im.Blur("images/bg/int_house_of_mt_day.jpg", 1.5)

    image bsad_snow_layer0_anim:
        contains:
            "bsad_snow_layer0_img"
            bsad_snow_move(8, 0.0, -0.05)

        contains:
            "bsad_snow_layer0_img"
            bsad_snow_move(8, 0.25, -0.05)

        contains:
            "bsad_snow_layer0_img"
            bsad_snow_move(8, 0.5, -0.05)

        contains:
            "bsad_snow_layer0_img"
            bsad_snow_move(8, 0.75, -0.05)

    image bsad_snow_layer1_anim:
        contains:
            "bsad_snow_layer1_img"
            bsad_snow_move(10, 0.0, 0.05, pause_time = 0.5)

        contains:
            "bsad_snow_layer1_img"
            bsad_snow_move(10, 0.25, 0.05, pause_time = 0.5)

        contains:
            "bsad_snow_layer1_img"
            bsad_snow_move(10, 0.5, 0.05, pause_time = 0.5)

        contains:
            "bsad_snow_layer1_img"
            bsad_snow_move(10, 0.75, 0.05, pause_time = 0.5)


    image bsad_snow_layer2_anim:
        contains:
            "bsad_snow_layer2_img"
            bsad_snow_move(15, 0.0, -0.05, pause_time = 1.0)

        contains:
            "bsad_snow_layer2_img"
            bsad_snow_move(15, 0.25, -0.05, pause_time = 1.0)

        contains:
            "bsad_snow_layer2_img"
            bsad_snow_move(15, 0.5, -0.05, pause_time = 1.0)

        contains:
            "bsad_snow_layer2_img"
            bsad_snow_move(15, 0.75, -0.05, pause_time = 1.0)

    image bsad_snow_layer3_anim:
        contains:
            "bsad_snow_layer3_img"
            bsad_snow_move(20, 0.0, 0.07)

        contains:
            "bsad_snow_layer3_img"
            bsad_snow_move(20, 0.25, 0.07)

        contains:
            "bsad_snow_layer3_img"
            bsad_snow_move(20, 0.5, 0.07)

        contains:
            "bsad_snow_layer3_img"
            bsad_snow_move(20, 0.75, 0.07)

    image bsad_snow_layer0_anim_quick:
        contains:
            "bsad_snow_layer0_img"
            bsad_snow_move(3, 0.0, -0.03)

        contains:
            "bsad_snow_layer0_img"
            bsad_snow_move(3, 0.25, -0.03)

        contains:
            "bsad_snow_layer0_img"
            bsad_snow_move(3, 0.5, -0.03)

        contains:
            "bsad_snow_layer0_img"
            bsad_snow_move(3, 0.75, -0.03)

    image bsad_snow_layer1_anim_quick:
        contains:
            "bsad_snow_layer1_img"
            bsad_snow_move(4, 0.0, 0.05)

        contains:
            "bsad_snow_layer1_img"
            bsad_snow_move(4, 0.25, 0.05)

        contains:
            "bsad_snow_layer1_img"
            bsad_snow_move(4, 0.5, 0.05)

        contains:
            "bsad_snow_layer1_img"
            bsad_snow_move(4, 0.75, 0.05)

    image bsad_snow_layer2_anim_quick:
        contains:
            "bsad_snow_layer2_img"
            bsad_snow_move(5, 0.0, -0.05)

        contains:
            "bsad_snow_layer2_img"
            bsad_snow_move(5, 0.25, -0.05)

        contains:
            "bsad_snow_layer2_img"
            bsad_snow_move(5, 0.5, -0.05)

        contains:
            "bsad_snow_layer2_img"
            bsad_snow_move(5, 0.75, -0.05)

    image bsad_snow_layer3_anim_quick:
        contains:
            "bsad_snow_layer3_img"
            bsad_snow_move(5, 0.0, 0.03)

        contains:
            "bsad_snow_layer3_img"
            bsad_snow_move(5, 0.25, 0.03)

        contains:
            "bsad_snow_layer3_img"
            bsad_snow_move(5, 0.5, 0.03)
            
        contains:
            "bsad_snow_layer3_img"
            bsad_snow_move(5, 0.75, 0.03)

    transform bsad_buttons_atl():
        on idle:
            easein 0.5 zoom 1.0

        on hover:
            easein 0.5 zoom 1.05

    transform bsad_snow_move(time, start_pos, x_deviation = 0.05, pause_time = 0.0, fade_time = 1.0):
        truecenter
        ypos -0.25 + 1.5 * start_pos
        xpos 0.5 - x_deviation + 2 * x_deviation * start_pos
        pause pause_time

        block:
            block:
                alpha 1.0
                parallel:
                    linear(time * (1 - start_pos)) ypos 1.1 xpos (0.5 + x_deviation)

                parallel:
                    pause((time * (1 - start_pos)) - fade_time)
                    linear fade_time alpha 0.0

            block:
                ypos -0.25
                xpos 0.5 - x_deviation
                alpha 1.0
                linear(time * start_pos) ypos(-0.25 + 1.5 * start_pos) xpos(0.5 - x_deviation + 2 * x_deviation * start_pos)

            repeat

    transform bsad_zoom_qte_text:
        zoom 1.0
        block:
            linear 2.0 zoom 1.4
            linear 2.0 zoom 0.5
            repeat

    transform bsad_heart_monitor_phrases_position(x):
        xpos x
        ypos 264

    transform bsad_full_rotate_repeat(l, z, x, y):
        parallel:
            zoom z
            xalign x
            yalign y 
            rotate_pad True
            rotate 0
            linear l rotate 360
            repeat

    transform bsad_zoom_in_center():
        xalign 0.5 yalign 0.5 zoom 1.0
        pause 2.0
        linear 20 zoom 2.0 xalign 0.5 yalign 0.5

    transform bsad_name_header_pos():
        xalign 0.5
        yalign 0.045

    transform bsad_loading_text_pos():
        xalign 0.5 ypos 840

    transform bsad_first_dot_pos():
        xpos 1140
        ypos 843

    transform bsad_second_dot_pos():
        xpos 1150
        ypos 843

    transform bsad_third_dot_pos():
        xpos 1160
        ypos 843

    transform bsad_heartbeat_anim(image_name, power, zoom2):
        contains:
            image_name
            alpha 0.0
            zoom power
            xanchor 0.5 
            yanchor 0.5 
            xpos 0.5 
            ypos 0.5

            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0

            parallel:
                ease 0.75 zoom 1.10

            repeat

        contains:
            image_name
            alpha 0.0
            zoom power
            xanchor 0.5 
            yanchor 0.5 
            xpos 0.5 
            ypos 0.5

            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0

            parallel:
                ease 0.75 zoom zoom2

            repeat

    transform bsad_achievement_transform:
        align (1.2, 0.9)
        ease 1.0 align (0.85, 0.9)
        ease 0.5 align (0.95, 0.9)
        pause 1.5
        ease 0.5 align (1.5, 0.9)

    transform bsad_titles_anim():
        xalign 0.5
        ypos 1.1
        linear 38 ypos -2.0

    transform bsad_skip_pos():
        xalign 0.5
        ypos 900

    transform bsad_words_move(z, x, y):
        zoom z
        align(x, y)
        alpha .4

        parallel:
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            ease random.randint(1, 5) align(random.uniform(-0.2, 1.2), random.uniform(-0.2, 1.2))
            repeat

        parallel:
            linear random.uniform(0, 0.75) alpha .4
            linear random.uniform(0, 0.75) alpha 0
            repeat