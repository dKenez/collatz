### Collatz
***
This is a small project inpired by a [Numberphile video](https://www.youtube.com/watch?v=LqKpkdRRLZw). 
It is not meant to be particularly fast or beautifully animated, it is only intended to show the beauty of maths.

The repository contains three Python files:
1. `collatz.py`
2. `collatz_plot.py`
3. `collatz_tree.py`

`collatz.py` contains the functions used in the other two files, as well as a little script to calculate collatz 
sequences when run on its own.
`collatz_plot.py` plots the number of iterations needed for each number to reach 1 alongside a log2(n) plot, which is 
the lower boundary for how many steps a number has to take to reach one. For the powers of 2, this is gives exactly the 
number of steps.
The final file is `collatz_tree.py`, which draws the numbers is a similar fashion to the one shown in the above 
mentioned video.