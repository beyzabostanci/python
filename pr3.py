stuff = list()
stuff.append("99, yetti")
print(stuff)

#is something IN the list
print("99" in stuff)
print("99, yetti" in stuff)

nums = [1,34,65,72,48,99]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))#aritmetik ortalama


#FUNCTİON THAT FINDS THE AVARAGE    
nums = [1,34,65,72,48,99]
while True:
    inp = input("enter a number:  ")
    if inp == "done" : break
    value = float(inp)
    nums.append(value)

avarage = sum (nums)/len(nums)
print("avarage:", avarage)