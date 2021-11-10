"""Merge two dictionaries."""
dict_1={"a":26,"c":56,"d":34}
dict_2={23:"anjaly",35:"manu",40:"ganga",23:"mahi"}
print(dict_1)
print(dict_2)
dict_1.update(dict_2)
print("After merging both dictionaries",dict_1)