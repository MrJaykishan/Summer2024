class A:
    def __init__(self):
        print("this is class A contructor")

class B(A):
    pass
    # def __init__(self):
    #     print("this is class B contructor")


class C(B):
    pass
    # def __init__(self):
    #     print("this is class C contructor")

ob=C()