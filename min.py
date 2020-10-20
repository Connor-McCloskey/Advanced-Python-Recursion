def mult(x, y, x_original):
    print("X:", x)
    print("Y:", y)
    if x == 0 or y == 0:
        return 0
    if y == 1:
        return x
    else:
        x += x_original
        y -= 1
        if y == 0:
            return
        else:
            return mult(x, y, x_original)
    # return x

product = mult(5, 25, 5)
print(product)