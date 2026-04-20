import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required data (run once)
nltk.download('punkt')
nltk.download('stopwords')

text = input("Enter a paragraph: ")

# Tokenization
words = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w.lower() not in stop_words]

print("\nOriginal Words:")
print(words)

print("\nFiltered Words:")
print(filtered_words)
