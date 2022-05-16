def namelist(names):
    str = ""
    if len(names) == 1:
        return names[0].get("name")
    for index in range(0, len(names)):
        if index == len(names) - 1:
            str = str[:-2]
            str += " & " + names[index].get("name")
        else:
            str += names[index].get("name") + ", "

    return str


def namelisttwo(names):
    return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ", 1)[::-1]


def namelistthree(names):

    names = [hash["name"] for hash in names]
    output = names[:-2]
    output.append(" & ".join(names[-2:]))
    return ", ".join(output)


print(namelist([{"name": "Bart"}, {"name": "Lisa"}, {"name": "Maggie"}]))
