	If you have any questions or ideas please contact me on discord @Maxxie#7456 any and all ideas are welcome!!!

rest:
	Halts the process for a given amount of time in seconds
	Ex: `rest 10`
	Ex: `rest $DATA01

rand:
	Outputs a sudo random number based on one minimum and one maximum
	Ex: `rand 1 100`
	Ex: `rand $DATA0 $DATA1`

define:
	Creates a function that will be executed when the name is sent as a command different lines are seperated by a 'then' statement
	Ex: `define FunctionName print hello then print world then print !`
	Then if you call the function: `FunctionName` the code will be executed

length:
    Outputs the length of a given argument
    Ex: `length abcdefg`

tape:
	Outputs the current DATA tape
	Ex: `tape`

out:
	Outputs the current data block at the pointer index
	Ex: `out`

DATA or $DATA<data index>:
	Outputs the data block of the given argument
	Ex: `DATA 0`
	Ex: `print $DATA0`


data:
	Establishes a new data block of either type int (integer), str (string), or a bool (boolean)
	Ex: `data int 2`
	Ex: `data str hello world`
	Ex: `data bool True`

if:
	Test if a given data block or argument is True if it is true it will excute a set of commands
	Ex: `if True do out`
	Ex: `if $DATA0 do out`

is:
	Test if a given expression is true or false
	Ex: `is 1 + 1 == 2`
	Ex: `is 9 > 9`
	It is also possible to assign the output of these commands to a boolean data block
	Ex: `data str is 1 + 1 == 2` then `data bool $EVAL0`

print:
	Outputs text or data blocks from given arguments
	Ex: `print hello world`
	Ex: `print $DATA0`
	Ex: `print $EVAL0`

loop:
	Loops and does something multiple time based on given arguments
	Ex: `loop 3 print hewo`
	Ex: `loop $DATA0 print hewo`
	Ex: `loop $DATA0 print $DATA0`

location:
	Outputs the current pointer index
	Ex: `location`

set:
	Sets the current data block at the pointer index to a different value based on given arguments
	Ex: `set int 420`
    (Note, that when setting the int data type the value it is set to is first evaluated)
	Ex: `set bool True`
	Ex: `set str Hello, World`

math:
	Evaluates a math equasion from a given set of arguments
	Ex: `math 1 + 1`
	(Spaces are optional seing as the mathmatical operations are ran through python3)
	All allowed operators are:  + - * / and ()

decrament:
	Decraments the pointer by a value of 1
	Ex: `decrament`

incrament:
	Incraments the pointer by a value of 1
	Ex: `incament`

$EVAL:
	Evals a pice of code from a string given as an argument
	Ex: `data str print hello world` then `$EVAL0`
    (Note, code no longer prints the value. The output of this code will be an error saying there is no command named hello!)
