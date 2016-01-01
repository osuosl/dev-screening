"""
Assume that the lists below are all the correct order, the first
name in the names list corresponds to the first email in the
emails list, and the first score in the scores list, etc.

For each person in the names list with a score greater than or equal 
to 5:

1. Calculate their Z_number, which is (215 + average score) / score

For example, if the average score is 10 and one person's score is 12, 
their Z_number is 

(215 + 10)/12 = 225/12 = 18.0

2. Print out the name and corresponding email and Z_number on a line. 
Number each line, starting at 1, so that the output looks something like 
this:

	1. Name, email, Z = Z_number
	2. Name, email, Z = Z_number
	3. Name, email, Z = Z_number
	.
	.
	etc

"""

names = ['Bob', 'Annie', 'Fred', 'Marge', 'Tim', 'Sarah', 'John', 'Elise',
		 'Andy', 'Ellen']
emails = ['bob@example.com', 'annie@example.com', 'fred@example.com',
		  'marge@example.com', 'tim@example.com', 'sarah@example.com',
		  'john@example.com', 'elise@example.com', 'andy@example.com',
		  'ellen@example.com']
scores = [2, 5, -2, 9, 0, 23, -8, 7, 1, 4]

score = 0
i = 1

for score in scores:
	score += score
	i = i + 1

average_score = score / i

while i < 10:
	z_number = average_score + 215/scores[i] 
	i = i + 1

	line_string = str(i)
	if scores[i] > 5:
		line_string += ". " + names[i] + ", " + emails[i] + ", Z =" + str(z_number)

	print(line_string)
