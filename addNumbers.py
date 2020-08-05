# add numbers from 1 to num recursively
def count(num):
    result = 0

    if num == 0:
        return result
    else:
        result = num + count(num-1)
        return result

# add numbers from 1 to x iteratively
x = 41 
y = 0
while x >= 1:
    y = y+ x + (x-1)
    x -= 2
    

print(y)