init python:
    from os import path, environ
    import random
    import time

    for file_name in renpy.list_files():
        if "bsar" in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith("bsar/images/bg/"):
                renpy.image("bg " + file_path, file_name)

            elif file_name.startswith("bsar/images/gui/"):
                renpy.image(file_path, file_name)

            elif file_name.startswith("bsar/images/sprites/"):
                renpy.image(file_path, ConditionSwitch("persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), True, file_name))

            elif file_name.startswith("bsar/sounds/"):
                globals()[file_path] = file_name

    bsar_std_set_for_preview = {}
    bsar_std_set = {}
    store.bsar_colors = {}
    store.bsar_names = {}
    store.bsar_names_list = []
    bsar_speaker_color = "speaker_color"

    store.bsar_names_list.append("bsar_narrator")

    store.bsar_names_list.append("bsar_th")

    bsar_colors["bsar_protagonist"] = {"speaker_color": "#cccc7b"}
    bsar_names["bsar_protagonist"] = "Я"
    store.bsar_names_list.append("bsar_protagonist")

    bsar_colors["bsar_he"] = {"speaker_color": "#ffffff"}
    bsar_names["bsar_he"] = "Он"
    store.bsar_names_list.append("bsar_he")

    bsar_colors["bsar_us"] = {"speaker_color": "#ff3200"}
    bsar_names["bsar_us"] = "Ульяна"
    store.bsar_names_list.append("bsar_us")

    bsar_colors["bsar_usp"] = {"speaker_color": "#ff3200"}
    bsar_names["bsar_usp"] = "Пионерка"
    store.bsar_names_list.append("bsar_usp")

    bsar_colors["bsar_she"] = {"speaker_color": "#ffffff"}
    bsar_names["bsar_she"] = "Она"
    store.bsar_names_list.append("bsar_she")

    bsar_colors["bsar_she_red"] = {"speaker_color": "#ff3200"}
    bsar_names["bsar_she_red"] = "Она"
    store.bsar_names_list.append("bsar_she_red")

    bsar_colors["bsar_yana"] = {"speaker_color": "#ff3200"}
    bsar_names["bsar_yana"] = "Яна"
    store.bsar_names_list.append("bsar_yana")

    bsar_colors["bsar_dv"] = {"speaker_color": "#ffaa00"}
    bsar_names["bsar_dv"] = "Алиса"
    store.bsar_names_list.append("bsar_dv")

    bsar_colors["bsar_fox"] = {"speaker_color": "#ffffff"}
    bsar_names["bsar_fox"] = "Лис"
    store.bsar_names_list.append("bsar_fox")

    bsar_colors["bsar_fox_orange"] = {"speaker_color": "#ffaa00"}
    bsar_names["bsar_fox_orange"] = "Лис"
    store.bsar_names_list.append("bsar_fox_orange")

    bsar_colors["bsar_sl"] = {"speaker_color": "#ffd200"}
    bsar_names["bsar_sl"] = "Славя"
    store.bsar_names_list.append("bsar_sl")

    bsar_colors["bsar_sister"] = {"speaker_color": "#ffffff"}
    bsar_names["bsar_sister"] = "Сестра"
    store.bsar_names_list.append("bsar_sister")

    bsar_colors["bsar_sister_yellow"] = {"speaker_color": "#ffd200"}
    bsar_names["bsar_sister_yellow"] = "Сестра"
    store.bsar_names_list.append("bsar_sister_yellow")

    bsar_colors["bsar_mz"] = {"speaker_color": "#4a86ff"}
    bsar_names["bsar_mz"] = "Женя"
    store.bsar_names_list.append("bsar_mz")

    bsar_colors["bsar_mt"] = {"speaker_color": "#00ea32"}
    bsar_names["bsar_mt"] = "Ольга Дмитриевна"
    store.bsar_names_list.append("bsar_mt")

    bsar_colors["bsar_un"] = {"speaker_color": "#b956ff"}
    bsar_names["bsar_un"] = "Лена"
    store.bsar_names_list.append("bsar_un")

    bsar_colors["bsar_doctor"] = {"speaker_color": "#ffffff"}
    bsar_names["bsar_doctor"] = "Доктор"
    store.bsar_names_list.append("bsar_doctor")

    bsar_colors["bsar_od"] = {"speaker_color": "#00ea32"}
    bsar_names["bsar_od"] = "ОД"
    store.bsar_names_list.append("bsar_od")

    bsar_colors["bsar_phone"] = {"speaker_color": "#6e0808"}
    bsar_names["bsar_phone"] = "Телефон"
    store.bsar_names_list.append("bsar_phone")

    bsar_colors["bsar_skaz"] = {"speaker_color": "#cccc7b"}
    bsar_names["bsar_skaz"] = "Сказаев"
    store.bsar_names_list.append("bsar_skaz")

    bsar_colors["bsar_tish"] = {"speaker_color": "#6b0202"}
    bsar_names["bsar_tish"] = "Тишкевич"
    store.bsar_names_list.append("bsar_tish")

    bsar_colors["bsar_voice"] = {"speaker_color": "#ffffff"}
    bsar_names["bsar_voice"] = "Голос"
    store.bsar_names_list.append("bsar_voice")

    def bsar_char_define(character_name, is_nvl=False):
        global DynamicCharacter
        global nvl
        global bsar_store
        global bsar_speaker_color
        bsar_gl = globals()
        
        if character_name == "bsar_narrator":
            if is_nvl:
                bsar_gl["bsar_narrator"] = Character(None, kind=nvl, what_style="bsar_text_style")
            
            else:
                bsar_gl["bsar_narrator"] = Character(None, what_style="bsar_text_style")
            
            return
        
        if character_name == "bsar_th":
            if is_nvl:
                bsar_gl["bsar_th"] = Character(None, kind=nvl, what_style="bsar_text_style", what_prefix="~ ", what_suffix=" ~")
            
            else:
                bsar_gl["bsar_th"] = Character(None, what_style="bsar_text_style", what_prefix="~ ", what_suffix=" ~")
            
            return
        
        if is_nvl:
            bsar_gl[character_name] = DynamicCharacter("%s_name" % character_name, color=store.bsar_colors[character_name][bsar_speaker_color], kind=nvl, what_style="bsar_text_style", who_suffix=":")
            bsar_gl["%s_name" % character_name] = store.bsar_names[character_name]
        
        else:
            bsar_gl[character_name] = DynamicCharacter("%s_name" % character_name, color=store.bsar_colors[character_name][bsar_speaker_color], what_style="bsar_text_style")
            bsar_gl["%s_name" % character_name]=store.bsar_names[character_name]

    def bsar_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global bsar_store
        
        for character_name in store.bsar_names_list:
            bsar_char_define(character_name)

    def bsar_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global bsar_narrator
        global bsar_th
        bsar_narrator_nvl = bsar_narrator
        th_nvl = bsar_th
        
        global bsar_store
        
        for character_name in store.bsar_names_list:
            bsar_char_define(character_name, True)

    def bsar_reload_names():
        global bsar_store
        
        for character_name in store.bsar_names_list:
            bsar_char_define(character_name)

    bsar_reload_names()

    def bsar_page_counter(n, k):
        l = float(n) / float(k)
        
        if l - int(l) > 0:
            return int(l) + 1

        else:
            return l

    def bsar_heartbeat_animation(image_name, power, zoom2, transition=None):
        renpy.show(image_name, at_list=[bsar_heartbeat_anim(image_name, power, zoom2)], tag=image_name + "_2")
        renpy.with_statement(transition)

    def bsar_set_timeofday_cursor():
        config.mouse_displayable = MouseDisplayable(bsar_gui_path + "cursors/" + persistent.timeofday + "/cursor.png", 0, 0)

    def bsar_set_dynamic_cursor(state):
        if bsar_set_timeofday_cursor in config.overlay_functions:
            config.overlay_functions.remove(bsar_set_timeofday_cursor)

        if state == "timeofday":
            config.overlay_functions.append(bsar_set_timeofday_cursor)

        elif state == "insomnia_main_menu":
            config.mouse_displayable = MouseDisplayable(bsar_gui_path + "cursors/insomnia_main_menu/cursor.png", 0, 0)

        elif state == "sotp_main_menu":
            config.mouse_displayable = MouseDisplayable(bsar_gui_path + "cursors/sotp_main_menu/cursor.png", 0, 0)

        elif state == "null":
            config.mouse_displayable = MouseDisplayable(Null(0, 0), 0, 0)

    def bsar_set_time(timeofday, sprite_time=None):
        if sprite_time is None:
            sprite_time = timeofday
        
        renpy.block_rollback()
        persistent.timeofday = "winter_" + timeofday if timeofday in ["day", "night"] else timeofday
        persistent.sprite_time = sprite_time

    def bsar_onload(type):
        global bsar_lock_quit
        global bsar_lock_quick_menu

        if type == "lock":
            renpy.config.skipping = None
            bsar_lock_quit = True
            bsar_lock_quick_menu = True
            config.allow_skipping = False

        elif type == "unlock":
            bsar_lock_quit = False
            bsar_lock_quick_menu = False
            config.allow_skipping = True       

    def bsar_show_random_words(list, k=0):
        global randow_word

        count = len(list)

        for i in range(count + 1 + k):
            randow_word = random.choice(list)
            renpy.show(
                "bsar_words_move_style randow_word", 
                at_list=[
                    bsar_words_move(
                        random.uniform(0.1, 0.5), 
                        random.random(), 
                        random.random())
                ], 
                tag="text_" + str(i)
            )

    def bsar_show_centered_text(text, style, transition=None, pause=True):
        renpy.show("text", what=Text(text, slow=True, style=style, xalign=0.5, yalign=0.5))
        renpy.with_statement(transition)

        if pause:
            renpy.pause()

    def bsar_hide_centered_text(transition=None):
        renpy.hide("text")
        renpy.with_statement(transition)

    def bsar_show_heart_monitor_phrases(phrase):
        renpy.play(bsar_heart_monitor_sound, "sound")
        renpy.show(
            "bsar_" + phrase + "_left", 
            behind=["bsar_heart_monitor_frame"],
            at_list=[bsar_heart_monitor_phrases_position(0)]
        )
        renpy.with_statement(bsar_heart_monitor_transition)
        bsar_show_centered_text(
            bsar_heart_monitor_phrases[phrase][0], 
            transition=bsar_heart_monitor_transition,
            pause=False, 
            style=style.bsar_centered_text_style_heart_monitor
        )
        renpy.show(
            "bsar_" + phrase + "_right", 
            behind=["bsar_heart_monitor_frame"], 
            at_list=[
                bsar_heart_monitor_phrases_position(bsar_heart_monitor_phrases[phrase][1])
            ]
        )
        renpy.with_statement(bsar_heart_monitor_transition)
        renpy.pause()
        renpy.hide("bsar_" + phrase + "_left")
        renpy.hide("text")
        renpy.hide("bsar_" + phrase + "_right")
        renpy.with_statement(bsar_heart_monitor_transition)
        renpy.pause(0.5, hard=True)

    def bsar_frame_animation(image_name, frames_count, retention, loop, transition, start=1, **properties):
        anim_args = []
        
        for i in range(start, start + frames_count):
            anim_args.append(renpy.display.im.image(image_name + "_" + str(i) + ".png"))
            
            if loop:
                anim_args.append(retention)
                anim_args.append(transition)
        
        return anim.TransitionAnimation(*anim_args, **properties)

    def bsar_new_chapter(story_name, part, phrases=[]):
        global save_name

        insomnia_days = {
            "День первый.": 1,
            "День второй.": 2,
            "День третий.": 3
        }

        renpy.block_rollback()
        bsar_set_dynamic_cursor("null")
        bsar_onload("lock")
        save_name = story_name + "\n" + part
        renpy.pause(2, hard=True)

        if story_name == "Бессонница.":
            insomnia_day_number = insomnia_days.get(part)
            renpy.movie_cutscene(bsar_gui_path + "days_transitions/bsar_insomnia_day{}.ogv".format(insomnia_day_number))
            renpy.pause(0.5, hard=True)

        elif story_name in ["Три смерти.", "Тени."]:
            bsar_show_centered_text(story_name + " " + part, style=style.bsar_sotp_centered_text_style, transition=dissolve)
            renpy.pause(0.5, hard=True)
            bsar_hide_centered_text(dissolve)
            renpy.pause(0.5, hard=True)

            if story_name == "Тени.":
                for phrase in phrases:
                    bsar_show_centered_text(phrase, style=style.bsar_sotp_centered_text_style, transition=dissolve)
                    renpy.pause(0.5, hard=True)
                    bsar_hide_centered_text(dissolve)
                    renpy.pause(0.5, hard=True)

        bsar_set_dynamic_cursor("timeofday")
        renpy.pause(2, hard=True)
        bsar_onload("unlock")
        renpy.block_rollback()

    def bsar_snow(image, max_particles=50, speed=150, wind=100, xborder=(0, 100), yborder=(50, 400), **kwargs):
        return Particles(BsarSnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    class BsarSnowFactory(object):
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            self.max_particles = max_particles
            self.speed = speed
            self.wind = wind
            self.xborder = xborder
            self.yborder = yborder
            self.depth = kwargs.get("depth", 10)
            self.image = self.image_init(image)

        def create(self, particles, st):
            if particles is None or len(particles) < self.max_particles:
                depth = random.randint(1, self.depth)
                depth_speed = 1.5 - depth / (self.depth + 0.0)
                
                return [BsarSnowParticle(self.image[depth - 1], 
                        random.uniform(-self.wind, self.wind) * depth_speed,
                        self.speed * depth_speed,
                        random.randint(self.xborder[0], self.xborder[1]),
                        random.randint(self.yborder[0], self.yborder[1])) 
                        ]
        
        def image_init(self, image):
            rv = [ ]
            
            for depth in range(self.depth):
                p = 1.1 - depth / (self.depth + 0.0)

                if p > 1:
                    p = 1.0
                
                rv.append(im.FactorScale(im.Alpha(image, p), p))

            return rv
        
        def predict(self):
            return self.image
            
    class BsarSnowParticle(object):
        def __init__(self, image, wind, speed, xborder, yborder):
            self.image = image
            
            if speed <= 0:
                speed = 1
                
            self.wind = wind
            self.speed = speed
            self.oldst = None         
            self.xpos = random.uniform(0 - xborder, renpy.config.screen_width + xborder)
            self.ypos = -yborder
            
        def update(self, st):
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            if self.ypos > renpy.config.screen_height or\
                (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                return None

            return int(self.xpos), int(self.ypos), st, self.image

    class BsarDispTextStyle():
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
            self.bsar_scare_tag = None

        def bsar_add_tags(self, char):
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
                self.bsar_scare_tag = char
                return True

            elif tag == "/sc":
                self.bsar_scare_tag = None
                return True

            return False

        def bsar_apply_style(self, char):
            new_string = ""

            if self.bsar_scare_tag is not None:
                new_string += "{" + self.bsar_scare_tag + "}"
                
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

            if self.bsar_scare_tag is not None:
                new_string += "{/" + self.bsar_scare_tag + "}"

            return new_string

        def bsar_start_tags(self):
            new_string = ""

            if self.bsar_scare_tag is not None:
                new_string += "{" + self.bsar_scare_tag + "}"

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

        def bsar_end_tags(self):
            new_string = ""

            if self.bsar_scare_tag is not None:
                new_string += "{/" + self.bsar_scare_tag + "}"

            return new_string

    class BsarScareText(renpy.Displayable):
        def __init__(self, child, square = 2, **kwargs):
            super(BsarScareText, self).__init__(**kwargs)
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

    def bsar_scare_tag(tag, argument, contents):
        new_list = [ ]

        if argument == "":
            argument = 5

        scare_style = BsarDispTextStyle()

        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(scare_style.bsar_apply_style(char))
                    char_disp = BsarScareText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))

            elif kind == renpy.TEXT_TAG:
                if not scare_style.bsar_add_tags(text):
                    new_list.append((kind, text))

            else:
                new_list.append((kind,text))

        return new_list    

    config.custom_text_tags["bsar_scare"] = bsar_scare_tag

    if persistent.bsar_insomnia_achievements == None:
        persistent.bsar_insomnia_achievements = {}

    persistent.bsar_insomnia_achievements.setdefault("bsar_insomnia_paradise", False)
    persistent.bsar_insomnia_achievements.setdefault("bsar_insomnia_awakening", False)
    persistent.bsar_insomnia_achievements.setdefault("bsar_insomnia_murderous_snowball", False)

    if persistent.bsar_sotp_achievements == None:
        persistent.bsar_sotp_achievements = {}

    persistent.bsar_sotp_achievements.setdefault("bsar_sotp_begining_and_end", False)
    persistent.bsar_sotp_achievements.setdefault("bsar_sotp_better", False)

    if persistent.bsar_current_story == None:
        persistent.bsar_current_story = "insomnia"

    def bsar_show_achievement(achievement_name):
        renpy.play(sfx_achievement)
        renpy.show(achievement_name, [bsar_achievement_transform])
        renpy.pause(4, hard=True)
        renpy.hide(achievement_name)

init:
    $ bsar_insomnia_paradise_ending_v = 0
    $ bsar_insomnia_day1_stroll = False
    $ bsar_insomnia_day2_intervene = False

    $ bsar_insomnia_day2_amnesia_scene = ["Мог ли я быть знаком с Ульяной? ", "Чем занимаются родители?", "Где учусь?", "???"]

    $ bsar_heart_monitor_phrases = {
        "military_service": ["Служба в армии", 1179],
        "composure": ["Хладнокровие", 1149],
        "institute": ["Институт", 1089],
        "meeting_with_her": ["Встреча с ней", 1155],
        "love": ["Пветёа4", 1069],
        "police_work": ["Работа в полиции", 1215],
        "0apv4": ["0 АПВ 4", 978],
        "fox": ["Лис", 1038],
        "friendship": ["Дружба", 1061],
        "rest": ["Покой", 975],
        "easy_money": ["Лёгкие деньги", 1163],
        "protection": ["12-18-29-26-6-3-1-15-10-6", 1373],
        "drug_trafficking": ["15-1-18-12-16-16-2-16-18-16-20", 1516],
        "sisters_death": ["Шулчщг шлшщчв7", 946],
        "nightmares": ["Кошмары", 1059],
        "doubts": ["Сомнения", 976],
        "new_deal": ["15-16-3-1-33 19-5-6-13-12-1", 1404],
        "her_death": ["Её смерть", 1086],
        "sleep_that_knows_no_breaking": ["Сон", 1038]
    }

    $ bsar_heart_monitor_transition = ImageDissolve(bsar_gui_path + "effects/heart_monitor/bsar_hm_trans.png", 0.6, ramplen=8, reverse=False, alpha=True)
    $ bsar_flash = Fade(0.45, 1.0, 0.45, color="#ffff")

#     $ bsar_titles_text = '''Спасибо за прочтение! Вот уже прошло практически два года как мы начали делать модификации и именно этот проект является важной вехой нашей деятельности, ибо с него всё и начиналось.

# Искренне надеемся, что ремейк Бессонницы вам понравился.

# Над модом работали:
# СЦЕНАРИЙ
# Ева Миронова

# КОД
# Андрей Катаев

# ВИЗУАЛЬНАЯ СОСТАВЛЯЮЩАЯ
# Егор Бобков
# Лиза Степанцова
# Егор Козаченко
# Anna Monster
# Семён Персунов
# Александр Ларин

# МУЗЫКАЛЬНОЕ СОПРОВОЖДЕНИЕ
# Дмитрий Таранов
# Алан Кокоев

# ОТДЕЛЬНЫЕ БЛАГОДАРНОСТИ
# Александр Милютин
# Родион Егоров
# Саша Шмелев
# Илья Можайкин
# Женя Двойкин

# Спасибо всем за поддержку. Ваши оценки и отзывы очень важны для нас и мотивируют работать дальше! С уважением, команда Zero Impact.

# С новым годом!'''

    image bsar_titles_final = ParameterizedText(style="bsar_titles_style", size=40, xalign=0.5)

    image bsar_heavy_snow_day = bsar_snow(bsar_gui_path + "effects/bsar_snow_particle_day.png", max_particles=500)
    image bsar_normal_snow_day = bsar_snow(bsar_gui_path + "effects/bsar_snow_particle_day.png")

    image bsar_heavy_snow_night = bsar_snow(bsar_gui_path + "effects/bsar_snow_particle_night.png", max_particles=500)
    image bsar_normal_snow_night = bsar_snow(bsar_gui_path + "effects/bsar_snow_particle_night.png")

    $ bsar_main_menu_var = True
    $ bsar_lock_quit = False
    $ bsar_lock_quick_menu = False
    $ bsar_lock_quit_game_main_menu_var = True

    image bsar_static_noise_anim = bsar_frame_animation("bsar/images/bg/bsar_static_noise_anim/bsar_static_noise", 5, 0.2, True, Dissolve(0.2))

    image bsar_insomnia_main_menu_bg = Movie(fps=30, play=bsar_gui_path + "insomnia_main_menu/bsar_insomnia_main_menu_background.ogv")
    image bsar_sotp_main_menu_bg = Movie(fps=30, play=bsar_gui_path + "sotp_main_menu/bsar_sotp_main_menu_background.ogv")

    image bsar_words_move_style = ParameterizedText(style="settings_link", size = 100, color = "fff")

    image bsar_she_night = im.MatrixColor("bsar/images/sprites/she/bsar_she normal.png", im.matrix.tint(0.63, 0.78, 0.82))

    image bg bsar_int_house_of_mt_day_blurred = im.Blur("images/bg/int_house_of_mt_day.jpg", 1.5)

    image bsar_blank_skip = renpy.display.behavior.ImageButton(Null(1920, 1080), Null(1920, 1080), clicked=[Jump("bsar_after_intro")])

    image bsar_snow_layer0_anim:
        contains:
            "bsar_snow_layer0_img"
            bsar_snow_move(8, 0.0, -0.05)

        contains:
            "bsar_snow_layer0_img"
            bsar_snow_move(8, 0.25, -0.05)

        contains:
            "bsar_snow_layer0_img"
            bsar_snow_move(8, 0.5, -0.05)

        contains:
            "bsar_snow_layer0_img"
            bsar_snow_move(8, 0.75, -0.05)

    image bsar_snow_layer1_anim:
        contains:
            "bsar_snow_layer1_img"
            bsar_snow_move(10, 0.0, 0.05, pause_time=0.5)

        contains:
            "bsar_snow_layer1_img"
            bsar_snow_move(10, 0.25, 0.05, pause_time=0.5)

        contains:
            "bsar_snow_layer1_img"
            bsar_snow_move(10, 0.5, 0.05, pause_time=0.5)

        contains:
            "bsar_snow_layer1_img"
            bsar_snow_move(10, 0.75, 0.05, pause_time=0.5)


    image bsar_snow_layer2_anim:
        contains:
            "bsar_snow_layer2_img"
            bsar_snow_move(15, 0.0, -0.05, pause_time=1.0)

        contains:
            "bsar_snow_layer2_img"
            bsar_snow_move(15, 0.25, -0.05, pause_time=1.0)

        contains:
            "bsar_snow_layer2_img"
            bsar_snow_move(15, 0.5, -0.05, pause_time=1.0)

        contains:
            "bsar_snow_layer2_img"
            bsar_snow_move(15, 0.75, -0.05, pause_time=1.0)

    image bsar_snow_layer3_anim:
        contains:
            "bsar_snow_layer3_img"
            bsar_snow_move(20, 0.0, 0.07)

        contains:
            "bsar_snow_layer3_img"
            bsar_snow_move(20, 0.25, 0.07)

        contains:
            "bsar_snow_layer3_img"
            bsar_snow_move(20, 0.5, 0.07)

        contains:
            "bsar_snow_layer3_img"
            bsar_snow_move(20, 0.75, 0.07)

    image bsar_snow_layer0_anim_quick:
        contains:
            "bsar_snow_layer0_img"
            bsar_snow_move(3, 0.0, -0.03)

        contains:
            "bsar_snow_layer0_img"
            bsar_snow_move(3, 0.25, -0.03)

        contains:
            "bsar_snow_layer0_img"
            bsar_snow_move(3, 0.5, -0.03)

        contains:
            "bsar_snow_layer0_img"
            bsar_snow_move(3, 0.75, -0.03)

    image bsar_snow_layer1_anim_quick:
        contains:
            "bsar_snow_layer1_img"
            bsar_snow_move(4, 0.0, 0.05)

        contains:
            "bsar_snow_layer1_img"
            bsar_snow_move(4, 0.25, 0.05)

        contains:
            "bsar_snow_layer1_img"
            bsar_snow_move(4, 0.5, 0.05)

        contains:
            "bsar_snow_layer1_img"
            bsar_snow_move(4, 0.75, 0.05)

    image bsar_snow_layer2_anim_quick:
        contains:
            "bsar_snow_layer2_img"
            bsar_snow_move(5, 0.0, -0.05)

        contains:
            "bsar_snow_layer2_img"
            bsar_snow_move(5, 0.25, -0.05)

        contains:
            "bsar_snow_layer2_img"
            bsar_snow_move(5, 0.5, -0.05)

        contains:
            "bsar_snow_layer2_img"
            bsar_snow_move(5, 0.75, -0.05)

    image bsar_snow_layer3_anim_quick:
        contains:
            "bsar_snow_layer3_img"
            bsar_snow_move(5, 0.0, 0.03)

        contains:
            "bsar_snow_layer3_img"
            bsar_snow_move(5, 0.25, 0.03)

        contains:
            "bsar_snow_layer3_img"
            bsar_snow_move(5, 0.5, 0.03)
            
        contains:
            "bsar_snow_layer3_img"
            bsar_snow_move(5, 0.75, 0.03)

    transform bsar_buttons_atl():
        on idle:
            easein 0.5 zoom 1.0

        on hover:
            easein 0.5 zoom 1.05

    transform bsar_snow_move(time, start_pos, x_deviation=0.05, pause_time=0.0, fade_time=1.0):
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

    transform bsar_zoom_qte_text:
        zoom 1.0
        block:
            linear 2.0 zoom 1.4
            linear 2.0 zoom 0.5
            repeat

    transform bsar_heart_monitor_phrases_position(x):
        xpos x
        ypos 264

    transform bsar_full_rotate_repeat(l, z, x, y):
        parallel:
            zoom z
            xalign x
            yalign y 
            rotate_pad True
            rotate 0
            linear l rotate 360
            repeat

    transform bsar_zoom_in_center():
        xalign 0.5 yalign 0.5 zoom 1.0
        pause 2.0
        linear 20 zoom 2.0 xalign 0.5 yalign 0.5

    transform bsar_name_header_pos():
        xalign 0.5
        yalign 0.045

    transform bsar_loading_text_pos():
        xalign 0.5 ypos 840

    transform bsar_first_dot_pos():
        xpos 1140
        ypos 843

    transform bsar_second_dot_pos():
        xpos 1150
        ypos 843

    transform bsar_third_dot_pos():
        xpos 1160
        ypos 843

    transform bsar_heartbeat_anim(image_name, power, zoom2):
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

    transform bsar_achievement_transform:
        align(1.2, 0.9)
        ease 1.0 align(0.85, 0.9)
        ease 0.5 align(0.95, 0.9)
        pause 1.5
        ease 0.5 align(1.5, 0.9)

    transform bsar_titles_anim():
        xalign 0.5
        ypos 1.1
        linear 38 ypos -2.0

    transform bsar_dream_catcher_anim():
        ease 0.4 xoffset -5 rotate -0.4
        ease 0.4 xoffset 5 rotate 0
        ease 0.4 xoffset 0 rotate 0.4
        repeat

    transform bsar_skip_pos():
        xalign 0.5
        ypos 900

    transform bsar_words_move(z, x, y):
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