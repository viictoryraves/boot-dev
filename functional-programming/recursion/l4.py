def zipmap(keys, values):
    if not keys or not values:
        return {}
    zip = zipmap(keys[1:], values[1:])
    zip[keys[0]] = values[0]
    return zip
