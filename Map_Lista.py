items = [1, 4, True, None]

def stringify(items):
    return map(items, lambda x: str(x))



map([1, 4, True, None], stringify)