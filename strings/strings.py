my_string = 'Hello World'
print(my_string)

# using ' in a string
my_other_string = 'I\'m a programmer'
print(my_other_string)

# multi line string
sentance = """I rely enjoy doing this
but I need to start doing 
more projects!!"""
print(sentance)

# getting elements of the string
substring = my_string[1:7]
print(substring)

# print every second element of the string and reverse as string using -1.
subs = my_string[::2]
print(subs)
subs2 = my_string[::-1]
print(subs2)

# itrate the string
for i in my_string:
    print(i)

# check if the string contains any characters
if "H" in my_string:
    print("yes")
else:
    print("no")

# other string methods
hello = "hello my man"
print(hello.upper())
print(hello.lower())
print(hello.startswith("hello"))
print(hello.endswith("hello"))
print(hello.count("m"))
print(hello.replace("my", "is"))

# creating a list (array) froma sentance and back to sentance (using split nd join)
sent = "Lets learn to split this sentance"
print(sent.split(" "))
new_sent = "".join(sent)
print(new_sent)

# f-String
var1 = "awesome"
var2 = 5
var3 = 10.2546
print(f"adding to the tring using the format {var1} and {var2} and {var3:.2f} and {var3}")
