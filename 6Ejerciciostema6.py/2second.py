def count(word,letter):
    x = [letters for letters in word]
    x = x.count(letter)
    return(f"There are {x} letters {letter} in the word {word}")

print(count("ornitorrinco", "i"))
        
        