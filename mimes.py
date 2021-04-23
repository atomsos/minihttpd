




import json


mime = json.load(open('mimes.json'))
maxlength = 0
for key, val in mime.items():
    data = [key] + val
    data = ['"' + _ + '"' for _ in data]
    if len(data) > maxlength:
        maxlength = len(data)
print("#ifndef __MIMES_H__")
print("#define __MIMES_H__")
print("#define MIMES_LENGTH " + str(len(mime)))
print("#define MIMES_MAXLENGH " + str(maxlength))
print("char mimes[MIMES_LENGTH][MIMES_MAXLENGH][50] = {", end="")

for key, val in mime.items():
    data = [key] + val
    data = ['"' + _ + '"' for _ in data]
    if len(data) > maxlength:
        maxlength = len(data)
    print("{" + ",".join(data), "}", end=",")
print("}")
print("#endif")
