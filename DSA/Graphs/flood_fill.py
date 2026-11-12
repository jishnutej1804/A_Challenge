def flood_fill(image, sr, sc, color):
    rows = len(image)
    cols = len(image[0])

    original_color = image[sr][sc]

    if original_color == color:
        return image

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if image[r][c] != original_color:
            return

        image[r][c] = color

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image

image1 = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

image2 = [
    [0, 0, 0],
    [0, 0, 0]
]

print(flood_fill(image1, 1, 1, 2))
print(flood_fill(image2, 0, 0, 0))