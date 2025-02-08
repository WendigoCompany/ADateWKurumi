import renpy.exports as renpy
from profiles import profiles
import inspect

cache = {

}


def see_module(module):
    for i in module.__dict__:
        print(i)

# def save_persisnt(gid):
#     if not renpy.persistent.girls_finished:
#         renpy.register_persistent("girls_finished", [])

def get_cache(key):
    try:
        return cache.get(key)
    except Exception as err:
        if "is not callable" in str(err):
            return None
        else:
            print("get_cache")
            print(err)
            return False


def set_cache(key, value):
    cache[key] = value
    # renpy.register_persistent(key, value)
    # renpy.save_persistent()

def save_end_route(gid):
    if not renpy.persistent.girls_finished:
        renpy.register_persistent("girls_finished", [])
    
    renpy.persistent.girls_finished.append(profiles[gid])

def disclaimed(action="r", newValue=False):
    if action == "r":
        print("--------------------------------")
        # renpy.game.persistent.pedro = 1
        try:
            return renpy.game.persistent.disclaimed
        except Exception as err:
            return False

    elif action == "w":
        renpy.game.persistent.disclaimed = newValue
        renpy.save_persistent()
        return renpy.game.persistent.disclaimed
        # return renpy.game.persistent.disclaimed


def get_lang():
    if not renpy.game.preferences.language:
        return "en"
    return renpy.game.preferences.language


def set_lang(lang):
    renpy.change_language(lang)
    # renpy.game.persistent.disclaimed = True
    disclaimed("w", True)
    renpy.save_persistent()
    renpy.reload_script()
    # renpy.game.persistent.disclaimed = False 

# def cargar_persistente():
#     # renpy.game.persistent.puta = "madre"
#     # renpy.save_persistent()
#     print(renpy.game.persistent.cache)
#     return ""

# AGREGA PERSISTENCIA DE DATOS 
def set_percache(key, value):
    if not renpy.game.persistent.cache:
        renpy.game.persistent.cache = {}
    cache_per = renpy.game.persistent.cache
    cache_per[key] = value
    renpy.game.persistent.cache = cache_per
    renpy.save_persistent()

def get_percache(key):
    if not renpy.game.persistent.cache:
        return None
    return renpy.game.persistent.cache.get(key)

# AGREGA PERSISTENCIA DE DATOS 


import os

def crear_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
        ruta_completa = os.path.abspath(nombre_archivo)
        print(f'Archivo "{nombre_archivo}" creado con éxito en {ruta_completa}.')
    except Exception as e:
        print(f'Error al crear el archivo: {e}')

# Ejemplo de uso


# # print("---------------------------------------------------------------------------")
# # see_module(renpy.store)
# # print("---------------------------------------------------------------------------")
# # see_module(renpy.store.store)
# # print("---------------------------------------------------------------------------")
# # # inspect.getsource(renpy.store.save_name)
# print(see_module(renpy.store.FileDelete))

# # print("---------------------------------------------------------------------------")

# print("---------------------------------------------------------------------------")
# print(inspect.getsource(renpy.save))
# print("---------------------------------------------------------------------------")
# print(inspect.getsource(renpy.load))
# # print("---------------------------------------------------------------------------")
# print(inspect.getsource(renpy))

# see_module(renpy.list_saved_games())

# print(renpy.config.developer)


