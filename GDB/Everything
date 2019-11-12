GDB:gnu project debugger
1)uname -a 
gives the specs of the machine

2)gcc -st=c99 -g -o output file.c 

g flag:means you can see the proper names of variables and functions in your stack frames, get line numbers and see the source as you step around in the executable

-std=C99 flag:implies use standard C99 to compile the code

-o flag :writes the build output to an output file

3)gdb ./output 

1)run or r –> executes the program from start to end.
2)break or b –> sets breakpoint on a particular line.
3)disable -> disable a breakpoint.
4)enable –> enable a disabled breakpoint.
5)next or n -> executes next line of code, but don’t dive into functions.
6)step –> go to next instruction, diving into the function.
7)list or l –> displays the code.
8)print or p –> used to display the stored value.
9)quit or q –> exits out of gdb.
10)clear –> to clear all breakpoints.
11)continue –> continue normal execution

>info b :used to see breakpoints
>disable b:disable break point
>enable b:re-enable b 

>Run the code by typing “run or r”.If you haven’t set any breakpoints, run command will simply execute the full program

>To see the value of variable, type “print variable_name or p variable_name“

>To change the value of variable in gdb and continue execution with changed value, type “set variable_name“.

4)GDB commands
1)b main - Puts a breakpoint at the beginning of the program
2)b - Puts a breakpoint at the current line
3)b N - Puts a breakpoint at line N
4)b +N - Puts a breakpoint N lines down from the current line
5)b fn - Puts a breakpoint at the beginning of function "fn"
6)d N - Deletes breakpoint number N
7)info break - list breakpoints
8)r - Runs the program until a breakpoint or error
9)c - Continues running the program until the next breakpoint or     error
10)f - Runs until the current function is finished
11)s - Runs the next line of the program
12)s N - Runs the next N lines of the program
13)n - Like s, but it does not step into functions
14)u N - Runs until you get N lines in front of the current line
15)p var - Prints the current value of the variable "var"
16)bt - Prints a stack trace
17)u - Goes up a level in the stack
18)d - Goes down a level in the stack
19)q - Quits gdb

5)Watch points 
watch x == 3

Sets a watchpoint, which pauses the program when a condition changes (when x == 3 changes).

Watchpoints are great for certain inputs (myPtr != NULL) without having to break on every function call.

6)continue 
Resumes execution after being paused by a breakpoint/watchpoint. The program will continue until it hits the next breakpoint/watchpoint

7)delete N 
deletes breakpoint N (breakpoints are numbered when created)

8)set 
set x=3
set x = y
Sets x to a set value (3) or to another variable (y)

9)call 
call myfunction()

call myotherfunction(x)

call strlen(mystring)

Calls user-defined or system functions. This is extremely useful, but beware of calling buggy functions.

10)display 

display x

Constantly displays the value of variable x, which is shown after every step or pause. Useful if you are constantly checking for a certain value.

undisplay x
