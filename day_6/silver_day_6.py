#maegpi
#2020-12-06
#AoC Day 6
#Silver Challenge

cdf = open('cdf.txt','r').read().split("\n\n")


groupedCDF = []
yesCh = 0

for cell in cdf:
    groupedCDF.append(cell.split("\n"))
    
for array in groupedCDF:
    groupCheck = {}
    for cell in array:
        for ch in cell:
            groupCheck[ch] = True
    yesCh += len(groupCheck)
    
print(yesCh)
