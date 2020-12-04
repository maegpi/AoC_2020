#maegpi
#AoC Day 4
#2020-12-04
#Silver Challenge

passports = open('passports.bat', 'r').read().split('\n\n')

def checkPerson(person):
    byr = 0
    iyr = 0
    eyr = 0
    hgt = 0
    hcl = 0
    ecl = 0
    pid = 0
    
    tempStr = ""
    person = person.replace("\n"," ")
    person = person.split(":")
    for cell in person:
        tempStr += cell
    person = tempStr.split(" ")
    for cell in person:
        if cell[0:3] == "byr":
            byr = 1
        if cell[0:3] == "iyr":
            iyr = 1
        if cell[0:3] == "eyr":
            eyr = 1
        if cell[0:3] == "hgt":
            hgt = 1
        if cell[0:3] == "hcl":
            hcl = 1
        if cell[0:3] == "ecl":
            ecl = 1
        if cell[0:3] == "pid":
            pid = 1
            
    return byr+iyr+eyr+hgt+hcl+ecl+pid

if __name__ == "__main__":
    validPassport = 0
    for cell in passports:
        if checkPerson(cell) == 7:
            validPassport += 1

    print("The total number of passports is: ",len(passports),"\nThe number of valid passports are: ",validPassport)
