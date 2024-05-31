line = [1, 7, 6, 11, 3]

img = [[1, 7, 6, 11, 3],
                        [1, 7, 6, 11, 3],
                        [1, 7, 6, 11, 3],
                        [1, 7, 6, 11, 3],
                        [1, 7, 6, 11, 3]]

img = [line[:],
                        line[:],
                        line[:],
                        line[:],
                        line[:]]

print(img[0])
print(img[0][1])

img[1] = [0, 0, 0, 0, 0]
print(img)

img[1] = [0] * 5
print(img)

img[2][2:4] = [0, 0]
print(img)

img[1][:] = [1] * 5
print(img)

img.append([1, 2, 3, 4, 5])
print(img)

del img[-1]
print(img)

A = [[[True, False],
                [1, 2, 3]],
                ["matrix", "vector"]]

print(A[0][1])
print(A[1])
print(A[0][1][2])
