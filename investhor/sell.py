import math

def calculate_selling_discount(interest, verification):
    """ Calculates the discount based on investment interest and risk
    """

    if interest > 100:
        discount = math.floor(interest/20)
    elif interest > 50:
        discount = math.floor(interest/15)
    else:
        discount = math.floor(interest/10)
    if verification:
        discount += 1
    return discount
