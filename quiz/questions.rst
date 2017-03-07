Student Developer Screening Quiz
================================

Answer the following questions and email your answers, code sample, and debugged
script to jobs@osuosl.org with the subject line: Dev Screening Answers.


1) What is an interpreted language, and what advantages do they have? In what
situations would you use an interpreted language instead of a compiled language
like C?


2) Name and describe three important concepts in Object Oriented Programming.


3) What is Test Driven Development, and why would you use it?


4) What is the difference between an Array and a Hash (aka Dictionary)?


5) Tabs or Spaces? Why?


6) Given the following database table, write an SQL query that will return the
animal name and food of the three animals with the highest populations.

	|id     |animal    |food        |population |
	|-------|----------|------------|-----------|
	|35     |ocelot    |mouse       |1200000    |
	|36     |dingo     |rabbit      |16000000   |
	|41     |capybara  |grass       |400000     |
	|52     |remora    |blood       |82000000   |
	|54     |emu       |fruit       |725000     |
	|63     |gecko     |insects     |9000000    |
	|68     |earwig    |lettuce     |420000000  |


7) What is your favorite editor, and why?


8) What is Recursion, and how would you use it?


9) Code Debugging:

	In the scripts directory in this repository is a file called names.rb. This
  code is supposed to print a numbered list of names, email addresses, and a
  weighted score - but there are a number of problems with the logic.

	Debug this script, fix the code as needed and add comments in the code
  describing what was wrong and how you fixed it. The code is written in Ruby,
  but the errors are not due to ruby syntax, and you should not need to know the
  ruby language to spot the errors. You can run it anywhere you have access to
  ruby by typing "ruby names.rb". Feel free to use Google or other resources to
  help you understand the syntax if you are not familiar.


10) Code sample:

	In the language of your choice, write code to complete the following task.
  This is a complicated problem, it's ok if you can't make it perfect. Try your
  best and send us code that shows how you are thinking about the problem, even
  if you can't get it to work.

	There is a file in this directory called "machine_parts.txt". This file
  contains a list of parts which can be assembled into one of three separate
  machines. Each line in the file has a machine number, a part name, and
  optionally the name of a part which must be added to the machine -before- this
  part may be added. Some parts have mulitple dependencies  - this means there
  will be several lines describing the same part.

	example line:

	2 nozzle_flange nozzle_flange_bracket

	In this example, the part belongs to machine 2, 'nozzle_flange' is the part
  name, and 'nozzle_flange_bracket' is a part which must be attached before
  'nozzle_flange' can be attached.

	Write code that will list the machine parts in the correct order of assembly
  for each machine. If a machine can't be assembled given the order of parts,
  report the last part which can be attached to that machine.

  (Hint: start with the parts that don't have any dependencies, and can be
  installed without anything else being installed first.)
