# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) > 0:
        del list_to_remove_elements[5]
    if len(list_to_remove_elements) > 4:
        del list_to_remove_elements[4]
    if len(list_to_remove_elements) > 0:
        del list_to_remove_elements[0]
    return list_to_remove_elements


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "P1nk")
    list_to_add_elements.append("Yellow")
    # list_to_add_elements.insert(len(list_to_add_elements), 'Yellow')
    return list_to_add_elements


def is_empty(list_to_check):
    return len(list_to_check) == 1


def check_lists(list1, list2):
    if len(list1) < 3 or len(list2) < 3:
        return True
    elif list1[2] == list2[2]:
        return True
    elif list1[2] != list2[2]:
        return False


def list_of_lists(list_of_lists_to_modify):
    element1 = list_of_lists_to_modify[11][0:2]
    element2 = list_of_lists_to_modify[1][1:4]
    element3 = list_of_lists_to_modify[2][-2:]
    return [element1, element2, element3]
