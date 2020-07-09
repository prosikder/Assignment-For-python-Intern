def strCheck(string_1,string_2):
    count =0
    for i in range(len(string_1)):
        if string_1[i]==string_2[0]:
            if string_1[i:i+len(string_2)] == string_2:
               count+=1;
    return count
string_1 = input("string_1 = ")
string_2 = input("string_2 = ")
a = strCheck(string_1,string_2)
print("Here string_2 occur in string_1", a, "times")