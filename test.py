print('First Name:')
FirstName = input()
print('Last Name:')
LastName = input()
print('Age:')
age = int(input())
if age >= 18:
    print('Welcome, {FirstName} {LastName}!' .format( FirstName=FirstName, LastName=LastName))
if age < 18:
    print('Sorry {FirstName}. You have to be 18 or older' .format( FirstName=FirstName))
