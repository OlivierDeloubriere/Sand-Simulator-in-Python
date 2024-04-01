import random

class World:
    def __init__(self, numberOfRows, numberOfColumns):
        self.numberOfRows = numberOfRows
        self.numberOfColumns = numberOfColumns
        self.grid = [[(0,0,0) for i in range(numberOfRows)] for j in range(numberOfColumns)]
        
    def update(self):
        newGrid = [[(0,0,0) for i in range(self.numberOfRows)] for j in range(self.numberOfColumns)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != (0,0,0):
                    if not self.__isOnGround(j):
                        if not self.__hasGrainBelow(j, i):
                            # move down
                            newGrid[i][j+1] = self.grid[i][j]
                        else:
                            couldSlideRight = not self.__hasGrainBelowRight(j, i)
                            couldSlideLeft = not self.__hasGrainBelowLeft(j, i)
                            if couldSlideLeft:
                                if couldSlideRight:
                                    # slide randomly between left and right
                                    if random.random() < 0.5:
                                        #slide left
                                        newGrid[i-1][j+1] = self.grid[i][j]
                                    else:
                                        #slide right
                                        newGrid[i+1][j+1] = self.grid[i][j]
                                else:
                                    #slide left
                                    newGrid[i-1][j+1] = self.grid[i][j]
                            else:
                                if couldSlideRight:
                                    #slide right
                                    newGrid[i+1][j+1] = self.grid[i][j]
                                else:
                                    # do not move
                                    newGrid[i][j] = self.grid[i][j]
                    else:
                        # do not move
                        newGrid[i][j] = self.grid[i][j]
        self.grid = newGrid
    
    def __hasGrainBelow(self, row, col):
        return self.grid[col][row+1] != (0,0,0)

    def __isOnGround(self, row):
        return row == self.numberOfRows - 1
    
    def __hasGrainBelowRight(self, row, col):
        if col < self.numberOfColumns - 1 and col >= 0:
            return self.grid[col+1][row+1] != (0,0,0)
        else:
            return True
    
    def __hasGrainBelowLeft(self, row, col):
        if col > 0 and col < self.numberOfColumns - 1:
            return self.grid[col-1][row+1] != (0,0,0)
        else:
            return True
        
    def addGrain(self, xposition, yposition, numberOfGrains, grainColor):
        if xposition >= 0 and xposition < self.numberOfColumns and yposition >= 0 and yposition < self.numberOfRows:
            for j in range(max(yposition - numberOfGrains // 2,0), min(yposition + numberOfGrains // 2, self.numberOfColumns)):
                self.grid[xposition][j] = grainColor