name="mississippi"
d={}
for ch in name:
    if (ch in d):
        d[ch]=d[ch]+1
    else :
        d[ch]=1
for key in d:
    print(f"{key}-{d[key]}")
    

