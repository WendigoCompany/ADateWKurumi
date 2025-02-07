define aux = Character("Aux")

define w = Character("{color=#ff1010}Kurumi{/color}")

# "#3f87d3"
label kurutoki_intro:
    $ from KurumiTokisaki_db import db_aux_kurumitokisaki_name, db_aux_kurumitokisaki_dialogs, db_player_kurumitokisaki_dialogs , db_kurumitokisaki_dialogs
    $ from patch_essencials import get_txt_patchDB
    jump firts_intro


# POST GAME LLAMADA
label call_finished:
    "VOS YA ME TERMINASES"

#PRIMERA INTERACCION
label firts_intro:
    $ aux.name = "{color=#bbfff0}[get_txt_patchDB(db_aux_kurumitokisaki_name, 0)]{/color}"
    stop music fadeout .5
    scene bg BLACK_SCREEN with dissolve
    $ renpy.pause(3)
    scene bg OFICINA_NORMAL with dissolve
    play music "music/loby.mp3" fadein 0.5 volume 0.75
    pl "[get_txt_patchDB(db_player_kurumitokisaki_dialogs, 0)]"
    pl "..."
    pl "[get_txt_patchDB(db_player_kurumitokisaki_dialogs, 1)]"
    pl "[get_txt_patchDB(db_player_kurumitokisaki_dialogs, 2)]"
    scene bg BLACK_SCREEN with dissolve
    "[get_txt_patchDB(db_aux_kurumitokisaki_dialogs, 1)]"
    pl ""
    pl "..."
