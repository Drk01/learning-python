def raiseToPower(base_number, power_number):
    result = 1
    for number in range(power_number):
        result = result * base_number
    return result

print(raiseToPower(10,10))
print(10**10)