"""
Assume that the lists below are all the correct order, the first
name in the names list corresponds to the first email in the
emails list, and the first score in the scores list, etc.

Print out all the names and emails for people whose scores are
greater than or equal to 5.

Then calculate the Z number, which is (215 + average score) / score

for example, if the average score is 10 and one person's score is 12, 
their Z number is 

(215 + 10)/12 = 225/12 = 18.0

Number each line, so that the output looks something like this:

1. Name 1, email 1, Z = Z number 1
2. Name 2, email 2, Z = Z number 2
.
.
.

etc

"""

names = ('Bob', 'Anne', 'Fred', 'Marge', 'Tim', 'Sarah', 'John', 'Elise',
		 'Andy', 'Ellen')
emails = ('bob@example.com', 'anne@example.com', 'fred@example.com',
		  'marge@example.com', 'tim@example.com', 'sarah@example.com',
		  'john@example.com', 'elise@example.com', 'andy@example.com',
		  'ellen@example.com')
scores = (2, 5, -2, 9, 0, 23, -8, 7, 1, 4)

score = 0
i = 1

for score in scores:
	score += score
	i = i + 1

average_score = score / i

i = 0
while i < 10:
	z_number = (average_score + 215)/scores[i] 
	i = i + 1

	line_string = str(i)
	if scores[i] > 5:
		line_string += ". " + names[i] + ", " + emails[i] + ", Z =" + str(z_number)

	print(line_string)
