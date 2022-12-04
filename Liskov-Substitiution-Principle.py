class Bird:

    def swim(self):
        print("Bird is swimming")

    def fly(self):
        print("Bird is flying")


class Duck(Bird):
    pass


class Pinguin(Bird):
    def fly(self):
        print("Pinguin cannot fly")


# Modified Version



class FlyingBird:

    def fly(self):
        print("Bird is flying")


class SwimmingBird:

    def swim(self):
        print("Bird is swimming")



class Duck(FlyingBird, SwimmingBird):
    pass


class Pinguin(SwimmingBird):
    pass


    






