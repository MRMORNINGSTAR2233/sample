def list_to_dictionary(keys,values):
    dictionary={}
    for i in range(len(keys)):
        if i < len(values):
            dictionary[keys[i]]=values[i]
        else:
            dictionary[i]=None
    return dictionary
keys=input()
values=input()
result_dict = list_to_dictionary(keys, values)
print("Resulting Dictionary:", result_dict)
