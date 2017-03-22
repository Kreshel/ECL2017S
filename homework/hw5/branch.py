#!/usr/bin/env python

abbr = input('What is the three letter abbreviation of this course? ')

answer_status = 'wrong'
if abbr == 'ECL': answer_status = 'correct'
# answer_status = ('wrong', 'correct')[abbr == 'ECL']
# this works because if abbr is 'ECL', answer_status is the set to the value in location 1
# else answer_status is set to the value in location 0 which is 'wrong'

print( ('Wrong buddy.. try again.', 'Your answer is correct!')[answer_status == 'correct'])
