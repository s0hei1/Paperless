import os
from typing import AnyStr

def get_current_path_parent(path : AnyStr, depth = 1):
    if depth == 0:
        return path
    else:
        path = os.path.dirname(path)
        return get_current_path_parent(path = path ,depth = depth - 1)
