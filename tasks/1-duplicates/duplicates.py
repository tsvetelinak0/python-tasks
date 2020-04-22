from typing import List

from constants import example_list


def remove_duplicates(input: List[str]) -> List[str]:
    """This method should return a new list with duplicates removed."""
    deduped_list = []
    for name in example_list:
        if name not in deduped_list:
            deduped_list.append(name)
    return deduped_list
   


def get_duplicates(input: List[str]) -> List[str]:
    """This method should return a list of the items which were duplicated."""
    list_seen = set()
    list_added = list_seen.add
    list_of_duplicates = set(name for name in example_list if name in list_seen or list_added(name))
       
    return list(list_of_duplicates)


# These results are checked by the test. Don't modify this.
deduped_list = remove_duplicates(example_list)
list_of_duplicates = get_duplicates(example_list)
