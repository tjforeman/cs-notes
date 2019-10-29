# Dictionaries

# defining and creating dictionary 
d = {
    "foo": 12,
    "bar": 20
    }

def hello():
    print("Helloooo")

print(d["bar"])

# d["bar"] = 30

# print(d["bar"])

# d['hi'] = hello

# d["hi"]()


for k, v in d.items():
    print(f"key {k} has value {v}")