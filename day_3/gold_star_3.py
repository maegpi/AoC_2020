#maegpi
#day 3
#gold star
#2020-12-03

map = open('hillMap.txt', 'r').read().splitlines()

def sledding(map, over, down):
    
    trees = 0
    x = over
    y = down
    xlim = len(map[0])
    while y < len(map):
        if map[y][x%xlim] == "#":
            trees += 1
        y += down
        x += over
    return trees

if __name__ == '__main__':
    slope = [(3,1)]
    print("Part One:\n\nThe number of trees are: ",sledding(map,int(slope[0][0]),int(slope[0][1])),"\n")

    slope.insert(0,(1,1))
    slope.append((5,1))
    slope.append((7,1))
    slope.append((1,2))
    goldTrees = 1
    for i in range(len(slope)):
        goldTrees *= sledding(map,slope[0+i][0],slope[0+i][1])
    print("Part Two:\nThe number of golden star trees are: ",goldTrees)
