#The following example shows how to estimate the number of documents in each category for the extracted text data from the previous example:


# Create a dictionary to store the number of documents in each category
category_counts = {}

for category in categories:
    category_counts[category] = 0

# Iterate over the extracted text data and count the number of documents in each category
for document in extracted_text_data:
    for category in categories:
        if category in document:
            category_counts[category] += 1

# Print the results
print(category_counts)

#output 
{'climate change': 8, 'heatwaves': 2, 'droughts```
