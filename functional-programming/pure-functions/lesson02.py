def add_format(default_formats, new_format):
    formats = {
        **default_formats,
    }
    formats[new_format] = True
    return formats


def remove_format(default_formats, old_format):
    formats = {
        **default_formats,
    }
    formats[old_format] = False
    return formats
