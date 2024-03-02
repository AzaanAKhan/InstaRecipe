import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def find_common_word_ml(csv_file, num_clusters=3):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Extract the text data from the first (and only) column
    texts = df.iloc[:, 0].astype(str)

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    # Clustering using KMeans
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)

    # Sum TF-IDF values for each term across all documents
    term_sums = X.sum(axis=0)

    # Get the index of the term with the highest sum
    most_common_index = term_sums.argmax()

    # Get the corresponding term from the feature names
    feature_names = vectorizer.get_feature_names_out()
    most_common_word = feature_names[most_common_index]

    return most_common_word

# Example usage
csv_file_path = '/Users/rishansubagar/Desktop/InstaRecipe/coke.csv'  # Replace with your CSV file path
common_word_ml = find_common_word_ml(csv_file_path)
print(f"The most common word in the CSV file using machine learning is: {common_word_ml}")