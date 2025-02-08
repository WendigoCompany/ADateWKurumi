import renpy.exports as renpy
import copy
import inspect
import os
import json

profile_data = {"player_name": ""}

base = os.path.dirname(os.path.abspath(__file__)) + "/userman/"


############################################################################################################

old_save = copy.deepcopy(renpy.save)


def new_save(*args, **kwargs):
    old_save(args[0], **kwargs)
    regis_save_entry(args[0])
    return ""


renpy.save = new_save


############################################################################################################

old_load = copy.deepcopy(renpy.load)


def new_load(*args, **kwargs):
    old_load(args[0])
    return ""


# print(inspect.getsource(old_load))


renpy.load = new_load

############################################################################################################


old_unlink_save = copy.deepcopy(renpy.unlink_save)


def new_unlink_save(*args, **kwargs):
    print("ananna")
    print(args)
    print(kwargs)
    return ""


renpy.unlink_save = new_unlink_save

############################################################################################################


def regis_save_entry(file):
    saves = renpy.list_saved_games()
    dtt = None
    for save in saves:
        if save[0] == file:
            dtt = save[3]
    userdict = get_userdict()
    index = len(userdict) + 1
    found = False
    # for prof in userdict:
    #     for hints in 
    # userdict.append({"profile": f"profile-{index}", hints : [{dtt , slot}]})


def save_userdict(data):
    try:
        with open(base + "/user_manifiest.json", "w") as file:
            json.dump(data, file)
            return True
    except Exception as err:
        print("Error loading User Dict")
        print(err)
        return False


def get_userdict():
    userdict = []
    exist = False
    try:
        with open(base + "/user_manifiest.json", "r") as file:
            userdict = json.load(file)
            exist = True
    except Exception as err:
        if not "No such file or directory" in str(err):
            print("Error loading User Dict")
            print(err)
            renpy.quit()

    return userdict, exist


def read_userdict():
    userdict, exist = get_userdict()
    if len(userdict) > 0:
        pass
    else:
        # PRIMERA INTERACCION
        if not exist:
            save_userdict([])

    # profile_data = userdata

    # for k in userdict.keys():
    #     print(k)

    # files = os.listdir(base)
    pass


os.makedirs(base, exist_ok=True)
os.makedirs(base + "/profiles/", exist_ok=True)
read_userdict()


# ('1-1', '', <renpy.display.im.ZipFileImage object at 0x00000000052072e0>, 1739029663.2764454)
