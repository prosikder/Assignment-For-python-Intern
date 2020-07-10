def muri():
    string_1 = input("string_1 = ")
    string_2 = input("string_2 = ")

    return string_1.count(string_2)

a = muri()
print("Here string_2 occur in string_1", a, "times")
