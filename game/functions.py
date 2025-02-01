import renpy.exports as renpy

cache = {

}


def see_module(module):
    for i in module.__dict__:
        print(i)


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
