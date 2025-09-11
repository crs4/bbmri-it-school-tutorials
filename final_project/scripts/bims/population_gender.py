import random
def pick_gender(p_m=0.5):
    """
    Randomly picks 'M' or 'F' based on probability.

    :param p_m: Probability of picking 'M' (0 <= p_m <= 1).
    :return: 'M' or 'F'
    """
    return random.choices(["M", "F"], weights=[p_m, 1 - p_m])[0]






