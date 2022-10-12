def num_inv(a):

    inv  = 0

    def sort(a):
        if a == []:
            return []
        
        pivot = a[0]
        nonlocal inv

        left, right = [], []
        # left = [x for x in a if x < pivot]
        # right = [x for x in a[1:] if x >= pivot]
        # inv  =  inv + len(left) + len(right)

        for number in a[1:]:
            if number < pivot:
                inv += (1 + len(right))
                left.append(number)
            else:
                right.append(number)
               

        return sort(left) + [pivot] + sort(right)
    
    sort(a)
    return inv

# print(num_inv([4,1,3,2]))
print(num_inv([2,5,6,1,3,4]))