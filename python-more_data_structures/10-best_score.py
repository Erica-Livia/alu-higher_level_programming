#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        for key, val in a_dictionary.items():
            if val == max(a_dictionary.values()):
                return key
    else:
        return None
