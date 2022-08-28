"""Show information about a specific user"""

from functools import lru_cache


@lru_cache
def calculate_lucky_no(birthday: str) -> int:
    """Calculate the lucky number of a user based on his/her birthday"""
    lucky_no = sum(map(int, birthday.replace("/", "")))
    if lucky_no > 9:
        return calculate_lucky_no(str(lucky_no))
    return lucky_no


def user_info():
    """Build and return details about a specific user"""
    return None


# print(calculate_lucky_no("2000/10/14"))
