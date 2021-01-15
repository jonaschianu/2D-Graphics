################################################################################
 # Project:       2D Graphical Outputs using Matrices                         #
 #                                                                            #
 # Name:          Jonas Chianu                                                #
 # File:          Graphics2d.py                                               #
 # Purpose:       Contains the graphical interface classes.                   #
 # Description:   Creates shapes and drawings given required parameters.      #
################################################################################

import math # Importing math module to access mathematical functions
import turtle # Importing turtle module
import main # Importing main.py file

class Drawing():
    ''' This class creates drawings from list of shapes '''
    def __init__(self, shape_array):
        ''' Initializes drawing with a list of shapes to be included 
            (Constructor)
            Passed: List of shapes (List)
            Returns: None
        '''
        self.__shapes=shape_array                                           # 4c
        self.bgcolor = "white"                                              # 4a


    def add_bg_color(self,bgcolor="white"):                                 # 4b
        ''' Adds a background color to drawing
            Passed: Background color (str)
            Returns: None
        '''
        self.bgcolor=bgcolor

    def display_drawing(self):
        ''' Creates and displays the drawing
            Passed: None
            Returns: None
        '''
        for shape in self.__shapes:                                         # 4d
            turtle.bgcolor(self.bgcolor)
            shape.draw_shape()

        turtle.exitonclick()

        try:
            turtle.bye()

        except Exception:
            pass

    def add_border(self,border_color,margin_dimensions):
        ''' Creates and displays the drawing
            Passed: Border color (str), Margin dimensions (list)
            Returns: None
        '''
        pass

class Shape():
    ''' This class creates a shape given corner coordinates '''
    def __init__(self, complex_array):
        ''' Initializes shape a list of corner coordinates (Constructor)
            Passed: List of corner coordinates (Matrix)
            Returns: None
        '''
        self._array=complex_array.get_matrix()[0]
        self.points_array()
        self._line_color = "black"
        self._fill_color = ""

    def rotate_shape(self,rotation):
        ''' Rotates the shape
            Passed: Rotation angle (number)
            Returns: None
        '''
        x = math.cos(rotation *(math.pi/180))
        y = math.sin(rotation*(math.pi/180))

        for i in range(len(self._array)):
            self._array[i]*=main.ComplexNumber(x, y)

        self.points_array()

    def move_shape(self,x,y):
        ''' Moves the shape
            Passed: Horizontal translation (number),
                    Vertical translation (number)
            Returns: None
        '''
        for i in range(len(self._array)):
            self._array[i]+=main.ComplexNumber(x, y)

        self.points_array()

    def shape_size(self,ratio):
        ''' Changes the relative size of shape
            Passed: Scaling ratio (number)
            Returns: None
        '''
        for i in range(len(self._array)):
            self._array[i]*=main.ComplexNumber(ratio, 0)

        self.points_array()

    def points_array(self):
        ''' Changes the matrix with complex numbers coordinates
            to a list of tuples coordinates
            Passed: None
            Returns: None
        '''
        self._points=[]

        for complex_num in self._array:
            self._points.append(complex_num.get_complex_Number())

        self._points.append(self._array[0].get_complex_Number())

    def color(self,line_color = "black",fill_color=""):
        ''' Assigns a color to the shape
            Passed: Color of shape's border (str), Color of shape (str)
            Returns: None
        '''
        self._line_color = line_color
        self._fill_color = fill_color

class Shape_linear(Shape):
    ''' This class creates a shape drawn using straight lines '''
    def draw_shape(self):
        ''' Draws and displays the shape
            Passed: None
            Returns: None
        '''
        turtle.penup()
        turtle.goto(self._points[0])
        turtle.pendown()
        turtle.color(self._line_color, self._fill_color)
        turtle.begin_fill()

        for i in range(len(self._points)-1):
            turtle.goto(self._points[i+1])

        turtle.end_fill()
        turtle.penup()

        turtle.hideturtle()

    def line_style(self,line_style):
        ''' Changes the line_style
            Passed: Line style (str)
            Returns: None
        '''
        pass

    def remove_section(self,coordinates_to_remove):
        ''' Remove a section of the line between two points
            Passed: Coordinates to remove (tuple)
            Returns: None
        '''
        pass

class Shape_arc(Shape):
    def draw_shape(self):
        ''' Draws and displays the shape
            Passed: None
            Returns: None
        '''
        radius_list=[]
        angle_list=[]
        # print(self._array)
        for i in range(len(self._array)-1):
            radius_list.append( (self._array[i+1]-self._array[i]).polar_mag/2 )
            angle_list.append( (self._array[i+1]-self._array[i]).polar_phase*(180/math.pi) )
            # print((self._array[i+1]-self._array[i]).polar_phase )
        radius_list.append((self._array[0] - self._array[-1]).polar_mag / 2)
        angle_list.append((self._array[0] - self._array[-1]).polar_phase * (180 / math.pi))
        turtle.penup()

        turtle.goto(self._points[0])
        turtle.pendown()
        turtle.color(self._line_color,self._fill_color)
        turtle.begin_fill()
        for i in range(len(radius_list)):
            turtle.setheading(angle_list[i]+90)
            turtle.circle(radius_list[i]*-1, 360)
        turtle.end_fill()
        # for i in range(len(self._points)-1):
        #     turtle.goto(self._points[i+1])
        turtle.penup()

        turtle.hideturtle()

    def arc_bulge(self,bulge_radius):
        ''' Change the bulge of the arc given bulge radius
            Passed: Bulge radius (number)
            Returns: None
        '''
        pass

    def remove_section(self,angle_range):
        ''' Remove a section of arc given given desired angle range to remove
            Passed: Angle range (tuple)
            Returns: None
        '''
        pass