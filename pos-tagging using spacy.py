# Step 1: Install spaCy (Run in terminal first time)
# pip install spacy
# python -m spacy download en_core_web_sm

# Step 2: Import spaCy
import spacy

# Step 3: Load English language model
nlp = spacy.load("en_core_web_sm")

# Step 4: Define example text
text = "Machine learning models are improving healthcare systems worldwide."

# Step 5: Process the text
doc = nlp(text)

# Step 6: Print each word with its POS tag
print("Input Sentence:", text)
print("\nPOS Tagging Output:\n")

for token in doc:
    print(token.text, "-->", token.pos_)