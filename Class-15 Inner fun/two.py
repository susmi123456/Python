def outer():
    print("inside outer function")
    def inner():
        print("inside inner function")

outer()
inner() #NameError: name 'inner' is not defined. Did you mean: 'iter'?