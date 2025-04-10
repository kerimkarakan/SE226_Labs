def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    words = s.split()
    
    capitalized_words = []
    
    for word in words:
        capitalized_word = word.capitalize()
        capitalized_words.append(capitalized_word)
    
    result = " ".join(capitalized_words)
    
    return result

def remove_punctuation(s):
    import string
    
    punctuation_chars = string.punctuation
    
    result = ""
    
    for char in s:
        if char not in punctuation_chars:
            result += char
    
    return result
