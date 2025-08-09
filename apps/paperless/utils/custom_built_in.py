def dir_without_dunders(p_object=None):
    return [i for i in dir(p_object) if not i.startswith("__")]


def cls_callables(cls):
    return [attr for attr in dir_without_dunders(cls) if callable(getattr(cls, attr))]
