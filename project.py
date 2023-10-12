from list import mylist_db
from match import match
from typing import List, Tuple, Callable, Any

def get_school(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[0]


def get_neighbor(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[1]


def get_numfood(movie: Tuple[str, str, int, List[str]]) -> int:
    return movie[2]


def get_food(movie: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[3]

for food in mylist_db:
    print(get_school(food))


def food_by_school(matches: List[str]) -> List[str]:
    """Finds all food places located near school

    Args:
        matches - a list of 1 string, just the school.

    Returns:
        a list of food places near the school
    """
    places = []
    for food in mylist_db:
        school = get_school(food)
        if school == matches:
            places = (get_food(food))
    return places


def neighbor_by_school(matches: List[str]) -> List[str]:
    """Finds school neigborhood

    Args:
        matches - a list of 1 string, just the school.

    Returns:
        neighborhood of school
    """
    places = []
    for food in mylist_db:
        school = get_school(food)
        if school == matches:
            places.append(get_neighbor(food))
    return places
print(neighbor_by_school("lane tech"))