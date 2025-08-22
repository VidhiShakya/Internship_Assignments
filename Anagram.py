def anagram(list_object):
    dict = {}
    for i in list_object:
        key_string=''
        key = key_string + str((sorted(i)))
        if key in dict:
            dict[key].append(i)
        else:
            dict[key] = [i]
    return list(dict.values())
    

list_object = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(anagram(list_object))