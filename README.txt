*****************************************************************************
*                   requires python 3 to be installed                       *
*****************************************************************************

**************************About this program*********************************
This program compute PageRank scores for an input web-graph using the power 
iteration method. It continues iterating until convergence is achieved or 
100 iterations. Convergence is achieved when none of the values changes more 
than 5% of that of the previous iteration. The program can do both the 
standard formula and Googles formula (teleportation: teleportation parameter 
value of 0.85). 
*****************************************************************************

**************************Input and Output***********************************
Inputs for the program can come in two forms:
    1. The input come from a file using an adjacency using integers as nodes:
        <node number> <connections>
        0 1 2 3 6 9 12
        1 0 2 5 20
        ect... 
    2. The program can generate a random adjacency list to solve
    
Output are written in two files. These files contain (in each line) a pair
of numbers as <Vertex ID, PageRank Value>. The output for the standard power 
iteration will be written in 'part_a.txt' and Google's formula will be 
written in file 'part_b.txt' 
*****************************************************************************

******************************Files Included*********************************
I have included a file for dead end case and a trap file for spider trap 
cases. I have also included a sample file that works out nicely.  
******************************************************************************

*********************************Running**************************************
You will be prompted to enter a custom file to find the page ranks or have
the program create a custom randomly generated adjacency list to find the 
page ranks for.You will then be prompted to do standard power iteration 
(part a) or Google's formula (part b). The randomly generated list will be 
written in 'adj_list.txt'. 

To Run:

In your terminal, navigate to this folder and type: python3 adjacency_lists.py
******************************************************************************
Enjoy.
