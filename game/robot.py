class Robot():
    #Constructor with boundary, direction
    def __init__(self, x=None, y=None, face=None):
        self._x = x
        self._y = y
        self._face = face
        self.board_boundary = 4
        self.directions = ["NORTH", "EAST", "SOUTH", "WEST"]
    
    #Getters
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def get_face(self):
        return self._face

    #Place based on params, return False if bound of boundary/Not a direction, else sets the position values and return True
    def place(self, x, y, face):
        x,y = int(x), int(y)
        if 0 <= x <= self.board_boundary and 0 <= y <= self.board_boundary and face in self.directions:
            self._x = x
            self._y = y
            self._face = self.directions.index(face)
            return True
        return False

    #Check face and position before moving, returns False if out of bounds, else moves pos and return True
    def move(self):
        if self._face == 0 and self._y < self.board_boundary:
            self._y += 1
            return True
        if self._face == 2 and self._y > 0:
            self._y -= 1
            return True
        if self._face == 1 and self._x < self.board_boundary:
            self._x += 1
            return True
        if self._face == 3 and self._x > 0:
            self._x -= 1
            return True
        return False
    
    #Rotates robot face left, returns False if uninitialised, else rotates face and return True
    def rotate_left(self):
        if self._face is None:
            return False
        self._face = (self._face - 1) % 4
        return True

    #Rotates robot face right, return False if uninitialised, else rotates face and return True
    def rotate_right(self):
        if self._face is None:
            return False
        self._face = (self._face + 1) % 4
        return True

    #Report current location and face direction, return "x,y,face"
    def report(self):
        return ("{},{},{}".format(self._x, self._y, self.directions[self._face]))
