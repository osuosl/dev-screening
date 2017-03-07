# Class for calculating weighted scores
#
# To use: instantiate this class with an array of 10 scores corresponding to the
# names list, and call the output method.
#
# For each person in the names list with a score greater than or equal
# to 5 this code should do the following:
#
# 1. Calculate their weighted score, which is (215 + average score) / score
#
# For example, if the average score is 10 and one person's score is 12,
# their weighted score is
#
# (215 + 10)/12 = 225/12 = 18.0
#
# 2. Print out the name, corresponding email and weighted score on a line.
# Number each line, starting at 1, so that the output looks something like
# this:
#
#	 1. Name, email, W = weighted_score
#	 2. Name, email, W = weighted_score
#	 3. Name, email, W = weighted_score
#	 .
#	 .
#	 etc

class WeightedScore

  def initialize(scores)
    @names = ['Amy', 'Annie', 'Fred', 'Marge', 'Tim', 'Sarah', 'John', 'Elise',
		 'Andy', 'Ellen']
    @emails = ['amy@example.com', 'annie@example.com', 'fred@example.com',
		  'marge@example.com', 'tim@example.com', 'sarah@example.com',
		  'john@example.com', 'elise@example.com', 'andy@example.com',
		  'ellen@example.com']
    @scores = scores

  end

  def weighted_score(score)
    return average_score + 215/score
  end

  def average_score
    score = 0
    i = 1
    @scores.each do |score|
    	score += score
    	i = i + 1
    end
    return score / i
  end

  def output
    i = 0
    while i < 10
      name = @names[i]
    	i = i + 1
    	line_string = i.to_s
  		line_string << ". #{name}, #{@emails[i]}, W = #{weighted_score(@scores[i]).to_s}"
      if @scores[i] > 5
    	   puts line_string
      end
    end
  end
end

# START

# these ten scores correspond, in order, with the names of test taker
scores = [2, 5, -2, 9, 0, 23, -8, 7, 1, 4]

# instantiate the class with the scores
znumber = WieghtedScore.new(scores)

# print out the names, emails and weighted scores
znumber.output
