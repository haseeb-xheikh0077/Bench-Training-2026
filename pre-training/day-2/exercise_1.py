from collections import defaultdict
import string

def word_frequency(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1
    return dict(freq)

paragraph = """
The quick brown fox jumps over the lazy dog. The dog barked loudly,
but the fox was already gone. A quick fox is hard to catch. The lazy
dog sat by the fence and watched the fox disappear into the forest.
The forest was dark and the trees were tall. The fox felt safe in the forest.
"""
freq = word_frequency(paragraph)
top_5 = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:5]
print("Top 5 most common words:")
for word, count in top_5:
    print(f"  {word!r}: {count}")
