define aux = Character("Aux")

define w = Character("{color=#ff1010}Kurumi{/color}")

# "#3f87d3"
label kurutoki_intro:
    $ from KurumiTokisaki_db import call_kuru_toki_txt
    jump firts_intro


# POST GAME LLAMADA
label call_finished:
    "VOS YA ME TERMINASES"

#PRIMERA INTERACCION
label firts_intro:
    $ aux.name = "{color=#bbfff0}[call_kuru_toki_txt('aux_name', 0)]{/color}"
    stop music fadeout .5
    scene bg BLACK_SCREEN with dissolve
    $ renpy.pause(3)
    scene bg OFICINA_NORMAL with dissolve
    play music "music/loby.mp3" fadein 0.5 volume 0.75
    pl "[call_kuru_toki_txt('player_dialogs', 0)]"
    pl "..."
    pl "[call_kuru_toki_txt('player_dialogs', 1)]"
    pl "[call_kuru_toki_txt('player_dialogs', 2)]"
    scene bg BLACK_SCREEN with dissolve
    "[call_kuru_toki_txt('aux_dialogs', 0)]"
    pl ""
    pl "..."

