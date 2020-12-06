#maegpi
#AoC Day 5
#2020-12-06
#Gold Challenge

seats = open('seats.txt','r').read().split("\n")
seats.remove(seats[-1])

TEST_VAL = "FBFBBFFRLR"

def binSeat(port):
    total = 0
    for ch in port:
        if ch == "F" or ch == "L":
            total += 0b1
        else:
            total += 0b0
    return total

def binSort(cell):
    rowTop = 127
    rowBot = 0
    row = ""
    colTop = 7
    colBot = 0
    column = ""

    for ch in cell[:6]:
        if ch == "F":
            rowTop = (rowTop + rowBot) // 2
        elif ch == "B":
            rowBot = (rowTop + rowBot) //2
            if rowBot % 2 == 1:
                rowBot += 1
        print("row ",rowBot," to ",rowTop," char ",ch)
    for ch in cell[7:-1]:
        if ch == "L":
            colTop = (colTop + colBot) //2
        elif ch == "R":
            colBot = (colTop + colBot) // 2
            if colBot % 2 == 1:
                colBot += 1
        print("column ",colBot," to ",rowTop," char ",ch)
    if cell[6] == "F":
        row = rowBot
    else:
        row = rowTop
    if cell[-1] == "L":
        column = colBot
    else:
        column = colTop
    return row,column
        
    
if __name__ == "__main__":
    highestSeat = 0
    highCell = None
    thisSeat = 0
    seatCollection = []
    seatHold = 0
    check = False
    i = 1
    
    for cell in seats:
        row,column = binSort(cell)
        seatID = row * 8 + column
        seatCollection.append(seatID)
        if seatID > highestSeat:
            highestSeat = seatID
            highCell = cell
    seatCollection.sort()
    j = len(seatCollection)
    print(seatCollection)
    while check is False or i != j:
        if seatCollection[i] - seatCollection[i-1] != 1:
            seatHold = seatCollection[i] -1
            check = True
        i += 1
        
    print("The highest seat ID is: ", highestSeat," in cell: ",highCell)
    print("The missing seat ID is: ", seatHold)
