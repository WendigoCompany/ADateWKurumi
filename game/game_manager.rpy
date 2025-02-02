init python:
    from functions import get_cache , set_cache , get_lang
    from db import get_txt_db
    from profiles import profiles

label game_nav:
    if get_cache('profile_selected')[1] == "Kurumi Tokisaki":
        jump kurutoki_intro
    # elif get_cache('profile_selected')[1] == "Naomi Yamato":
    #     jump naoyama_intro