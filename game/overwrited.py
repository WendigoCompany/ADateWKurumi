import renpy.exports as renpy
import copy
import inspect

old_save = copy.deepcopy(renpy.save)

def new_save(*args, **kwargs):
    print("DESDE EL NUEVITO")
    old_save(args[0], **kwargs)
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