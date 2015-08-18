class SudokuPuzzle:
    def __init__(self, filePath):
        self.grid = [] 
        self.getGridFromFilePath(filePath)

    def getGridFromFilePath(self, filePath):
        with open(filePath) as f:
            self.grid = []
            for row in f:
                row = row.split()
                row = [int(i) for i in row]
                self.grid.append(row)

    def printGrid(self):
        print "-------------------------------------"
        for row in range(0,9):
            for column in range(0,9):
                number = self.grid[row][column]
                if number != 0:
                    print "|", number,
                else:
                    print "|  ",

            print "|"
            print "-------------------------------------"

a = SudokuPuzzle("testPuzzle.txt")
a.printGrid()
