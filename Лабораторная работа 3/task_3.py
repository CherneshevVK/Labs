def count_letters(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower not in letter_counts:
                letter_counts[char_lower] = 1
            else:
                letter_counts[char_lower] += 1
    return letter_counts

def calculate_frequency(letter_counts):
    total_count = sum(letter_counts.values())
    letter_frequency = {}
    for letter, count in letter_counts.items():
        frequency = count / total_count
        letter_frequency[letter] = round(frequency, 2)
    return letter_frequency

text = "Тут должен быть какой-то текст"
letters = count_letters(text)
frequency = calculate_frequency(letters)

for letter, freq in frequency.items():
    print(letter, ":", freq)
