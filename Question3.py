import re
from collections import defaultdict

def word_frequency(sentence):
    # Convert the sentence to lowercase and split into words
    words = re.findall(r'\w+', sentence.lower())
    
    # Count word frequency using a defaultdict
    frequency = defaultdict(int)
    for word in words:
        frequency[word] += 1
    
    return dict(frequency)

# Sample input
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
