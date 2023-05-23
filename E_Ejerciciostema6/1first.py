def count_letters(word,letter):
    counter = 0 
    for letters in word:
        if letters == letter:
            counter += 1 
    return(f"There are {counter} letters {letter} in the word {word}")

print(count_letters("banana", "a"))