#maegpi
#2020-12-01
#AoC Day 1, Part 1


getNums = open('day_1_nums.txt', 'r')
lst = []
FINAL_ANSWER = 2020

for line in getNums:
    lst.append(int(line))
print(lst)

num_bank_1 = {}
num_bank_2 = {}
counter_1 = 0
counter_2=0

for i in range(len(lst)):
    if lst[i] < FINAL_ANSWER/2:
        num_bank_1[counter_1] = lst[i]
        counter_1 += 1
    else:
        num_bank_2[counter_2] = lst[i]
        counter_2 += 1
print(num_bank_1)
print(num_bank_2)

check = False
while check is not True:
    for j in range(len(num_bank_2)):
        for k in range(len(num_bank_1)):
            if num_bank_1[k] + num_bank_2[j] == FINAL_ANSWER:
                winVal = [num_bank_1[k],num_bank_2[j]]
                check = True

print("The two values are: ", winVal,"\n the answer is: ",winVal[0]*winVal[1])
