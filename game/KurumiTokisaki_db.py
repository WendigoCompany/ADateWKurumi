from patch_essencials import get_txt_patchDB

db_aux_name = [
    {
        "en": "Assistant",
        "es": "Asistente",
    }
]

db_aux_dialogs = [
    {
        "en": "[A couple of days later.]",
        "es": "[Un par de días después.]",
    },
]


db_player_dialogs = [
    {
        "en": "Well... Kurumi Tokisaki, let's see your profile.",
        "es": "Bien... Kurumi Tokisaki, veamos tu perfil. ",
    },
    {
        "en": "(Not bad. Pretty, good measurements and willing.)",
        "es": "(Nada mal. Bonita, buenas medidas  y dispuesta.)",
    },
    {
        "en": "(I'll send her an email to arrange.)",
        "es": "(Voy a enviarle un correo para acordar.)",
    },
]


kurumi_db_dialogs = []

kuru_toki_data = {
    "aux_name": db_aux_name,
    "aux_dialogs": db_aux_dialogs,
    "player_dialogs": db_player_dialogs,
    "kurumi_dialogs": kurumi_db_dialogs,
}


def call_kuru_toki_txt(key, index, extra={}):
   return get_txt_patchDB(kuru_toki_data[key], index, extra)


#  {
#      "en": "Assistant",
#      "es": "Asistente",
#  } ,
