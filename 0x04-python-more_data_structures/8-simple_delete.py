def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
