# Null Input

print('''
Where do you want to Organize your Files?
1. Downloads
2. Any Other Location
Enter the Full Path to your Directory [Just Type 'Downloads' for Case 2] ->
''')

path = input()
if not path:
    print(f"None!")
else:
    print(f"Not Null!")

path = None
if not path:
    path = "Downloads"
else:
    path = "Not Downloads"
print(path)


## Conlusion => Unit Testing Successful for nullInput.