EX\_25JUL - Busy Train Station Simulator

Create a function named simulate\_train\_station that receives station\_layout, commuter\_data, and time as its parameters.



The function simulates the movement and interaction of commuters in a busy train station using geometric shapes and string manipulation. It should output a string representation of the station state at the given time.



The train station is represented as a 2D coordinate system with various geometric shapes:



&#x20;   Circles: gathering areas (represented as "C,x,y,r" where x,y is the center and r is the radius)

&#x20;   Rectangles: platforms (represented as "R,x1,y1,x2,y2" where (x1,y1) is the top-left corner and (x2,y2) is the bottom-right corner)

&#x20;   Lines: tracks (represented as "L,x1,y1,x2,y2" where (x1,y1) is the start point and (x2,y2) is the end point)



Implement the following steps:



&#x20;   Parse the station layout and commuter data using regular expressions.

&#x20;   Implement geometric calculations to determine commuter movements, collisions, and interactions.

&#x20;   Apply transformations to simulate commuter movement and station dynamics over time.

&#x20;   Generate a string output that visually represents the current state of the station, including commuter positions and densities in different areas.



Parameters:



&#x20;   station\_layout (str): A string encoding the geometric representation of the station. Each shape is separated by a semicolon.

&#x20;   commuter\_data (str): A string containing information about each commuter. Each commuter's data is separated by a semicolon and follows the format "name,destination,x,y,speed".

&#x20;   time (float): A float representing the simulation time in minutes.



The function returns a string representing the current state of the station, including the positions of all geometric shapes and commuters.

