init python:
    from functions import get_cache , set_cache , get_lang
    from db import profiles,get_txt_db

label game_nav:
    if get_cache('profile_selected')[1] == "Kurumi Tokisaki":
        jump kurutoki_intro