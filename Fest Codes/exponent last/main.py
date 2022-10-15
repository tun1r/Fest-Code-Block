def last_digit(n1, n2):
    value=n1**n2
    string_value=str(value)
    last_digit=int(string_value[-1])
    return last_digit
print(last_digit(9,7))