define aux = Character("Aux")

label kurutoki_intro:
    jump firts_intro


# POST GAME LLAMADA
label call_finished:
    "VOS YA ME TERMINASES"

#PRIMERA INTERACCION
label firts_intro:
    $ aux.name = "{color=#bbfff0}aSS{/color}"
    stop music fadeout .5
    scene bg BLACK_SCREEN with dissolve
    $ renpy.pause(3)
    scene bg OFICINA_NORMAL with dissolve
    play music "music/loby.mp3" fadein 0.5 volume 0.75
    aux "FIN"