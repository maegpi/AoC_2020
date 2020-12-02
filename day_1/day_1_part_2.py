#maegpi
#2020-12-01
#AoC Day 1, Part 2


getNums = open('day_1_nums.txt', 'r')
lst = []
FINAL_ANSWER = 2020

for line in getNums:
    lst.append(int(line))
print(lst,"\n")

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


check = False
while check is not True:
    for i in range(len(num_bank_1)):
        for j in range(len(num_bank_1)):
            for k in range(len(num_bank_1)):
                if num_bank_1[i] + num_bank_1[j] + num_bank_1[k] == FINAL_ANSWER:
                    winVal = [num_bank_1[i], num_bank_1[j], num_bank_1[k]]
                    check = True

print("The three values are: ",winVal,"\nAnd the answer is: ",winVal[0]*winVal[1]*winVal[2])
