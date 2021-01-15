# 2D Graphical Outputs using Matrices

## Dependencies
* [Python 3.8](https://www.python.org/downloads/)
* [Math module](https://docs.python.org/3/library/math.html)
* [System module](https://docs.python.org/3/library/sys.html)
* [Turtle module](https://docs.python.org/3/library/turtle.html)
* [Copy module](https://docs.python.org/3/library/copy.html)

## Description
* Uses complex numbers classes and graphical classes
 to create graphical outputs.
 
## Usage
1. Open main.py
2. Run the code.

## Main File
### Calculator Class
* There are three protected fields: The real part, the imaginary part and the 
matrix.
* There are two read-only properties in the Calculator Class that are used to
return the polar coordinate's magnitude and phase of the complex number.
* Functions: Get polar magnitude, get polar phase, add (overload) two complex 
numbers, subtract (overload) two complex numbers, multiplication overloading, 
multiply two complex numbers, multiply two matrices (vector and matrix 
multiplication), division overloading, divide two complex numbers, 
divide two matrices (vector division), destructor.

### Matrix Class
* Functions: Constructor, get matrix, string representation (for user output), 
destructor.

*Preconditions:*
* Vector: A vector is defined as a one column matrix 
and must be listed vertically.
* The size (number of elements) of each row, of each created matrix, must be the same.
* Matrix multiplication: The number of columns in the first matrix has to be 
the same as the number of rows in the second matrix.
* Vector multiplication/division (Element-wise): The number of rows and columns in the first matrix has
 to be equal to the number of rows and columns in the second matrix.

### Complex Number Class
* There in one protected field: The complex number.
* Functions: Constructor, set complex number, get complex number, get real part,
get imaginary part, string representation (for user output), destructor.

## User File
### UI Class
* There are two protected fields: The list of matrices and the resultant matrix.
* Functions: Input multiplication type, prompt user to delete matrix, return user request, input matrix 
dimensions, check dimensions are valid, generate list of matrices, check result 
is valid, print current result, ask if user wants to multiply result by another 
matrix, destructor.

## Graphics File
### Drawing Class
* There is one private field (list of shapes), and
 one public field (background color)
* Functions: Constructor, add background color, display drawing, add border

### Shape Class
* There are three potected fields (list of coordinates, line color,
 filling color, and list of points)
* Functions: Constructor, rotate shape, move shape, change shape size,
 convert matrix to list of tuples, add color to shape

### Linear Shape Class
* Functions: Draw shape, specify line style, remove section

### Arc Shape Class
* Functions: Draw shape, Change the bulge of the arc, remove section

## Author
* Jonas Chianu