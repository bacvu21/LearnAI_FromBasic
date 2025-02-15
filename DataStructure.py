# number = [1,2,3,4]  # list syntax

# ###tubles 

# colors = (1,2,3,4)
# singles_Tubles = ("hello",)
# print(singles_Tubles);

#dictionary

# dic = {"name":"bac", "age":10}

# print(dic["name"])

# del dic["name"]


##sets

# set1 = {1,2,3,4}
# set2 = {2,3,4,5}
# print(set1 - set2)

g_dic = {"Toi": "toi", "la": "la", "bac": "bac"}


def finding_keydata(key, val):
    for key_, val_ in g_dic.items(): 
        if key_ == key or val_ == val: 
            print(f"Found { val_ }")
        else:
            print("Not Found!") 
            

finding_keydata("toi", "bac")



