import renpy.exports as renpy


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


def set_lang(lang):
    renpy.change_language(lang)
    # renpy.game.persistent.disclaimed = True
    disclaimed("w", True)
    renpy.save_persistent()
    renpy.reload_script()
    # renpy.game.persistent.disclaimed = False