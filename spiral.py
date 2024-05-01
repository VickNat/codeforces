class Solution:
    def spiralOrder(self, matrix):
        colSize = len(matrix[0])
        rowSize = len(matrix)
        rStart = 0
        cStart = 0
        answer = []
        
        while rowSize >= 0 or colSize > 0: 
            if rStart != 0:           
              for right in range(cStart, colSize + 1):
                answer.append(matrix[rStart][right])
            else:
              for right in range(cStart, colSize):
                answer.append(matrix[rStart][right])
                
      
             
            for down in range(rStart+1, rowSize):
                answer.append(matrix[down][colSize-1])
               
            for left in range(colSize-2, cStart - 1, -1):
                  answer.append(matrix[rowSize-1][left])
            
            for up in range(rowSize-2, rStart, -1):
                  answer.append(matrix[up][cStart])

            
            colSize -= 2
            rowSize -= 2
            rStart += 1
            cStart += 1
        
        return answer


s = Solution()
s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])