# Step 1: Import the nltk library
import nltk

# Download required resources (Run only first time)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Step 2: Define a function for POS tagging
def pos_tagging(text):
    
    # Step 3a: Tokenize the input text into individual words
    words = nltk.word_tokenize(text)
    
    # Step 3b: Perform Part-of-Speech tagging
    pos_tags = nltk.pos_tag(words)
    
    # Step 3c: Return the tagged words
    return pos_tags


# Step 4: Define an example text
example_text = "Artificial Intelligence is transforming the world rapidly."

# Step 5: Call the function
pos_tags = pos_tagging(example_text)

# Step 6: Display the output
print("Input Sentence:", example_text)
print("\nPOS Tagging Output:\n")

for word, tag in pos_tags:
    print(f"{word} --> {tag}")
