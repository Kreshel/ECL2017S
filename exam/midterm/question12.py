abbr = input ("What is the three letter abbreviation of this course? ")

answer_status = 'wrong'
if abbr == 'ECL': answer_status = 'correct'
answer_status = ('wrong', 'correct')[abbr == 'ECL']

print('You answer is correct!' if answer_status == 'correct' else 'wrong buddy...try again')
