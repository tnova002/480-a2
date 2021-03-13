#480-a2
*Execution*
The two scripts are standalone scripts that can be executed
by simply executing them in a Python environment with no 
special arguments or flags needed. 

h1.py is the 'misplaced tile' heuristic and h2.py is the 'Manhattan' heuristic.

*Performance*
Like the previous assignment, the informed search algorithms 
were not able to find a solution to the 24-puzzle problem within
a reasonable time constraint (about an hour each). 
I formatted the output from the program as such:
(h, c, state)
where h is the heuristic value of the given state, c is the counter
which was used as a tie-breaker for placement in the priority queue,
and state is the current state of the board.
This format holds for both of the algorithms detailed. 

When these algorithms were adapted to accept an 8-puzzle problem instead,
they were able to find a solution fairly quickly. It appears that the
state-space of the 24-puzzle problem is so massive that it would require
a very long time and a large memory budget to find a solution. 
When checking on the output of the programs, they appear to be moving closer 
to the solution (the heuristic value is stepping down from the original state),
but there are thousands of states that share the same heuristic value so the
program gets clogged with a lot of junk states that are just different permutations
of the same heuristic value that happen to not be moving closer.