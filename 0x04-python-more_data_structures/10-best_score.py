def best_score(a_dictionary):
    max_num = 0
    if a_dictionary is None:
        return None
    new_dict = a_dictionary.copy()
    new_list = list(new_dict.keys())
    for k in new_list:
        if new_dict[k] > max_num:
            max_num = new_dict[k]
    for k, v in new_dict.items():
        if v == max_num:
            return k
