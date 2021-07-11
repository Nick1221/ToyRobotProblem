class Robot():
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

    #Place based on params, checks if they are valid
    def place(self, x, y, face):
        x,y = int(x), int(y)
        if 0 <= x <= self.board_boundary and 0 <= y <= self.board_boundary and face in self.directions:
            self._x = x
            self._y = y
            self._face = self.directions.index(face)
            return True
        return False

    #Check face and position before moving, returns False if out of bounds
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
    
    #Rotates robot face left, returns False if uninitliased
    def rotate_left(self):
        if self._face is None:
            return False
        self._face = (self._face - 1) % 4
        return True

    #Rotates robot face right, 
    def rotate_right(self):
        if self._face is None:
            return False
        self._face = (self._face + 1) % 4
        return True

    #Report current location and face direction, 
    def report(self):
        return ("{},{},{}".format(self._x, self._y, self.directions[self._face]))
