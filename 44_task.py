def task(num):
    results = {}
    results[f"is {num} divisible by 5 and 6?"] = (num % 5 == 0) and (num % 6 == 0)
    results[f"is {num} divisible by 5 or 6?"] = (num % 5 == 0) or (num % 6 == 0)
    results[f"is {num} divisible by 5 or 6, but not both?"] = (num % 5 == 0) ^ (num % 6 == 0)
    return results


# Example usage:
number = 24
print(task(number))