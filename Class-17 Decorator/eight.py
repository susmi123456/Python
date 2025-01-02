def logion_req(func):

    def inner(name,status):
        if status == False:
            print("Login Req")
        else:
            func(name,status)

    return inner

@logion_req
def profile_page(name,status):
    print("profile page")

profile_page("Rahul",False)