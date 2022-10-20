class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        elements = []
        for x in mat:
            for j in x:
                elements.append(j)
        ans = []
        index = 0
        
        try:
            for i in range(r):
                newarr = []
                for j in range(c):
                    newarr.append(elements[0])
                    elements.pop(0)
                ans.append(newarr)
                index += r
            print(elements)
            if(elements == []):
                return ans
            else:
                return mat
        except:
            return mat