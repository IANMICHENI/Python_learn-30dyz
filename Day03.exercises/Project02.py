'''
✅ PROJECT 2 — Coordinate & Slope Analyzer
Goal:

Analyze two points and a line. Calculate slope, distance, x-intercept, y-intercept, and compare slopes. Practice booleans, arithmetic, type checking, and formatted output.

Step-by-Step Instructions

Start a new Python file and add a comment:

# Day 3: Coordinate & Slope Analyzer


Ask the user to enter coordinates for two points:

x1, y1 → point 1

x2, y2 → point 2
(convert inputs to float for precision)

Calculate the slope between the two points:

slope = (y2 - y1) / (x2 - x1)


Calculate the Euclidean distance between the points:

distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)


Use ** or pow() for squaring

Import math.sqrt if you want

Calculate the slope of the line y = 2x – 2

slope = 2

x-intercept: solve 0 = 2x – 2 → x = ?

y-intercept: set x = 0 → y = ?

Compare slopes:

slope between points vs slope of the line

Print which is larger or if equal

Check boolean properties:

Is slope positive?

Is distance > 10?

Print all results in a formatted multi-line block:

Include points, slopes, distance, x-intercept, y-intercept, boolean checks, types (type())

Skills Covered

Variables & floats ✔️

Arithmetic operations ✔️

Slope & distance formulas ✔️

Comparison operators ✔️

Booleans ✔️

Type checking (type()) ✔️

Multi-line formatted printing ✔️

User input ✔️

Print the midpoint of the two points:
'''
# Day 3: Coordinate & Slope Analyzer
import math

x1 = float(input("Enter X coordinate of Point 1: "))
y1 = float(input("Enter Y coordinate of Point 1: "))

x2 = float(input("Enter X coordinate of Point 2: "))
y2 = float(input("Enter Y coordinate of Point 2: "))

slope_points = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

line_slope = 2
x_intercept = 1  
y_intercept = -2  

is_slope_positive = slope_points > 0
is_distance_large = distance > 10

if slope_points > line_slope:
    slope_comparison = "Slope between points is larger than line slope."
elif slope_points < line_slope:
    slope_comparison = "Slope of line is larger than slope between points."
else:
    slope_comparison = "Slopes are equal."

report = f"""
==================== Coordinate & Slope Analyzer ====================

Point 1: ({x1}, {y1})
Point 2: ({x2}, {y2})

Slope between points: {slope_points}  (Positive? {is_slope_positive})
Distance between points: {distance:.2f}  (Greater than 10? {is_distance_large})
Midpoint of points: ({mid_x}, {mid_y})

Line y = 2x - 2:
  Slope: {line_slope}
  X-intercept: {x_intercept}
  Y-intercept: {y_intercept}

Slope comparison:
  {slope_comparison}

Types of variables:
  x1: {type(x1)}, y1: {type(y1)}
  x2: {type(x2)}, y2: {type(y2)}
  slope_points: {type(slope_points)}, distance: {type(distance)}

======================================================================
"""

print(report)



