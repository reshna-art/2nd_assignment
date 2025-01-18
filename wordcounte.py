#Word Frequency Counter with Counter: Given a paragraph, count the frequency of each word using Counter and display the top 3 most common words.

from collections import Counter
import re

def word_frequency_counter(paragraph):
    # Clean the paragraph (remove punctuation and convert to lowercase)
    cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph).lower()
    # Split the paragraph into words
    words = cleaned_paragraph.split()
    # Count the frequency of each word using Counter
    word_counts = Counter(words)
    # Get the top 3 most common words
    top_three = word_counts.most_common(3)
    return top_three

# Example paragraph
paragraph = """Data is the oil of the digital age. The ability to analyze data effectively 
               can transform businesses, create new opportunities, and solve complex problems."""
               
# Call the function and display the result
top_words = word_frequency_counter(paragraph)
print("Top 3 most common words:")
for word, count in top_words:
    print(f"{word}: {count}")
