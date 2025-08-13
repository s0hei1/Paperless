def dir_without_dunders(p_object=None):
    return [i for i in dir(p_object) if not i.startswith("__")]


def cls_callables(cls):
    return [attr for attr in dir_without_dunders(cls) if callable(getattr(cls, attr))]

def attr_reader(p_object : object ,only_annotations : bool = False):
    attrs = dir_without_dunders(p_object)
    for attr in attrs:
        if hasattr(p_object, attr):

            if only_annotations and attr not in p_object.__annotations__.keys():
                continue
            print(f"{type(p_object)}.{attr} = {getattr(p_object, attr)}")




