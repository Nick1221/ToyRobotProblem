from game.robot import Robot
import unittest

class TestBoardmethods(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()

    def test_robot_initialised(self):
        # Check if robot is initialised
        self.assertFalse(self.robot._x)
        self.assertFalse(self.robot._y)
        self.assertFalse(self.robot._face)

    def test_robot_ignore_until_placed(self):
        # All movement and rotation should fail before PLACE
        self.assertFalse(self.robot.move())
        self.assertFalse(self.robot.rotate_left())
        self.assertFalse(self.robot.rotate_right())

    def test_robot_placed(self):
        #Check functionality of robot after place should all work
        self.robot.place(0,0,"NORTH")
        self.assertTrue(self.robot.move())
        self.assertTrue(self.robot.rotate_left())
        self.assertTrue(self.robot.rotate_right())
    
    def test_robot_falling(self):
        #Test for movement beyond the corners
        #ensure it doesn't move and continues
        #Rotations should persist
        self.robot.place(4,4,"NORTH")
        self.assertFalse(self.robot.move())
        self.assertEqual(self.robot.report(), "4,4,NORTH")
        self.robot.rotate_right()
        self.assertFalse(self.robot.move())
        self.assertEqual(self.robot.report(), "4,4,EAST")

        self.robot.place(0,4,"NORTH")
        self.assertFalse(self.robot.move())
        self.assertEqual(self.robot.report(), "0,4,NORTH")
        self.robot.rotate_left()
        self.assertFalse(self.robot.move())
        self.assertEqual(self.robot.report(), "0,4,WEST")

        self.robot.place(0,0,"SOUTH")
        self.assertFalse(self.robot.move())
        self.assertEqual(self.robot.report(), "0,0,SOUTH")
        self.robot.rotate_right()
        self.assertFalse(self.robot.move())
        self.assertEqual(self.robot.report(), "0,0,WEST")

        self.robot.place(4,0,"SOUTH")
        self.assertFalse(self.robot.move())
        self.assertEqual(self.robot.report(), "4,0,SOUTH")
        self.robot.rotate_left()
        self.assertFalse(self.robot.move())
        self.assertEqual(self.robot.report(), "4,0,EAST")

    
if __name__ == '__main__':
    unittest.main()
    