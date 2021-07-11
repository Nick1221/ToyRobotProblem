from game.robot import Robot
 
class Game():
    def process_commands(self, commands):
        #Create a new robot for this game
        robot = Robot()
        for command in commands:      
            self.__play(robot, command)

    def __play(self, robot, command):
        #Reads the command and checks for valid commands only
        instruction = command.split()[0].strip()
        if instruction == "PLACE":
            x,y,face = command.split()[1].split(",")
            robot.place(x,y,face)

        #Checks if the robot has been PLACE before allowing any commands to run
        elif robot.get_x() is not None and robot.get_y() is not None and robot.get_face() is not None:
            if instruction == "MOVE":
                robot.move()
            elif instruction == "LEFT":
                robot.rotate_left()
            elif instruction == "RIGHT":
                robot.rotate_right()
            elif instruction == "REPORT":
                print (robot.report())
  