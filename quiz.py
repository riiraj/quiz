points = 0

svar_1 = input('Bor Rimmi i Helsingfors?')

if svar_1.lower() == 'jo':
    points = points + 1
else:
    points = points -1


svar_2 = input('Är Rahul datanom?')

if svar_2.lower() == 'nej':
    points = points + 1
else:
    points = points -1

svar_3 = input('Pappa kan baka?')

if svar_3.lower() == 'nej':
    points = points + 1
else:
    points = points -1

svar_4 = input('Hur gammal är Mamma?')

if svar_4.lower() == '51':
    points = points + 1
else:
    points = points -1

svar_5 = input('Bor Richi i Jakobstad?')

if svar_5.lower() == 'nej':
    points = points + 1
else:
    points = points -1

print("Du fick " + str(points) + " poäng!")