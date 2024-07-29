style insomnia_scared_text_red_large:
    color "#aa0000"
    size 30
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]

style insomnia_scared_text_red_small:
    color "#aa0000"
    size 25
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]

style insomnia_scared_text_centered:
    color "#aa0000"
    size 80
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]    

style insomnia_scared_text_style_large:
    color "#ffffff"
    size 30
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]

style insomnia_scared_text_style_small:
    color "#ffffff"
    size 25
    outlines [(absolute(2), "#000", absolute(2), absolute(2))]

style insomnia_qte_text:
    size 40
    color "#ffffff"
    outlines [(2, "#002b74", absolute(0), absolute(0))]

init -1 python:
    insomnia_gui_path = "insomnia/images/gui/"
    insomnia_verdana = insomnia_gui_path + "fonts/Verdana.ttf"
    insomnia_flow_ext = insomnia_gui_path + "fonts/flow_ext.otf"
    insomnia_diamond_girl_skinny = insomnia_gui_path + "fonts/diamond_girl_skinny.otf"
    insomnia_electronical = insomnia_gui_path + "fonts/electronical.otf"

    insomnia_load_text = "Загрузить"
    insomnia_preferences_text = "Настройки"
    insomnia_extra_text = "Дополнительно"
    insomnia_return_text = "Назад"
    insomnia_delete_text = "Удалить"
    insomnia_display_preferences_text = "Режим экрана"
    insomnia_yes_text = "Да"
    insomnia_no_text = "Нет"

    style.insomnia_titles_style = Style(style.default)
    style.insomnia_titles_style.font = insomnia_flow_ext
    style.insomnia_titles_style.color = "#fff"
    style.insomnia_titles_style.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    style.insomnia_titles_style.drop_shadow_color = "#000"
    style.insomnia_titles_style.italic = False
    style.insomnia_titles_style.bold = False
    style.insomnia_titles_style.text_align = 0.5
    style.insomnia_titles_style.xmaximum = 0.8
    
    style.insomnia_button_none = Style(style.button)
    style.insomnia_button_none.background = None
    style.insomnia_button_none.hover_background = None
    style.insomnia_button_none.selected_background = None
    style.insomnia_button_none.selected_hover_background = None
    style.insomnia_button_none.selected_idle_background = None

    style.insomnia_text_style = Style(style.default)
    style.insomnia_text_style.color = "#ffffff"
    style.insomnia_text_style.drop_shadow = (2, 2)
    style.insomnia_text_style.drop_shadow_color = "#000"

    style.insomnia_main_menu_text_style = Style(style.default)
    style.insomnia_main_menu_text_style.font = insomnia_flow_ext
    style.insomnia_main_menu_text_style.color = "#ffffff"
    style.insomnia_main_menu_text_style.size = 70

    style.insomnia_preferences_main_menu_text_style = Style(style.default)
    style.insomnia_preferences_main_menu_text_style.font = insomnia_flow_ext
    style.insomnia_preferences_main_menu_text_style.color = "#b3b3b3"
    style.insomnia_preferences_main_menu_text_style.hover_color = "#ffffff"
    style.insomnia_preferences_main_menu_text_style.selected_color = "#ffffff"
    style.insomnia_preferences_main_menu_text_style.size = 60
    
    style.insomnia_preferences_main_menu_text_style_inverse = Style(style.default)
    style.insomnia_preferences_main_menu_text_style_inverse.font = insomnia_flow_ext
    style.insomnia_preferences_main_menu_text_style_inverse.color = "#ffffff"
    style.insomnia_preferences_main_menu_text_style_inverse.hover_color = "#ffffff"
    style.insomnia_preferences_main_menu_text_style_inverse.selected_color = "#ffffff"
    style.insomnia_preferences_main_menu_text_style_inverse.size = 60

    style.insomnia_centered_text_style = Style(style.default)
    style.insomnia_centered_text_style.color = "#ffffff"
    style.insomnia_centered_text_style.drop_shadow = (2, 2)
    style.insomnia_centered_text_style.drop_shadow_color = "#000"
    style.insomnia_centered_text_style.size = 80

    style.insomnia_centered_text_style_heart_monitor = Style(style.default)
    style.insomnia_centered_text_style_heart_monitor.font = insomnia_electronical
    style.insomnia_centered_text_style_heart_monitor.color = "#028702"
    style.insomnia_centered_text_style_heart_monitor.drop_shadow = (2, 2)
    style.insomnia_centered_text_style_heart_monitor.drop_shadow_color = "#000"
    style.insomnia_centered_text_style_heart_monitor.size = 80

    style.insomnia_quick_menu_style_winter_day = Style(style.default)
    style.insomnia_quick_menu_style_winter_day.font = insomnia_flow_ext
    style.insomnia_quick_menu_style_winter_day.size = 60
    style.insomnia_quick_menu_style_winter_day.color = "#ffffff"
    style.insomnia_quick_menu_style_winter_day.hover_color = "#2171b8"
    style.insomnia_quick_menu_style_winter_day.selected_color = "#2171b8"

    style.insomnia_quick_menu_style_winter_night = Style(style.default)
    style.insomnia_quick_menu_style_winter_night.font = insomnia_flow_ext
    style.insomnia_quick_menu_style_winter_night.size = 60
    style.insomnia_quick_menu_style_winter_night.color = "#ffffff"
    style.insomnia_quick_menu_style_winter_night.hover_color = "#002b74"
    style.insomnia_quick_menu_style_winter_night.selected_color = "#002b74"

    style.insomnia_quick_menu_style_bw = Style(style.default)
    style.insomnia_quick_menu_style_bw.font = insomnia_flow_ext
    style.insomnia_quick_menu_style_bw.size = 60
    style.insomnia_quick_menu_style_bw.color = "#ffffff"
    style.insomnia_quick_menu_style_bw.hover_color = "#dcd168"
    style.insomnia_quick_menu_style_bw.selected_color = "#dcd168"

    style.insomnia_quick_menu_style_fog = Style(style.default)
    style.insomnia_quick_menu_style_fog.font = insomnia_flow_ext
    style.insomnia_quick_menu_style_fog.size = 60
    style.insomnia_quick_menu_style_fog.color = "#ffffff"
    style.insomnia_quick_menu_style_fog.hover_color = "#c2dded"
    style.insomnia_quick_menu_style_fog.selected_color = "#c2dded"

    style.insomnia_text_history = Style(style.default)
    style.insomnia_text_history.font = insomnia_verdana
    style.insomnia_text_history.color = "#ffffff"
    style.insomnia_text_history.drop_shadow = (2, 2)
    style.insomnia_text_history.drop_shadow_color = "#000"
    style.insomnia_text_history.size = 28
    style.insomnia_text_history.line_spacing = 2

    style.insomnia_save_load_button_main_menu = Style(style.button)
    style.insomnia_save_load_button_main_menu.background = insomnia_gui_path + "save_load/main_menu/save_load_button_idle.png"
    style.insomnia_save_load_button_main_menu.hover_background = insomnia_gui_path + "save_load/main_menu/save_load_button_hover.png"
    style.insomnia_save_load_button_main_menu.selected_background = insomnia_gui_path + "save_load/main_menu/save_load_button_selected.png"
    style.insomnia_save_load_button_main_menu.selected_hover_background = insomnia_gui_path + "save_load/main_menu/save_load_button_selected.png"
    style.insomnia_save_load_button_main_menu.selected_idle_background = insomnia_gui_path + "save_load/main_menu/save_load_button_selected.png"

    style.insomnia_save_load_winter_day = Style(style.default)
    style.insomnia_save_load_winter_day.font = insomnia_flow_ext
    style.insomnia_save_load_winter_day.size = 60
    style.insomnia_save_load_winter_day.kerning = 3
    style.insomnia_save_load_winter_day.color = "#ffffff"
    style.insomnia_save_load_winter_day.hover_color = "#2171b8"
    style.insomnia_save_load_winter_day.selected_color = "#ffffff"
    style.insomnia_save_load_winter_day.selected_idle_color = "#ffffff"
    style.insomnia_save_load_winter_day.selected_hover_color = "#2171b8"
    style.insomnia_save_load_winter_day.insensitive_color = "#ffffff"

    style.insomnia_text_winter_day = Style(style.default)
    style.insomnia_text_winter_day.font = insomnia_flow_ext
    style.insomnia_text_winter_day.size = 60
    style.insomnia_text_winter_day.color = "#ffffff"
    style.insomnia_text_winter_day.hover_color = "#2171b8"
    style.insomnia_text_winter_day.selected_color = "#ffffff"
    style.insomnia_text_winter_day.selected_idle_color = "#ffffff"
    style.insomnia_text_winter_day.selected_hover_color = "#2171b8"
    style.insomnia_text_winter_day.insensitive_color = "#ffffff"

    style.insomnia_save_load_button_winter_day = Style(style.button)
    style.insomnia_save_load_button_winter_day.background = insomnia_gui_path + "save_load/winter_day/save_load_button_idle.png"
    style.insomnia_save_load_button_winter_day.hover_background = insomnia_gui_path + "save_load/winter_day/save_load_button_hover.png"
    style.insomnia_save_load_button_winter_day.selected_background = insomnia_gui_path + "save_load/winter_day/save_load_button_selected.png"
    style.insomnia_save_load_button_winter_day.selected_hover_background = insomnia_gui_path + "save_load/winter_day/save_load_button_selected.png"
    style.insomnia_save_load_button_winter_day.selected_idle_background = insomnia_gui_path + "save_load/winter_day/save_load_button_selected.png"

    style.insomnia_text_preferences_winter_day = Style(style.default)
    style.insomnia_text_preferences_winter_day.font = insomnia_flow_ext
    style.insomnia_text_preferences_winter_day.size = 60
    style.insomnia_text_preferences_winter_day.color = "#ffffff"
    style.insomnia_text_preferences_winter_day.hover_color = "#2171b8"
    style.insomnia_text_preferences_winter_day.selected_color = "#2171b8"

    style.insomnia_text_inverse_preferences_winter_day = Style(style.default)
    style.insomnia_text_inverse_preferences_winter_day.font = insomnia_flow_ext
    style.insomnia_text_inverse_preferences_winter_day.size = 60
    style.insomnia_text_inverse_preferences_winter_day.color = "#2171b8"
    style.insomnia_text_inverse_preferences_winter_day.hover_color = "#2171b8"
    style.insomnia_text_inverse_preferences_winter_day.selected_color = "#2171b8"

    style.insomnia_save_load_winter_night = Style(style.default)
    style.insomnia_save_load_winter_night.font = insomnia_flow_ext
    style.insomnia_save_load_winter_night.size = 60
    style.insomnia_save_load_winter_night.kerning = 3
    style.insomnia_save_load_winter_night.color = "#ffffff"
    style.insomnia_save_load_winter_night.hover_color = "#002b74"
    style.insomnia_save_load_winter_night.selected_color = "#ffffff"
    style.insomnia_save_load_winter_night.selected_idle_color = "#ffffff"
    style.insomnia_save_load_winter_night.selected_hover_color = "#002b74"
    style.insomnia_save_load_winter_night.insensitive_color = "#ffffff"

    style.insomnia_text_winter_night = Style(style.default)
    style.insomnia_text_winter_night.font = insomnia_flow_ext
    style.insomnia_text_winter_night.size = 60
    style.insomnia_text_winter_night.color = "#ffffff"
    style.insomnia_text_winter_night.hover_color = "#002b74"
    style.insomnia_text_winter_night.selected_color = "#ffffff"
    style.insomnia_text_winter_night.selected_idle_color = "#ffffff"
    style.insomnia_text_winter_night.selected_hover_color = "#002b74"
    style.insomnia_text_winter_night.insensitive_color = "#ffffff"

    style.insomnia_text_preferences_winter_night = Style(style.default)
    style.insomnia_text_preferences_winter_night.font = insomnia_flow_ext
    style.insomnia_text_preferences_winter_night.size = 60
    style.insomnia_text_preferences_winter_night.color = "#ffffff"
    style.insomnia_text_preferences_winter_night.hover_color = "#002b74"
    style.insomnia_text_preferences_winter_night.selected_color = "#002b74"

    style.insomnia_text_inverse_preferences_winter_night = Style(style.default)
    style.insomnia_text_inverse_preferences_winter_night.font = insomnia_flow_ext
    style.insomnia_text_inverse_preferences_winter_night.size = 60
    style.insomnia_text_inverse_preferences_winter_night.color = "#002b74"
    style.insomnia_text_inverse_preferences_winter_night.hover_color = "#002b74"
    style.insomnia_text_inverse_preferences_winter_night.selected_color = "#002b74"

    style.insomnia_save_load_button_winter_night = Style(style.button)
    style.insomnia_save_load_button_winter_night.background = insomnia_gui_path + "save_load/winter_night/save_load_button_idle.png"
    style.insomnia_save_load_button_winter_night.hover_background = insomnia_gui_path + "save_load/winter_night/save_load_button_hover.png"
    style.insomnia_save_load_button_winter_night.selected_background = insomnia_gui_path + "save_load/winter_night/save_load_button_selected.png"
    style.insomnia_save_load_button_winter_night.selected_hover_background = insomnia_gui_path + "save_load/winter_night/save_load_button_selected.png"
    style.insomnia_save_load_button_winter_night.selected_idle_background = insomnia_gui_path + "save_load/winter_night/save_load_button_selected.png"

    style.insomnia_save_load_bw = Style(style.default)
    style.insomnia_save_load_bw.font = insomnia_flow_ext
    style.insomnia_save_load_bw.size = 60
    style.insomnia_save_load_bw.kerning = 3
    style.insomnia_save_load_bw.color = "#ffffff"
    style.insomnia_save_load_bw.hover_color = "#dcd168"
    style.insomnia_save_load_bw.selected_color = "#ffffff"
    style.insomnia_save_load_bw.selected_idle_color = "#ffffff"
    style.insomnia_save_load_bw.selected_hover_color = "#dcd168"
    style.insomnia_save_load_bw.insensitive_color = "#ffffff"

    style.insomnia_text_bw = Style(style.default)
    style.insomnia_text_bw.font = insomnia_flow_ext
    style.insomnia_text_bw.size = 60
    style.insomnia_text_bw.color = "#ffffff"
    style.insomnia_text_bw.hover_color = "#dcd168"
    style.insomnia_text_bw.selected_color = "#ffffff"
    style.insomnia_text_bw.selected_idle_color = "#ffffff"
    style.insomnia_text_bw.selected_hover_color = "#dcd168"
    style.insomnia_text_bw.insensitive_color = "#ffffff"

    style.insomnia_save_load_button_bw = Style(style.button)
    style.insomnia_save_load_button_bw.background = insomnia_gui_path + "save_load/bw/save_load_button_idle.png"
    style.insomnia_save_load_button_bw.hover_background = insomnia_gui_path + "save_load/bw/save_load_button_hover.png"
    style.insomnia_save_load_button_bw.selected_background = insomnia_gui_path + "save_load/bw/save_load_button_selected.png"
    style.insomnia_save_load_button_bw.selected_hover_background = insomnia_gui_path + "save_load/bw/save_load_button_selected.png"
    style.insomnia_save_load_button_bw.selected_idle_background = insomnia_gui_path + "save_load/bw/save_load_button_selected.png"

    style.insomnia_text_preferences_bw = Style(style.default)
    style.insomnia_text_preferences_bw.font = insomnia_flow_ext
    style.insomnia_text_preferences_bw.size = 60
    style.insomnia_text_preferences_bw.color = "#ffffff"
    style.insomnia_text_preferences_bw.hover_color = "#dcd168"
    style.insomnia_text_preferences_bw.selected_color = "#dcd168"

    style.insomnia_text_inverse_preferences_bw = Style(style.default)
    style.insomnia_text_inverse_preferences_bw.font = insomnia_flow_ext
    style.insomnia_text_inverse_preferences_bw.size = 60
    style.insomnia_text_inverse_preferences_bw.color = "#dcd168"
    style.insomnia_text_inverse_preferences_bw.hover_color = "#dcd168"
    style.insomnia_text_inverse_preferences_bw.selected_color = "#dcd168"

    style.insomnia_text_fog = Style(style.default)
    style.insomnia_text_fog.font = insomnia_flow_ext
    style.insomnia_text_fog.size = 60
    style.insomnia_text_fog.color = "#ffffff"
    style.insomnia_text_fog.hover_color = "#c2dded"
    style.insomnia_text_fog.selected_color = "#ffffff"
    style.insomnia_text_fog.selected_idle_color = "#ffffff"
    style.insomnia_text_fog.selected_hover_color = "#c2dded"
    style.insomnia_text_fog.insensitive_color = "#ffffff"

    style.insomnia_save_load_fog = Style(style.default)
    style.insomnia_save_load_fog.font = insomnia_flow_ext
    style.insomnia_save_load_fog.size = 60
    style.insomnia_save_load_fog.kerning = 3
    style.insomnia_save_load_fog.color = "#ffffff"
    style.insomnia_save_load_fog.hover_color = "#c2dded"
    style.insomnia_save_load_fog.selected_color = "#ffffff"
    style.insomnia_save_load_fog.selected_idle_color = "#ffffff"
    style.insomnia_save_load_fog.selected_hover_color = "#c2dded"
    style.insomnia_save_load_fog.insensitive_color = "#ffffff"

    style.insomnia_save_load_button_fog = Style(style.button)
    style.insomnia_save_load_button_fog.background = insomnia_gui_path + "save_load/fog/save_load_button_idle.png"
    style.insomnia_save_load_button_fog.hover_background = insomnia_gui_path + "save_load/fog/save_load_button_hover.png"
    style.insomnia_save_load_button_fog.selected_background = insomnia_gui_path + "save_load/fog/save_load_button_selected.png"
    style.insomnia_save_load_button_fog.selected_hover_background = insomnia_gui_path + "save_load/fog/save_load_button_selected.png"
    style.insomnia_save_load_button_fog.selected_idle_background = insomnia_gui_path + "save_load/fog/save_load_button_selected.png"

    style.insomnia_text_preferences_fog = Style(style.default)
    style.insomnia_text_preferences_fog.font = insomnia_flow_ext
    style.insomnia_text_preferences_fog.size = 60
    style.insomnia_text_preferences_fog.color = "#ffffff"
    style.insomnia_text_preferences_fog.hover_color = "#c2dded"
    style.insomnia_text_preferences_fog.selected_color = "#c2dded"

    style.insomnia_text_inverse_preferences_fog = Style(style.default)
    style.insomnia_text_inverse_preferences_fog.font = insomnia_flow_ext
    style.insomnia_text_inverse_preferences_fog.size = 60
    style.insomnia_text_inverse_preferences_fog.color = "#c2dded"
    style.insomnia_text_inverse_preferences_fog.hover_color = "#c2dded"
    style.insomnia_text_inverse_preferences_fog.selected_color = "#c2dded"