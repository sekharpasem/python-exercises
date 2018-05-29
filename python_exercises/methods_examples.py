class Person():
    def hello(self, name):
        self.name = name
        print("Hello {} How are you ?".format(self.name))

    def bye(self, name):
        self.name = name
        print("Nice Meeting You {}".format(self.name))


jackman = Person()
jackman.hello("Lee")
jackman.bye("Edison")