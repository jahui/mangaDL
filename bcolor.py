
class bcolor:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    end = '\033[0m'

    def test(self):
        print self.purple + "This color is purple" + self.end
        print self.blue + "This color is blue" + self.end
        print self.green + "This color is green" + self.end
        print self.red + "This color is red" + self.end
        print self.yellow + "This color is yellow" + self.end

def printPurple(printme):
    print bcolor.purple + printme + bcolor.end

def printRed(printme):
    print bcolor.red + printme + bcolor.end

def printGreen(printme):
    print bcolor.green + printme + bcolor.end

def printBlue(printme):
    print bcolor.blue + printme + bcolor.end

def printYellow(printme):
    print bcolor.yellow + printme + bcolor.end


def main():
    x = bcolor()
    x.test()

    print bcolor.red + "Error: Invalid nothing" + bcolor.end

if __name__ == '__main__':
    main()