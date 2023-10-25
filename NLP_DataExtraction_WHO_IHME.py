#The following example shows how to extract and classify unstructured text data from the WHO, IHME dataset using spaCy

import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Preprocess the data
text = "Climate change is a major threat to human health. Heatwaves, droughts, floods, storms, air pollution, sea level rise, vector-borne diseases, and food insecurity are all linked to climate change."
text = text.lower()
text = text.strip()

# Tokenize the data
tokens = nlp(text)

# Lemmatize the data
lemmatized_tokens = [token.lemma_ for token in tokens]

# Tag the data
tagged_tokens = nlp.tag(lemmatized_tokens)

# Classify the data
categories = []
for token in tagged_tokens:
    if token.pos_ == "NOUN":
        categories.append(token.text)

# Print the results
print(categories)

# output 
['climate change', 'heatwaves', 'droughts', 'floods', 'storms', 'air pollution', 'sea level rise', 'vector-borne diseases', 'food insecurity']

