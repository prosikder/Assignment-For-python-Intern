def anumeric(st):
    word = st.split()
    l = []
    for i in word:
        if not i.isalpha() and not i.isnumeric() and i.isalnum():
            l.append(i)
    return l
print(anumeric("prokash this2 value is5 alphanumaric and 123 &h12"))