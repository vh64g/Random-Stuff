
def modify_str(s):
    if len(s) < 3: return s
    elif s[-3:] == "ing": return f"{s}ly"
    else: return f"{s}ing"

def invert_dict(d):
    nd = {}
    for key, value in d.items():
        if nd.keys().__contains__(value): nd[value].append(key)
        else: nd.update({value: [key]})
    return nd

if __name__ == "__main__":
    print(invert_dict({'Physics': 67, 'Maths': 87, 'Practical': 48, "Job": 48}))