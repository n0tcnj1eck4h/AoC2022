with open("input.txt", "r") as input:
    cals: list[int] = [0]
    for line in input:
        if line == "\n":
            cals.append(0)
            continue
        cals[len(cals) - 1] = cals[len(cals) - 1] + int(line.strip())
        
    cals.sort(reverse=True)
    print(cals[0])
    print(cals[0] + cals[1] + cals[2])
