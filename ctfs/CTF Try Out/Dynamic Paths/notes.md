
    melty@ubuntu-slimdragon:~/Git/hackthebox/ctfs/CTF Try Out/Dynamic Paths$ nc 94.237.60.161 42989
    You will be given a number of t = 100 grids for the different regions you need to pass. For every map you will have the below values:
        1. The dimensions i x j of the map grid where 2 <= i, j <= 100
        2. The numbers n_i,j symbolizing the distances between the blocks where 1 <= n_i,j <= 50
    You will start at the top left element, and your goal is to reach the bottom right, while only being allowed to move down or right, minimizing the sum of the numbers you pass. Provide the minimum sum.

    Example Question:
        4 3
        2 5 1 9 2 3 9 1 3 11 7 4

    This generates the following grid:
        2 5 1
        9 2 3
        9 1 3
        11 7 4

    Example Response:
        17
    (Optimal route is 2 -> 5 -> 2 -> 1 -> 3 -> 4)

    Test 1/100
    4 4
    9 8 7 8 8 9 7 3 8 7 9 2 6 3 3 7
