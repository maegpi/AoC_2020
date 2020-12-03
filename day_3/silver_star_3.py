#maegpi
#day 3
#silver star
#2020-12-03

map = open('hillMap.txt', 'r').read().splitlines()

def sledding(map, over, down):
    line = 1
    trees = 0
    x = over
    y = down
    lim = len(map[0])
    while line < len(map):
        if map[y][x%lim] == "#":
            trees += 1
        y += down
        x += over
        line += 1
    return trees

if __name__ == '__main__':
    slope = "31"
    print("The number of trees are: ",sledding(map,int(slope[0]),int(slope[1])))
