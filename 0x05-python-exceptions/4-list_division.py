#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                if not (isinstance(my_list_1[i], (int, float))
                        and isinstance(my_list_2[i], (int, float))):
                    raise TypeError("wrong type")
                if my_list_2[i] == 0:
                    raise ZeroDivisionError("division by 0")
                div = my_list_1[i] / my_list_2[i]
                result.append(div)
            except IndexError:
                print("out of range")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            finally:
                pass
    except IndexError:
        print("out of range")
    return result
