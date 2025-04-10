def count_characters(s):
    return len(s)

def count_words(s):
    words = s.split()
    return len(words)

def average_word_length(s):
    words = s.split()
    
    if len(words) == 0:
        return 0
    
    total_characters = 0
    for word in words:
        total_characters += len(word)
    
    average = total_characters / len(words)

    return average
