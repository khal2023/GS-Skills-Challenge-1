def make_snippet(string):
    words = string.split(" ")
    snippet = " ".join(words[0:5])
    if len(words) > 5:
        return snippet + "..."
    else: 
        return snippet
