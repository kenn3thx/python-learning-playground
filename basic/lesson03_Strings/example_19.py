my_string = "    Hello Everybody.    "

print(my_string) # Output:     Hello Everybody.  

print(my_string.strip()) # Output: Hello Everybody.
print("On an island".strip("O")) # Output: n an island

print('but life is good'.split()) # Output: ['but', 'life', 'is', 'good']
print('but, every boring'.split(",")) # Output: ['but', ' every boring']

print("Help me".replace("me", "you")) # Output: Help you
print("Help me".replace("Help", "Thank").replace("me", "you")) # Output: Thank you
print("Help me, Help you".replace("Help", "Thank")) # Output: Thank you
