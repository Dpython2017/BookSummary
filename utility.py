def average(time_list):
    """
    :param time_list:List of time stamps
    :type time_list: list
    :rtype: int

    """
    if time_list:
        avg = time_list[0]
        for i in range(1, len(time_list)):
            avg += time_list[i]

        return avg // len(time_list)


def difference(d1, d2):
    """
    Calculates the difference between two time stamps
    :param d1: time stamp 1
    :param d2: time stamp 2
    :return: difference of timestamp 1 and timestamp 2
    :rtype: datetime
    """
    if d1 and d2:
        diff = d2 - d1
        # print(diff)
        return diff


def clean(string):
    """
    Cleans the input, removes escape characters
    :param string: input string
    :return: clean string
    """
    return string.replace("\n", "")
