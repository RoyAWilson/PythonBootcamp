'''
Problem to turn 1000 coins.
Start all coins heads up.
1st iteration:  Turn every second coin over.
2nd iteration:  Turn every 3rd coin over.
nth iteration:  Turn every n+1th coin over.
Return the coins that are facing heads up after last iteration
'''


def coin(num) -> dict:
    '''
    Function to model the coin problem 
    Argument num number of coins as an integer
    Variables:
        coins - list to all coins required
        coins_dict - dictionary to display key as coin number and Heads for the relevant coins only
    '''

    coins: list = [0] * num
    coins_dict: dict = {}
    for i in range(1, num):
        for j in range(0, num, i):
            coins[j] = 1 - coins[j]
    for k, v in enumerate(coins):
        if v != 0:
            coins_dict[k] = 'Heads'
    return coins_dict


print(coin(1001))
