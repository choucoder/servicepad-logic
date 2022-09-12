import string

def frequency_counter(text: str):
    freq = {}

    for _ in string.punctuation:
        text = text.replace(_, '')
    
    text = [s.lower() for s in text.split()]

    for word in text:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    return freq


if __name__ == '__main__':
    text = "Hi how are things? How are you? Are you a developer? I am also a developer"
    freq = frequency_counter(text)
    
    for word, n in freq.items():
        print(f"{word}: {n}")