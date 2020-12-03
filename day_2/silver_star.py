#maegpi
#day 2
#silver challenge
#2020-12-02

password = open('passwords.txt', 'r')

counter = 0

for line in password:
    limit, val, key = line.split(' ')
    llim,hlim = limit.split('-')
    occur = key.count(val[0])
    if occur >= int(llim) and occur <= int(hlim):
        counter += 1

print("Number of approved passwords are: ", counter)
