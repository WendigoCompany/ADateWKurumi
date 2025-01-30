init -3 python:
    from functions import disclaimed
    # from functions import disclaimed
    # disclaimedval = disclaimed("r")
    disclaimed_bool_py = disclaimed()
    disclaimed_func_py = disclaimed
    if renpy.game.preferences.language is None:
        renpy.game.preferences.language = "en"
        renpy.save_persistent()
    lang_py = renpy.game.preferences.language
    
define lang = lang_py
define disclaimed_bool = disclaimed_bool_py
define disclaimed_func = disclaimed_func_py

label en_disclaim:
    $ renpy.pause(2)
    show text "This game contains explicit material.\n\n All scenes depicted in the game are fictional and should not be reproduced in real life. \n It should only be played by persons over 18 years of age. \n\n All characters depicted in this work are fictitious and are at least 18 years old. \n\n Any resemblance to names, situations, etc. is purely coincidental. \n\n This game contains third party content. \n\n This work is not intended to promote or facilitate piracy or plagiarism. \n\n This is a work created solely for adult entertainment. All rights belong to and remain with their respective creators. \n\n I hope you enjoy it. \n":
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(30)
    return

label es_disclaim:
    $ renpy.pause(2)
    show text "Este juego contiene material explicito.\n\n  Todas las escenas aquí mostradas son ficticias y no deben ser replicadas en la vida real. \n El mismo solo debería ser jugado por personas con una edad de 18 o mas años. \n\n Todos los personajes representados en esta obra son ficticios y tienen al menos 18 años. \n\n Cualquier parecido con nombres, situaciones, etc. es pura coincidencia. \n\n Este juego contiene contenido de terceros. \n\n Esta obra no pretende promover ni facilitar la piratería o el plagio del mismo. \n\n Se trata de una obra creada exclusivamente para el entretenimiento de adultos. Todos los derechos pertenecen y permanecerán en poder de sus respectivos creadores. \n\n Espero que disfrutes de ella... \n":
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(30)
    return


label splashscreen:
    if not disclaimed_bool:
        if lang == "en":
            jump en_disclaim
        elif lang == "es":
            jump es_disclaim
    $ disclaimed_func("w", False)
    # if not disclaimed:
    #     if lang == "en":
    #         jump en_splash
    #     elif lang == "es":
    #         jump es_splash
        
    #     $ renpy.pause(3.0)
    # $ disclaimedFunc("w", False)
    return



