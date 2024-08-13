style bsar_scared_text_red_large:
    color "#aa0000"
    size 30
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]

style bsar_scared_text_red_small:
    color "#aa0000"
    size 25
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]

style bsar_scared_text_centered:
    color "#aa0000"
    size 80
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]    

style bsar_scared_text_style_large:
    color "#ffffff"
    size 30
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]

style bsar_scared_text_style_small:
    color "#ffffff"
    size 25
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]

style bsar_qte_text:
    size 40
    color "#ffffff"
    outlines [(2, "#002b74", absolute(0), absolute(0))]

init -1 python:
    bsar_gui_path = "bsar/images/gui/"
    bsar_verdana = bsar_gui_path + "fonts/Verdana.ttf"
    bsar_flow_ext = bsar_gui_path + "fonts/flow_ext.otf"
    bsar_diamond_girl_skinny = bsar_gui_path + "fonts/diamond_girl_skinny.otf"
    bsar_electronical = bsar_gui_path + "fonts/electronical.otf"

    bsar_preferences_text = "Настройки"
    bsar_extra_text = "Дополнительно"
    bsar_return_text = "Назад"
    bsar_delete_text = "Удалить"
    bsar_display_preferences_text = "Режим экрана"
    bsar_yes_text = "Да"
    bsar_no_text = "Нет"

    style.bsar_titles_style = Style(style.default)
    style.bsar_titles_style.font = bsar_flow_ext
    style.bsar_titles_style.color = "#fff"
    style.bsar_titles_style.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    style.bsar_titles_style.drop_shadow_color = "#000"
    style.bsar_titles_style.italic = False
    style.bsar_titles_style.bold = False
    style.bsar_titles_style.text_align = 0.5
    style.bsar_titles_style.xmaximum = 0.8
    
    style.bsar_button_none = Style(style.button)
    style.bsar_button_none.background = None
    style.bsar_button_none.hover_background = None
    style.bsar_button_none.selected_background = None
    style.bsar_button_none.selected_hover_background = None
    style.bsar_button_none.selected_idle_background = None

    style.bsar_text_style = Style(style.default)
    style.bsar_text_style.color = "#ffffff"
    style.bsar_text_style.drop_shadow = (2, 2)
    style.bsar_text_style.drop_shadow_color = "#000"

    style.bsar_main_menu_text_style = Style(style.default)
    style.bsar_main_menu_text_style.font = bsar_flow_ext
    style.bsar_main_menu_text_style.color = "#ffffff"
    style.bsar_main_menu_text_style.size = 70

    style.bsar_preferences_main_menu_text_style = Style(style.default)
    style.bsar_preferences_main_menu_text_style.font = bsar_flow_ext
    style.bsar_preferences_main_menu_text_style.color = "#b3b3b3"
    style.bsar_preferences_main_menu_text_style.hover_color = "#ffffff"
    style.bsar_preferences_main_menu_text_style.selected_color = "#ffffff"
    style.bsar_preferences_main_menu_text_style.size = 60
    
    style.bsar_preferences_main_menu_text_style_inverse = Style(style.default)
    style.bsar_preferences_main_menu_text_style_inverse.font = bsar_flow_ext
    style.bsar_preferences_main_menu_text_style_inverse.color = "#ffffff"
    style.bsar_preferences_main_menu_text_style_inverse.hover_color = "#ffffff"
    style.bsar_preferences_main_menu_text_style_inverse.selected_color = "#ffffff"
    style.bsar_preferences_main_menu_text_style_inverse.size = 60

    style.bsar_centered_text_style = Style(style.default)
    style.bsar_centered_text_style.color = "#ffffff"
    style.bsar_centered_text_style.drop_shadow = (2, 2)
    style.bsar_centered_text_style.drop_shadow_color = "#000"
    style.bsar_centered_text_style.size = 80

    style.bsar_centered_text_style_heart_monitor = Style(style.default)
    style.bsar_centered_text_style_heart_monitor.font = bsar_electronical
    style.bsar_centered_text_style_heart_monitor.color = "#028702"
    style.bsar_centered_text_style_heart_monitor.drop_shadow = (2, 2)
    style.bsar_centered_text_style_heart_monitor.drop_shadow_color = "#000"
    style.bsar_centered_text_style_heart_monitor.size = 80

    style.bsar_quick_menu_style_winter_day = Style(style.default)
    style.bsar_quick_menu_style_winter_day.font = bsar_flow_ext
    style.bsar_quick_menu_style_winter_day.size = 60
    style.bsar_quick_menu_style_winter_day.color = "#ffffff"
    style.bsar_quick_menu_style_winter_day.hover_color = "#2171b8"
    style.bsar_quick_menu_style_winter_day.selected_color = "#2171b8"

    style.bsar_quick_menu_style_winter_night = Style(style.default)
    style.bsar_quick_menu_style_winter_night.font = bsar_flow_ext
    style.bsar_quick_menu_style_winter_night.size = 60
    style.bsar_quick_menu_style_winter_night.color = "#ffffff"
    style.bsar_quick_menu_style_winter_night.hover_color = "#002b74"
    style.bsar_quick_menu_style_winter_night.selected_color = "#002b74"

    style.bsar_quick_menu_style_bw = Style(style.default)
    style.bsar_quick_menu_style_bw.font = bsar_flow_ext
    style.bsar_quick_menu_style_bw.size = 60
    style.bsar_quick_menu_style_bw.color = "#ffffff"
    style.bsar_quick_menu_style_bw.hover_color = "#dcd168"
    style.bsar_quick_menu_style_bw.selected_color = "#dcd168"

    style.bsar_quick_menu_style_fog = Style(style.default)
    style.bsar_quick_menu_style_fog.font = bsar_flow_ext
    style.bsar_quick_menu_style_fog.size = 60
    style.bsar_quick_menu_style_fog.color = "#ffffff"
    style.bsar_quick_menu_style_fog.hover_color = "#c2dded"
    style.bsar_quick_menu_style_fog.selected_color = "#c2dded"

    style.bsar_text_history = Style(style.default)
    style.bsar_text_history.font = bsar_verdana
    style.bsar_text_history.color = "#ffffff"
    style.bsar_text_history.drop_shadow = (2, 2)
    style.bsar_text_history.drop_shadow_color = "#000"
    style.bsar_text_history.size = 28
    style.bsar_text_history.line_spacing = 2

    style.bsar_save_load_button_main_menu = Style(style.button)
    style.bsar_save_load_button_main_menu.background = bsar_gui_path + "save_load/main_menu/save_load_button_idle.png"
    style.bsar_save_load_button_main_menu.hover_background = bsar_gui_path + "save_load/main_menu/save_load_button_hover.png"
    style.bsar_save_load_button_main_menu.selected_background = bsar_gui_path + "save_load/main_menu/save_load_button_selected.png"
    style.bsar_save_load_button_main_menu.selected_hover_background = bsar_gui_path + "save_load/main_menu/save_load_button_selected.png"
    style.bsar_save_load_button_main_menu.selected_idle_background = bsar_gui_path + "save_load/main_menu/save_load_button_selected.png"

    style.bsar_save_load_winter_day = Style(style.default)
    style.bsar_save_load_winter_day.font = bsar_flow_ext
    style.bsar_save_load_winter_day.size = 60
    style.bsar_save_load_winter_day.kerning = 3
    style.bsar_save_load_winter_day.color = "#ffffff"
    style.bsar_save_load_winter_day.hover_color = "#2171b8"
    style.bsar_save_load_winter_day.selected_color = "#ffffff"
    style.bsar_save_load_winter_day.selected_idle_color = "#ffffff"
    style.bsar_save_load_winter_day.selected_hover_color = "#2171b8"
    style.bsar_save_load_winter_day.insensitive_color = "#ffffff"

    style.bsar_text_winter_day = Style(style.default)
    style.bsar_text_winter_day.font = bsar_flow_ext
    style.bsar_text_winter_day.size = 60
    style.bsar_text_winter_day.color = "#ffffff"
    style.bsar_text_winter_day.hover_color = "#2171b8"
    style.bsar_text_winter_day.selected_color = "#ffffff"
    style.bsar_text_winter_day.selected_idle_color = "#ffffff"
    style.bsar_text_winter_day.selected_hover_color = "#2171b8"
    style.bsar_text_winter_day.insensitive_color = "#ffffff"

    style.bsar_save_load_button_winter_day = Style(style.button)
    style.bsar_save_load_button_winter_day.background = bsar_gui_path + "save_load/winter_day/save_load_button_idle.png"
    style.bsar_save_load_button_winter_day.hover_background = bsar_gui_path + "save_load/winter_day/save_load_button_hover.png"
    style.bsar_save_load_button_winter_day.selected_background = bsar_gui_path + "save_load/winter_day/save_load_button_selected.png"
    style.bsar_save_load_button_winter_day.selected_hover_background = bsar_gui_path + "save_load/winter_day/save_load_button_selected.png"
    style.bsar_save_load_button_winter_day.selected_idle_background = bsar_gui_path + "save_load/winter_day/save_load_button_selected.png"

    style.bsar_text_preferences_winter_day = Style(style.default)
    style.bsar_text_preferences_winter_day.font = bsar_flow_ext
    style.bsar_text_preferences_winter_day.size = 60
    style.bsar_text_preferences_winter_day.color = "#ffffff"
    style.bsar_text_preferences_winter_day.hover_color = "#2171b8"
    style.bsar_text_preferences_winter_day.selected_color = "#2171b8"

    style.bsar_text_inverse_preferences_winter_day = Style(style.default)
    style.bsar_text_inverse_preferences_winter_day.font = bsar_flow_ext
    style.bsar_text_inverse_preferences_winter_day.size = 60
    style.bsar_text_inverse_preferences_winter_day.color = "#2171b8"
    style.bsar_text_inverse_preferences_winter_day.hover_color = "#2171b8"
    style.bsar_text_inverse_preferences_winter_day.selected_color = "#2171b8"

    style.bsar_save_load_winter_night = Style(style.default)
    style.bsar_save_load_winter_night.font = bsar_flow_ext
    style.bsar_save_load_winter_night.size = 60
    style.bsar_save_load_winter_night.kerning = 3
    style.bsar_save_load_winter_night.color = "#ffffff"
    style.bsar_save_load_winter_night.hover_color = "#002b74"
    style.bsar_save_load_winter_night.selected_color = "#ffffff"
    style.bsar_save_load_winter_night.selected_idle_color = "#ffffff"
    style.bsar_save_load_winter_night.selected_hover_color = "#002b74"
    style.bsar_save_load_winter_night.insensitive_color = "#ffffff"

    style.bsar_text_winter_night = Style(style.default)
    style.bsar_text_winter_night.font = bsar_flow_ext
    style.bsar_text_winter_night.size = 60
    style.bsar_text_winter_night.color = "#ffffff"
    style.bsar_text_winter_night.hover_color = "#002b74"
    style.bsar_text_winter_night.selected_color = "#ffffff"
    style.bsar_text_winter_night.selected_idle_color = "#ffffff"
    style.bsar_text_winter_night.selected_hover_color = "#002b74"
    style.bsar_text_winter_night.insensitive_color = "#ffffff"

    style.bsar_text_preferences_winter_night = Style(style.default)
    style.bsar_text_preferences_winter_night.font = bsar_flow_ext
    style.bsar_text_preferences_winter_night.size = 60
    style.bsar_text_preferences_winter_night.color = "#ffffff"
    style.bsar_text_preferences_winter_night.hover_color = "#002b74"
    style.bsar_text_preferences_winter_night.selected_color = "#002b74"

    style.bsar_text_inverse_preferences_winter_night = Style(style.default)
    style.bsar_text_inverse_preferences_winter_night.font = bsar_flow_ext
    style.bsar_text_inverse_preferences_winter_night.size = 60
    style.bsar_text_inverse_preferences_winter_night.color = "#002b74"
    style.bsar_text_inverse_preferences_winter_night.hover_color = "#002b74"
    style.bsar_text_inverse_preferences_winter_night.selected_color = "#002b74"

    style.bsar_save_load_button_winter_night = Style(style.button)
    style.bsar_save_load_button_winter_night.background = bsar_gui_path + "save_load/winter_night/save_load_button_idle.png"
    style.bsar_save_load_button_winter_night.hover_background = bsar_gui_path + "save_load/winter_night/save_load_button_hover.png"
    style.bsar_save_load_button_winter_night.selected_background = bsar_gui_path + "save_load/winter_night/save_load_button_selected.png"
    style.bsar_save_load_button_winter_night.selected_hover_background = bsar_gui_path + "save_load/winter_night/save_load_button_selected.png"
    style.bsar_save_load_button_winter_night.selected_idle_background = bsar_gui_path + "save_load/winter_night/save_load_button_selected.png"

    style.bsar_save_load_bw = Style(style.default)
    style.bsar_save_load_bw.font = bsar_flow_ext
    style.bsar_save_load_bw.size = 60
    style.bsar_save_load_bw.kerning = 3
    style.bsar_save_load_bw.color = "#ffffff"
    style.bsar_save_load_bw.hover_color = "#dcd168"
    style.bsar_save_load_bw.selected_color = "#ffffff"
    style.bsar_save_load_bw.selected_idle_color = "#ffffff"
    style.bsar_save_load_bw.selected_hover_color = "#dcd168"
    style.bsar_save_load_bw.insensitive_color = "#ffffff"

    style.bsar_text_bw = Style(style.default)
    style.bsar_text_bw.font = bsar_flow_ext
    style.bsar_text_bw.size = 60
    style.bsar_text_bw.color = "#ffffff"
    style.bsar_text_bw.hover_color = "#dcd168"
    style.bsar_text_bw.selected_color = "#ffffff"
    style.bsar_text_bw.selected_idle_color = "#ffffff"
    style.bsar_text_bw.selected_hover_color = "#dcd168"
    style.bsar_text_bw.insensitive_color = "#ffffff"

    style.bsar_save_load_button_bw = Style(style.button)
    style.bsar_save_load_button_bw.background = bsar_gui_path + "save_load/bw/save_load_button_idle.png"
    style.bsar_save_load_button_bw.hover_background = bsar_gui_path + "save_load/bw/save_load_button_hover.png"
    style.bsar_save_load_button_bw.selected_background = bsar_gui_path + "save_load/bw/save_load_button_selected.png"
    style.bsar_save_load_button_bw.selected_hover_background = bsar_gui_path + "save_load/bw/save_load_button_selected.png"
    style.bsar_save_load_button_bw.selected_idle_background = bsar_gui_path + "save_load/bw/save_load_button_selected.png"

    style.bsar_text_preferences_bw = Style(style.default)
    style.bsar_text_preferences_bw.font = bsar_flow_ext
    style.bsar_text_preferences_bw.size = 60
    style.bsar_text_preferences_bw.color = "#ffffff"
    style.bsar_text_preferences_bw.hover_color = "#dcd168"
    style.bsar_text_preferences_bw.selected_color = "#dcd168"

    style.bsar_text_inverse_preferences_bw = Style(style.default)
    style.bsar_text_inverse_preferences_bw.font = bsar_flow_ext
    style.bsar_text_inverse_preferences_bw.size = 60
    style.bsar_text_inverse_preferences_bw.color = "#dcd168"
    style.bsar_text_inverse_preferences_bw.hover_color = "#dcd168"
    style.bsar_text_inverse_preferences_bw.selected_color = "#dcd168"

    style.bsar_text_fog = Style(style.default)
    style.bsar_text_fog.font = bsar_flow_ext
    style.bsar_text_fog.size = 60
    style.bsar_text_fog.color = "#ffffff"
    style.bsar_text_fog.hover_color = "#c2dded"
    style.bsar_text_fog.selected_color = "#ffffff"
    style.bsar_text_fog.selected_idle_color = "#ffffff"
    style.bsar_text_fog.selected_hover_color = "#c2dded"
    style.bsar_text_fog.insensitive_color = "#ffffff"

    style.bsar_save_load_fog = Style(style.default)
    style.bsar_save_load_fog.font = bsar_flow_ext
    style.bsar_save_load_fog.size = 60
    style.bsar_save_load_fog.kerning = 3
    style.bsar_save_load_fog.color = "#ffffff"
    style.bsar_save_load_fog.hover_color = "#c2dded"
    style.bsar_save_load_fog.selected_color = "#ffffff"
    style.bsar_save_load_fog.selected_idle_color = "#ffffff"
    style.bsar_save_load_fog.selected_hover_color = "#c2dded"
    style.bsar_save_load_fog.insensitive_color = "#ffffff"

    style.bsar_save_load_button_fog = Style(style.button)
    style.bsar_save_load_button_fog.background = bsar_gui_path + "save_load/fog/save_load_button_idle.png"
    style.bsar_save_load_button_fog.hover_background = bsar_gui_path + "save_load/fog/save_load_button_hover.png"
    style.bsar_save_load_button_fog.selected_background = bsar_gui_path + "save_load/fog/save_load_button_selected.png"
    style.bsar_save_load_button_fog.selected_hover_background = bsar_gui_path + "save_load/fog/save_load_button_selected.png"
    style.bsar_save_load_button_fog.selected_idle_background = bsar_gui_path + "save_load/fog/save_load_button_selected.png"

    style.bsar_text_preferences_fog = Style(style.default)
    style.bsar_text_preferences_fog.font = bsar_flow_ext
    style.bsar_text_preferences_fog.size = 60
    style.bsar_text_preferences_fog.color = "#ffffff"
    style.bsar_text_preferences_fog.hover_color = "#c2dded"
    style.bsar_text_preferences_fog.selected_color = "#c2dded"

    style.bsar_text_inverse_preferences_fog = Style(style.default)
    style.bsar_text_inverse_preferences_fog.font = bsar_flow_ext
    style.bsar_text_inverse_preferences_fog.size = 60
    style.bsar_text_inverse_preferences_fog.color = "#c2dded"
    style.bsar_text_inverse_preferences_fog.hover_color = "#c2dded"
    style.bsar_text_inverse_preferences_fog.selected_color = "#c2dded"