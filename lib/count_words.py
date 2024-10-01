def count_words(string):
    if type(string)!= str:
        raise Exception("Input must be a string!")
    
    if string == "":
        return 0
    
    clean_string = ""
    for i in range(len(string) - 1):
        if string[i] == " " and string[i + 1] == " ":
            pass
        else:
            clean_string = clean_string + string[i]

    raw_words = clean_string.split(" ")
    clean_words = [word for word in raw_words if not word.isnumeric()]
    return len(clean_words)

print(count_words("Hello  my  friend  in  life  "))
 