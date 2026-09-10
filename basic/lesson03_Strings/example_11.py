my_string = "Hello World"

helloStr = my_string[0:5] # Not include #5, this mean get from index 0 to index 4.
helloStr2 = my_string[:5] # If start with index 0, can bypass it.

worldStr = my_string[6:11] 
worldStr2 = my_string[6:] # If end with last index, can bypass it 

print(helloStr) # Output: Hello
print(helloStr2) # Output: Hello

print(worldStr) # Output: World
print(worldStr2) # Output: World
