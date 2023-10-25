"""info = {}
info ["name"] = "Sandy"
info ["occupation"] = "hacker"
print (info)"""

"""mygrades = {90:'A', 80:'B', 70:'C'}
list (mygrades.items())
print (mygrades.items())

for (key, value) in mygrades.items():
    print (key, value)"""

"""my_info = {'name':'Sandy','occupation':'manager', 'age': '38'}
theKeys = list (my_info.keys ())
theKeys.sort ()
print (theKeys)

for key in theKeys:
    print (key, my_info [key])"""


dict1 = {1:1, 2:9, 3:4}
sorted_values = sorted(dict1.values())      #[1, 4, 9]
# print (sorted_values)
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():          #[1, 2, 3]
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break

