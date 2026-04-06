#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = None
    max_val = 0
    for key, value in a_dictionary.items():
        if max_key is None or value > max_val:
            max_val = value
            max_key = key
    return max_key
