# Find the first n ugly numbers

# Ugly numbers are the numbers whose prime factors are 2,3 or 5.

# Normal Approach :
# Run a loop till n and check if it has 2,3 or 5 as the only prime factors
# if yes, then print the number. It is in-efficient but has constant extra space.

# DP approach :
# As we know, every other number which is an ugly number can be easily computed by
# again multiplying it with that prime factor. So stor previous ugly numbers till we get n ugly numbers
# This approach is efficient than naive solution but has O(n) space requirement.

def ugly_numbers(n):
    
    # keeping a list initialised to 1(as it a ugly number) to store ugly numbers
    ugly = [1]

    # keeping three index values for tracking index of current number
    # being divisible by 2,3 or 5
    index_of_2, index_of_3, index_of_5 = 0, 0, 0

    # loop till the length of ugly reaches n i.e we have n amount of ugly numbers
    while len(ugly) < n:

        # append the multiples checking for the minimum value of all multiples
        ugly.append(min(ugly[index_of_2] * 2, min(ugly[index_of_3] * 3, ugly[index_of_5] * 5)))

        # keep incrementing the indexes as well encounter multiples of 2,3 or 5 respectively
        if ugly[-1] == ugly[index_of_2] * 2:
            index_of_2 += 1

        if ugly[-1] == ugly[index_of_3] * 3:
            index_of_3 += 1

        if ugly[-1] == ugly[index_of_5] * 5:
            index_of_5 += 1

    # return the list
    return ugly


# Driver Code
n = 20
print(ugly_numbers(n))

# Time Complexity : O(n)
# Space Complexity : O(n)
