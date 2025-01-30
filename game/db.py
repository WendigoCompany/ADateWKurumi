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
    "display": {
        "en": "Display",
        "es": "Pantalla",
    },
    "window": {
        "en": "Window",
        "es": "Ventana",
    },
    "fullscreen": {
        "en": "Fullscreen",
        "es": "Pantalla Completa",
    },
    "unseentext": {
        "en": "Unseen Text",
        "es": "Texto no Visto",
    },
    "afterchoices": {
        "en": "After Choices",
        "es": "Despues de Elecciones",
    },
    "transitions": {
        "en": "Transitions",
        "es": "Transiciones",
    },
    "language": {
        "en": "Language",
        "es": "Idioma",
    },
    "en": {
        "en": "English",
        "es": "Inglés",
    },
    "es": {
        "en": "Spanish",
        "es": "Español",
    },
    "textspeed": {
        "en": "Text Speed",
        "es": "Velocidad Texto",
    },
    "autoforwardtime": {
        "en": "Auto-Forward Time",
        "es": "Tiempo Texto Auto",
    },
    "musicvolume": {
        "en": "Music Volume",
        "es": "Volumen Música",
    },
    "soundvolume": {
        "en": "Sound Volume",
        "es": "Volumen Sonido",
    },
    "voicevolume": {
        "en": "Voice Volume",
        "es": "Volumen Voz",
    },
    "muteall": {
        "en": "Mute All",
        "es": "Silenciar Todo",
    },
    "test": {
        "en": "Test",
        "es": "Probar",
    },
    "nohisto": {
        "en": "The dialogue history is empty.",
        "es": "El historial de dialogos esta vacío.",
    },
    "keyboard": {
        "en": "Keyboard",
        "es": "Teclado",
    },
    "mouse": {
        "en": "Mouse",
        "es": "Mouse",
    },
    "gamepad": {
        "en": "Gamepad",
        "es": "Mando",
    },
}

"""
{
        "en": "",
        "es": "",
    },


"""







def get_txt_db(db, index):
    lang = renpy.game.preferences.language
    txt = "ERR"
    if db == "menu":
        txt = menu_db[index].get(lang)
    return txt
