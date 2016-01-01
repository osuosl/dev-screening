Student Developer Screening Quiz
================================

Answer the following questions and email your answers, code sample, and debugged script to jobs@osuosl.org with the subject line: Dev Screening Answers


1) What is an interpreted language, and what advantages do they have? In what situations would you use an interpreted language instead of a compiled language like C?


2) Why might you want to separate presentation logic from data logic in a web application?


3) What is Test Driven Development, and why would you use it?


4) What is the difference between an Array and a Dictionary (aka Hash)?


5) What is the difference between a Class variable and an Instance variable?


6) What is the difference between Obect Oriented and Procedural programming? Give an example of where Procedural would work better than Object Oriented.


7) In a relational database, what is a "join table", and why might you need one?


8) Given the following database table, write an SQL query that will return a list of the colors of the three tallest plants.

|id    |plant    |color       |height |
|------|---------|------------|-------|
|1     |tree     |red         |12     |
|2     |bush     |blue        |2      |
|3     |vine     |green       |30     |
|4     |flower   |yellow      |500    |
|5     |hedge    |purple      |8      |
|6     |moss     |white       |1      |


9) What is Recursion, and how would you use it?


10) Code Debugging: 
	In the scripts directory in this repository is a file called debug_this.py. This code is supposed to print a numbered list of names, email addresses, and a computed 'Z Number' - but there are a number of problems with the logic. Debug this script, fix the code as needed and add comments in the code describing what was wrong and how you fixed it. The code is written in Python 2.7, but the errors are not due to python syntax, and you should not need to know the python language to spot the logical errors. You can run it anywhere you have access to python by typing "python debug_this.py". 

11) Code sample:

	In the language of your choice, write code to complete the following task.

	There is a file in this repository called "machine_parts.txt". This file contains a list of parts which can be assembled into one of three separate machines. Each line in the file has a machine number, a part name, and optionally the name of a part which must be added to the machine before this part may be added.

	example line:

	1 nozzle_flange_bracket nozzle_flange

	where the part belongs to machine 1, 'nozzle_flange_bracket' is a part which must be attached before 'nozzle_flange' can be attached, and 'nozzle_flange' is the part name.

	Write code that will list the machine parts in the correct order of assembly for each machine. If a machine can't be assembled given the order of parts, report the last part which can be attached to that machine.