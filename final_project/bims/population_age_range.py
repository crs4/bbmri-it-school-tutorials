

import random
from datetime import datetime, timedelta


def random_dob(age_start, age_end):
    """
    Generate a random date of birth for an age in (age_start, age_end) exclusive.
    Returns a string in the format 'dd-mm-yyyy'.

    Parameters:
        age_start (int): Lower age bound (exclusive)
        age_end (int): Upper age bound (exclusive)

    Returns:
        str: Random date of birth in 'dd-mm-yyyy' format
    """
    today = datetime.today()

    # Calculate latest and earliest possible DOBs
    # Subtract age_end and age_start+1 to make ranges exclusive
    latest_dob = today - timedelta(days=(age_start + 1) * 365)
    earliest_dob = today - timedelta(days=(age_end - 1) * 365)

    # Generate a random date between earliest_dob and latest_dob
    delta_days = (latest_dob - earliest_dob).days
    random_days = random.randint(0, delta_days)
    dob = earliest_dob + timedelta(days=random_days)

    return dob.strftime('%Y-%m-%d')