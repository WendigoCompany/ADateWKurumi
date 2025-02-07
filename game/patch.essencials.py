import renpy.exports as renpy

def get_txt_patchDB(db, index, extra={}):
    lang = renpy.game.preferences.language
    txt = "ERR"
    if type(db) is tuple or type(db) is list:
        if extra.get("subindex"):
            txt = db[index][extra["subindex"]][lang]
        else:
            txt = db[index][lang]
    elif type(db) is dict:
        if extra.get("subindex"):
            txt = db[index][extra["subindex"]][lang]
        else:
            txt = db[index][lang]
    return txt