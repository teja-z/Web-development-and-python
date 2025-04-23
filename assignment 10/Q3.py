def magic_square_odd(n):
    square = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2

    while num <= n ** 2:
        square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    return square

def magic_square_doubly_even(n):
    square = [[(n*y) + x + 1 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i + j) % 4 == 3):
                square[i][j] = n * n + 1 - square[i][j]
    return square

def magic_square_singly_even(n):
    half = n // 2
    sub_square = magic_square_odd(half)
    square = [[0] * n for _ in range(n)]

    add = [0, 2 * half * half, 3 * half * half, half * half]

    for i in range(half):
        for j in range(half):
            square[i][j] = sub_square[i][j] + add[0]
            square[i][j + half] = sub_square[i][j] + add[1]
            square[i + half][j + half] = sub_square[i][j] + add[2]
            square[i + half][j] = sub_square[i][j] + add[3]

    k = (n - 2) // 4
    for i in range(n):
        for j in range(n):
            if (i < half and j < k) or (i < half and j >= n - k and j < n):
                if j != k or i != k:
                    square[i][j], square[i + half][j] = square[i + half][j], square[i][j]
    return square

def generate_magic_square(n):
    if n % 2 == 1:
        return magic_square_odd(n)
    elif n % 4 == 0:
        return magic_square_doubly_even(n)
    else:
        return magic_square_singly_even(n)

def print_square(square):
    n = len(square)
    for row in square:
        print(" ".join(f"{num:3}" for num in row))
    print(f"Magic Constant: {n * (n**2 + 1) // 2}\n")

# Generate magic squares for N = 4 to 8
for n in range(4, 9):
    print(f"\nMagic Square for N = {n}")
    square = generate_magic_square(n)
    print_square(square)
