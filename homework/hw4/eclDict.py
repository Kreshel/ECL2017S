eclNames = ['nicholas boeker', 'bradley bridges', 'sagar dhana', 'travis driver', 'eric gagliano',
            'christian garcia', 'matthew goree', 'lucero herrera', 'jake janssen', 'michael langford',
            'colin lewis', 'mark loveland', 'emilio mendiola', 'kreshel nguyen', 'russell philley',
            'caleb phillips', 'joseph robbins', 'bradley smith', 'vivek varier', 'amir shahmoradi']

eclRoles = []

for i in range(18):
    eclRoles.append('student')

eclRoles.append('assistant')
eclRoles.append('instructor')

eclDict = dict(zip(eclNames,eclRoles))
