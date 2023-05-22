with open("z.txt", "r") as archive:
    for lines in archive:
        print(lines.upper())