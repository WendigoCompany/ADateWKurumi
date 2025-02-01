# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# init python:
#     from db import get_txt_db

# # The game starts here.

# label start:
#     $ name = renpy.input(get_txt_db("omni",0))
#     if not name:
#         $ name = "Shido"
#     $ pl.name = name
    
    
#     # # Show a background. This uses a placeholder by default, but you can
#     # # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # # images directory to show it.

#     # scene bg room

#     # # This shows a character sprite. A placeholder is used, but you can
#     # # replace it by adding a file named "eileen happy.png" to the images
#     # # directory.

#     # show eileen happy

#     # # These display lines of dialogue.

#     # e "You've created a new Ren'Py game."

#     # e "Once you add a story, pictures, and music, you can release it to the world!"

#     # # This ends the game.

#     return


# Importa las funciones necesarias
init python:
    from functions import get_cache , set_cache ,see_module
    see_module(renpy.game)
    # def size_and_crop(im, width, height):
    #     # Calcula la proporción
    #     ratio = min(width / im.width, height / im.height)
    #     im = im.resize((int(im.width * ratio), int(im.height * ratio)), resample=Image.LANCZOS)
    #     # Recorta la imagen
    #     im = im.crop(((im.width - width) // 2, (im.height - height) // 2, (im.width + width) // 2, (im.height + height) // 2))
    #     return im

define get_cache_fun = get_cache
define set_cache_fun = set_cache 


# Define la pantalla del menú
screen opciones_menu(options):
    $ page = get_cache_fun("profiles_page")
    if not page:
        $ page = 0
        $ set_cache_fun("profiles_page", 0)
    else:
        $ page = int(page)
    vbox:
        for i, (img, txt) in enumerate(options):
            if i // 4 == page:
                button:
                    action Return(i)
                    hbox:
                        add im.Scale(img, 150, 150)  
                        text txt
                    style "button_default"
                    hover_background "#cccccc"
        button:
            action Return("a")
            hbox:
                text "Anterior"
        button:
            action Return("s")
            hbox:
                text "Siguiente"
        

define opciones = [
        ("opcion.jpg", "Texto de la opción 1"),
        ("opcion.jpg", "Texto de la opción 2"),
        ("opcion.jpg", "Texto de la opción 3"),
        ("opcion.jpg", "Texto de la opción 4"),
        ("opcion.jpg", "Texto de la opción 5"),
        ("opcion.jpg", "Texto de la opción 6"),
        ("opcion.jpg", "Texto de la opción 7"),
        ("opcion.jpg", "Texto de la opción 8"),
        ("opcion.jpg", "Texto de la opción 9"),
        ("opcion.jpg", "Texto de la opción 10"),
        ("opcion.jpg", "Texto de la opción 12"),
        ("opcion.jpg", "Texto de la opción 13"),
        ("opcion.jpg", "Texto de la opción 11"),
        ("opcion.jpg", "Texto de la opción 12"),
        ("opcion.jpg", "Texto de la opción 13"),
    ]


# Llama al menú de opciones
define opcion_seleccionada = ""
label start:
    $ opcion_seleccionada = renpy.call_screen("opciones_menu",opciones)
    if opcion_seleccionada == "s":
        $ set_cache_fun("profiles_page", get_cache_fun("profiles_page") + 1)
        jump start
        # $ opcion_seleccionada = renpy.call_screen("opciones_menu",opciones)
    if opcion_seleccionada == "a" :
        $ set_cache_fun("profiles_page", get_cache_fun("profiles_page") - 1)
        jump start
        # $ opcion_seleccionada = renpy.call_screen("opciones_menu",opciones)
    else:
        jump continuar
        
label continuar:
    "Has seleccionado la opción [opcion_seleccionada]"
