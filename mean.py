def mean(num_list):
    if any(isinstance(num, complex) for num in num_list):
        return NotImplemented
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError :
        return 0
    except TypeError as original_error :
        msg = "The algebraic mean of an non-numerical list is undefined.\
               Please provide a list of numbers."
        raise TypeError(original_error.__str__() + "\n" +  msg)
