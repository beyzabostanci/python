#re.findall returns all that matches
import re


#matching and extracting data

x= "my 2 favoritr numbers are 19 and 43"
y=re.findall("[0-9]+", x)
print(y)

#greedy(larger) matching more than 1 overlapping string matching

x = "From: Using the : character"
y= re.findall("^F.+", x)
print(y)

#non-greedy mathcing----?

x="From: Using the : character"
y=re.findall("^F.+?:", x)
print(y)

# paranthesis says start and end about what string to extact
#you are addşng the effecting things to their right

#\$[0-9.]+     id like a dollor sign followed by one or more digits or dots