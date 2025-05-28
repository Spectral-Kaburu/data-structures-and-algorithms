# coins is the list of denominations you got 
# amount is the total amount to be reached
# this solution only gives an answer of how many coins will be used
# I am yet to configure it to give the specific numbers, if that is even possible.


def change_matrix(coins:list[int], amount:int):   
    matrix = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)] # creates a matrix that will store the ans(number of coins)
    for i in range(amount + 1):
        matrix[0][i] = i            # fills the first column of the matrix with values 0 - amount

    return matrix

def change_coins(coins:list[int], amount:int):
    matrix = change_matrix(coins, amount)

    for c in range(1, len(coins) + 1):
        for r in range(1, amount + 1):              # Iterates over the matrix

            if coins[c-1] == r:                     
                matrix[c][r] = 1                    # if r(amount on the matrix) == the coin in the iteration then only 1 coin is needed  

            elif coins[c-1] > r:
                matrix[c][r] = matrix[c-1][r]       # the number of coinsis equal to the number above the position

            else:
                matrix[c][r] = min(matrix[c-1][r], 1 + matrix[c][r - coins[c-1]]) 

            
    return matrix[-1][-1]


print(change_coins([1, 5, 6, 8], 11))