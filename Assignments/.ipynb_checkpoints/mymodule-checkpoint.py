def check_even (num):
    if not isinstance(num, int):
        raise Exception(f"Error: {num} is not an integer") 
    if num %2 == 0:
        return "even"
    return "odd"