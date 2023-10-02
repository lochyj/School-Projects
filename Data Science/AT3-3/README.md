# The maze generator

This was much much simpler that I initially expected...

There may be some naming inconsistencies such as `node <-> vertex`, `edge <-> path <-> connection`

The max size you should do is ~75
It is rather slow though and its best if you stay within the 7 - 30 range for the optimal experience
The poor performance is from the use of adjacency matrices which python absolutely LOVES and definitely doesn't struggle to any operations on

Why is there artifacting on the maze itself? TODO: add image here

What is the grey square?
The grey square follows the cursor around and snaps to the closest vertex in the maze. This is used to both illustrate that the maze is a graph and to generate a path to a location in the maze (by clicking when auto-solve is enabled)
