try:
    import mscvrt

    def getkey():
        return mscvrt.getch()


except:
    import sys
    import tty
    import termios

    def getkey():
        fd =sys.stdin.fileno()
        original_attributs = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributs)
        return ch

