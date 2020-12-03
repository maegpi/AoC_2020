#maegpi
#day 2
#gold challenge
#2020-12-02

password = open('passwords.txt', 'r')

counter = 0

for line in password:
    limit, val, key = line.split(' ')
    llim,hlim = limit.split('-')
    val = val[0]
    if (key[int(llim)-1] == val) ^ (key[int(hlim)-1] == val):
        counter += 1

print("Number of approved passwords are: ", counter)
