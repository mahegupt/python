x = 1


def outer_fun():
    x = 20

    def inner_fun():
        global x
        x += 10
        print(x)
    inner_fun()


outer_fun()
