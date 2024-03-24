class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]

        if og == color:
            return image

        def bfs(row,col):
            # print(row,col,og)
            if row<len(image) and col<len(image[0]) and row>=0 and col>=0 and image[row][col] == og:
                image[row][col] = color
                print(row,col)
            
                bfs(row+1,col)
                bfs(row-1,col)
                bfs(row,col+1)
                bfs(row,col-1)

        bfs(sr,sc)
        return image
