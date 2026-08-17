EX\_17AUG - Community Speed Watch Setup

Create a program that helps organize a community Speed Watch program by processing vehicle detection data, finding volunteer names in a duty roster grid, and planning patrol routes.



Your program should implement a custom HashSet class (with string keys) to track unique vehicle license plates and count how many times each was detected.

Then search a character grid to find all volunteer names from a given list (names can appear horizontally, vertically, or diagonally in any direction).

Finally, determine if volunteers can complete a circuit of all monitoring checkpoints: given fuel available at each checkpoint and fuel needed to reach the next one, find a starting checkpoint where the circuit is possible, or report -1 if no such start exists.



Print the unique plates with their detection counts (sorted alphabetically), the list of found volunteer names, and the starting checkpoint index (or -1).

