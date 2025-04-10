from string_package import reverse_string, capitalize_words, remove_punctuation, count_characters, count_words, average_word_length


user_sentence = input("Enter a sentence: ")

reversed_sentence = reverse_string(user_sentence)
print(reversed_sentence)

capitalized_sentence = capitalize_words(user_sentence)
print(capitalized_sentence)

removed_punctuation_sentence = remove_punctuation(user_sentence)
print(removed_punctuation_sentence)

counted_characters = count_characters(user_sentence)
print(f"Character count in the sentence: {counted_characters}")

counted_words = count_words(user_sentence)
print(f"Word count in the sentence: {counted_words}")

average_word_lenght_value = average_word_length(user_sentence)
print(average_word_lenght_value)







