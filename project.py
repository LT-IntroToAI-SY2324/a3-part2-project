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
        if school == matches[0]:
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
        if school == matches[0]:
            places.append(get_neighbor(food))
    return places


def school_by_neighbor(matches: List[str]) -> List[str]:
    """Finds school(s) in neigborhood

    Args:
        matches - a list of 1 string, just the neighborhood.

    Returns:
        school(s) that's in neighborhood 
    """
    places = []
    for food in mylist_db:
        school = get_neighbor(food)
        if school == matches[0]:
            places.append(get_school(food))
    return places


def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("which neighborhood is % located"), neighbor_by_school),
    (str.split("which schools are in %"), school_by_neighbor),
    (str.split("what restaurants are in %"), food_by_school),
    (["bye"], bye_action),
]
def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    ans = []
    action = []
    for pattern in pa_list:
        check = match(pattern[0],src)
        if check != None:
            for source in src:
                if source == "neigborhood":
                    ans = neighbor_by_school(check)
                elif source == "schools":
                    ans = school_by_neighbor(check)
                elif source == "restaurants":
                    ans = food_by_school(check)
            if ans == []:
                action.append("No answers")
                return action
            else:
                action = ans
    if action == []:
        action.append("I don't understand")
        return action
    return action

def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()

if __name__ == "__main__":
    assert sorted(food_by_school(["lane tech"])) == sorted(
        ["mcdonalds","popeyes","chop suey","wendys","dunkin donuts"]
    ), "failed food_by_school test"
    assert sorted(neighbor_by_school(["de la salle"])) == sorted(
        ["bronzeville"]
    ), "failed neighbor_by_school test"
    assert sorted(school_by_neighbor(["garfield park"])) == sorted(
        ["westinghouse"]
    ), "failed 1st school_by_neighbor test"
    assert sorted(school_by_neighbor(["west side"])) == sorted(
        ["whitney young", "cristo rey"]
    ), "failed 2nd school_by_neighbor test"
    
    print("All tests passed")