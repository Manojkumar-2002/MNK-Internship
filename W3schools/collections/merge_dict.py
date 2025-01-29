from collections import ChainMap


dict1 = {"hi":1,"jii":4}
dict2 = {"hii":1,"ji":4}

print(dict(ChainMap(dict1,dict2)))

print({**dict1,**dict2})