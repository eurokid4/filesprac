with open("important.txt") as f:
    impt=f.read()
print(impt)
list1=impt.split('\n')
print(list1)

with open("important.txt") as f:
    f.write("credits to asdfmovie9")