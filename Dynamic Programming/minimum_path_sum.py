class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mem = [[-1 for i in range(len(grid[0]))]for j in range(len(grid))] 

        def minSumSol (x,y):
            if (x == len(grid)-1 and y == len(grid[0])-1):
                # print('\n',"yes",x,y,len(grid)-1,len(grid[0])-1)
                return grid[x][y]

            if (mem[x][y] != -1):
                return mem[x][y]

            rightMove = 100000 
            downMove = 100000
            if(x<len(grid) and y+1<len(grid[0])):
                rightMove = grid[x][y] + minSumSol(x,y+1)
            
            if(x+1<len(grid) and y<len(grid[0])):
                downMove = grid[x][y] + minSumSol(x+1,y)
            
            mem[x][y] = min(rightMove,downMove)

            return min(rightMove,downMove)

        return minSumSol(0,0)