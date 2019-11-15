import bpy


def make_annotations(cls):
    """Converts class fields to annotations if running with Blender 2.8"""
    if bpy.app.version < (2, 80):
        return cls
    bl_props = {k: v for k, v in cls.__dict__.items() if isinstance(v, tuple)}
    if bl_props:
        if '__annotations__' not in cls.__dict__:
            setattr(cls, '__annotations__', {})
        annotations = cls.__dict__['__annotations__']
        for k, v in bl_props.items():
            annotations[k] = v
            delattr(cls, k)
    return cls


def get_user_preferences(context=None):
    """Multi version compatibility for getting addon keys"""
    if not context:
        context = bpy.context
    prefs = None
    if hasattr(context, "user_preferences"):
        prefs = context.user_preferences
    elif hasattr(context, "preferences"):
        prefs = context.preferences
    if prefs:
        return prefs
    else:
        raise Exception("Could not fetch user preferences")


def hide_viewport(object, state):
    """Multi version compatibility for setting the viewport hide state of an object"""
    if hasattr(object, "hide_viewport"):
        object.hide_viewport = state # where state is a boolean True or False
    else:
        object.hide = state


def set_active_object(context, obj):
    """Get the active object in a 2.7 and 2.8 compatible way"""
    if hasattr(context, "view_layer"):
        context.view_layer.objects.active = obj # the 2.8 way
    else:
        context.scene.objects.active = obj # the 2.7 way
    # note that `context.object` still works in 2.8 as a read-only way to get active objects


def select_get(object):
    """Multi version compatibility for getting object selection"""
    if hasattr(object, "select_get"):
    	return object.select_get()
    else:
        return object.select


def select_set(object, state):
    """Multi version compatibility for setting object selection"""
    if hasattr(object, "select_set"):
    	object.select_set(state)
    else:
        object.select = state
