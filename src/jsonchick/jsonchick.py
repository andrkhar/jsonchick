def find(element, JSON, path=None, all_paths=None, mutable=False):
    """Get paths to a value in JSON data.

    Usage: find(value, data)
    """
    all_paths = [] if all_paths is None else all_paths
    path = tuple() if path is None else path
    if isinstance(JSON, dict):
        for key, value in JSON.items():
            find(element, value, path + (key,), all_paths, mutable)
    elif isinstance(JSON, list):
        for index, value in enumerate(JSON):
            find(element, value, path + (index,), all_paths, mutable)
    else:
        if JSON == element:
            if mutable:
                path = list(path)
            all_paths.append(path)
    if not mutable:
        all_paths = tuple(all_paths)
    return all_paths 


def get_tuples(value, data):
    """Get paths to a value as a tuple of tuples."""
    return find(value,data)


def get_lists(value, data):
    """Get paths to a value as a list of lists."""
    return find(value, data, mutable=True)


def get_strings(value, data):
    """Get paths to a value as a list of strings."""
    paths = get_lists(value, data)
    strings = []
    for path in paths:
        string = ''.join([f'["{item}"]' if isinstance(item, str) else f'[{str(item)}]' for item in path])
        strings.append(string)
    return strings

