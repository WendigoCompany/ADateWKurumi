init python:
    from functions import get_cache , set_cache , get_lang
    from db import get_txt_db
    from profiles import profiles

    def get_profile():
        return '/profiles/' + profile_selected[1].replace(" ","") +'_'+ get_lang_fun() + ".png"

# define opciones = [
#         ("opcion.jpg", "Texto de la opción 1"),
#         ("opcion.jpg", "Texto de la opción 2"),
#         ("opcion.jpg", "Texto de la opción 3"),
#         ("opcion.jpg", "Texto de la opción 4"),
#         ("opcion.jpg", "Texto de la opción 5"),
#         ("opcion.jpg", "Texto de la opción 6"),
#         ("opcion.jpg", "Texto de la opción 7"),
#         ("opcion.jpg", "Texto de la opción 8"),
#         ("opcion.jpg", "Texto de la opción 9"),
#         ("opcion.jpg", "Texto de la opción 10"),
#         ("opcion.jpg", "Texto de la opción 12"),
#         ("opcion.jpg", "Texto de la opción 13"),
#         ("opcion.jpg", "Texto de la opción 11"),
#         ("opcion.jpg", "Texto de la opción 12"),
#         ("opcion.jpg", "Texto de la opción 13"),
#     ]

define profile_selected = ""
define get_cache_fun = get_cache
define set_cache_fun = set_cache 
define max_per_page = 4
define get_lang_fun = get_lang
define get_txt_db_fun = get_txt_db



screen profiles_menu(options):
    $ page = get_cache_fun("profiles_page")
    if not page:
        $ page = 0
        $ set_cache_fun("profiles_page", 0)
    else:
        $ page = int(page)
    vbox:
        xalign 0.5
        for i, (img, txt) in enumerate(options):
            if i // 4 == page:
                button:
                    action Return(i)
                    hbox:
                        add im.Scale(img, 150, 150)  
                        text txt
                    hover_background "#cccccc"
        text ""
        button:
            xalign 0.5
            action Return("a")
            hbox:
                text get_txt_db_fun("menu", "next")
            hover_background "#cccccc"

        button:
            xalign 0.5
            action Return("s")
            hbox:
                text get_txt_db_fun("menu", "prev")
            hover_background "#cccccc"

label seleccionar_profile:
    $ profile_selected = renpy.call_screen("profiles_menu",profiles)
    if profile_selected == "s":
        if get_cache_fun("profiles_page")  < (len(profiles) // max_per_page ) :
            $ set_cache_fun("profiles_page", get_cache_fun("profiles_page") + 1)
        jump seleccionar_profile
        # $ profile_selected = renpy.call_screen("opciones_menu",opciones)
    if profile_selected == "a" :
        if get_cache_fun("profiles_page") > 0:
            $ set_cache_fun("profiles_page", get_cache_fun("profiles_page") - 1)
        jump seleccionar_profile

    else:
        # $ set_cache_fun("profiles_page", 0)
        $ profile_selected = profiles[profile_selected]
        
        jump profile_confirm

define pro_img = ""

label profile_confirm:
    image pro_img = "[get_profile()]"
    show pro_img at Position(xalign=0.5, yalign=0.5):
        size(750,1080)
    with dissolve
    pause
    menu:
        "[get_txt_db_fun('uscs', 'profile_menu', extra={'subindex': 1})]":
            hide pro_img with dissolve
            $ set_cache_fun("profiles_page", 0)
            $ set_cache_fun("profile_selected", profile_selected)
            jump game_nav
        "[get_txt_db_fun('uscs', 'profile_menu', extra={'subindex': 2})]":
            hide pro_img with dissolve
            jump start
            
    