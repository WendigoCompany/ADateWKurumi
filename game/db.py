import renpy.exports as renpy

menu_db = {
    "start": {
        "en": "Start",
        "es": "Iniciar",
    },
    "back": {
        "en": "Back",
        "es": "Volver",
    },
    "history": {
        "en": "History",
        "es": "Historial",
    },
    "skip": {
        "en": "Skip",
        "es": "Saltar",
    },
    "auto": {
        "en": "Auto",
        "es": "Auto",
    },
    "save": {
        "en": "Save",
        "es": "Guardar",
    },
    "qsave": {
        "en": "Q.Save",
        "es": "Guardado Rap.",
    },
    "qload": {
        "en": "Q.Load",
        "es": "Carga Rap.",
    },
    "prefs": {
        "en": "Prefs",
        "es": "Prefs",
    },
    "start": {
        "en": "Start",
        "es": "Iniciar",
    },
    "load": {
        "en": "Load",
        "es": "Cargar",
    },
    "preferences": {
        "en": "Preferences",
        "es": "Preferencias",
    },
    "mainmenu": {
        "en": "Main Menu",
        "es": "Menu Principal",
    },
    "about": {
        "en": "About",
        "es": "Acerca",
    },
    "help": {
        "en": "Help",
        "es": "Ayuda",
    },
    "quit": {
        "en": "Quit",
        "es": "Cerrar",
    },
    "page": {
        "en": "Page",
        "es": "Página",
    },
    "automaticsaves": {
        "en": "Automatic Saves",
        "es": "Guardado Automático",
    },
    "quicksaves": {
        "en": "Quick Saves",
        "es": "Guardado Rápido",
    },
        "emptyslot": {
        "en": "Empty Slot",
        "es": "Slot Vacío",
    },
}






def get_txt_db(db, index):
    lang = renpy.game.preferences.language
    txt = "ERR"
    if db == "menu":
        txt = menu_db[index].get(lang)
    return txt
