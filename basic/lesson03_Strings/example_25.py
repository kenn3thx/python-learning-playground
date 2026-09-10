pi = 3.14159
s = "pi number"
my_string = "Pi is %f from %s" % (pi, s)
my_string2 = "Pi is %.2f from %s" % (pi, s)

print(my_string) # Output: Pi is 3.141590 from pi number
print(my_string2) # Output: Pi is 3.14 from pi number