def outer():
    print("outer")
    def inner():
        print("inner")

    inner()
    inner()
    inner()

outer()
outer()