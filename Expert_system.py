import random

appliances = [['Fridge', 0], ['Washnig machine', 0], ['Dishwasher', 0]]


questions = [('Does it use hot water?: ', 'W, D'), ('Does it clean dishes?: ', 'D'),
             ('Does it store food?: ', 'F'), 
             ('Does is clean clothes?: ', 'W'), 
             ('Is there a low temperature iside?: ', 'F'),
             ('Is it related to eating?: ', 'F, D'),
             ('Can you see inside it when it is in use?:', 'W'),
             ('Are the objects iside of it moving when it is in use?: ', 'D'),
             ('Does it do something else than clean dishes:? ', 'W, F')]



for i in range(len(questions)):
    # q = random.choice(questions)
    # q[2] += 1
    # a = input(q[0])
    # print(questions)
    
    
    a = input(questions[i][0])
    while a not in ['YES'.lower(), 'NO'.lower()]:
        print('\nInvalid answer, try again.')
        a = input(questions[i][0])
    
    if a in ' YES'.lower():
        for x in appliances:
            if x[0][0] in questions[i][1]:
                x[1] += 1



    elif a in ' NO'.lower():
        for y in appliances:
            if y[0][0] not in questions[i][1]:
                y[1] += 1


highest = appliances[0]

for k in appliances:
    if k[1] > highest[1]:
        highest = k

print(highest[0])
