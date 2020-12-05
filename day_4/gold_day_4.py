#maegpi
#AoC Day 4
#2020-12-04
#Gold Challenge

passports = open('passports.bat', 'r').read().split('\n\n')

hairalpha = "abcdef0123456789"
charDict = {}
numDict = {}
for char in hairalpha:
    charDict[char] = True
for char in hairalpha[6:]:
    numDict[char] = True
eyeDict = {"amb":True,"blu":True,"brn":True,"gry":True,"grn":True,"hzl":True,"oth":True}


def checkPerson(person):

    byr = 0
    iyr = 0
    eyr = 0
    hgt = 0
    hcl = 0
    ecl = 0
    pid = 0
    
    person = person.replace("\n"," ")
    person = person.split(" ")

    for cell in person:
        if cell[0:3] == "byr":
            front,end = cell.split(":")
            if int(end) > 1919 and int(end) < 2003:
                byr = 1
        if cell[0:3] == "iyr":
            front,end = cell.split(":")
            if int(end) > 2009 and int(end) < 2021:
                iyr = 1
        if cell[0:3] == "eyr":
            front,end = cell.split(":")
            if int(end) > 2019 and int(end) < 2031:
                eyr = 1
        if cell[0:3] == "hgt":
            front,end = cell.split(":")
            if end[-2:] == "cm":
                if int(end[:-2]) > 149 and int(end[:-2]) < 194:
                    hgt = 1
            elif end[-2:] == "in":
                if int(end[:-2]) > 58 and int(end[:-2]) < 77:
                    hgt = 1
        if cell[0:3] == "hcl":
            front,end = cell.split(":")
            if len(end) == 7:
                check = True
                for char in end[5:]:
                    if char not in charDict:
                        check = False
                if check is True:
                    hcl = 1
        if cell[0:3] == "ecl":
            front,end = cell.split(":")
            if end in eyeDict:
                ecl = 1
        if cell[0:3] == "pid":
            front,end = cell.split(":")
            check = True
            counter = 0
            for char in end:
                if char not in numDict:
                    check = False
                counter += 1
            if check is True and counter == 9:
                pid = 1
                
    return byr+iyr+eyr+hgt+hcl+ecl+pid

if __name__ == "__main__":
    validPassport = 0

    for cell in passports:
        if checkPerson(cell) == 7:
            validPassport += 1
 
    print("The total number of passports is: ",len(passports),"\nThe number of valid passports are: ",validPassport)
