import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def find_common_word_ml(csv_file, num_clusters=3):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Extract the text data from the DataFrame
    texts = df['text'].astype(str)

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    # Clustering using KMeans
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)

    # Get cluster centers and find the most common word in the cluster
    cluster_centers = kmeans.cluster_centers_.argsort()[:, ::-1]
    feature_names = vectorizer.get_feature_names_out()

    most_common_word = feature_names[cluster_centers[0, 0]]

    return most_common_word

# Example usage
csv_file_path = 'your_file.csv'  # Replace with your CSV file path
common_word_ml = find_common_word_ml(csv_file_path)
print(f"The most common word in the CSV file using machine learning is: {common_word_ml}")