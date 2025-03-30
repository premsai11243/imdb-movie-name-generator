import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import emoji

# Load the movie dataset (make sure your CSV has 'name' and 'story' columns)
csv_files = pd.read_csv("D:/Desktop/IMDB movies/main/original file.csv")  # Replace with your actual dataset

# Convert the movie storylines to TF-IDF vectors
tfidf_vectorizer = TfidfVectorizer(stop_words="english")
X_tfidf = tfidf_vectorizer.fit_transform(csv_files['story'])  # Use the 'story' column

# Streamlit UI
st.title("Movie Recommendation System Based on Storyline")

# User input: Allow users to enter a movie description (storyline)
user_story = st.text_area("Enter a movie storyline:")

if user_story:
    # Convert the user input into a TF-IDF vector
    user_tfidf = tfidf_vectorizer.transform([user_story])
    
    # Compute similarity between the user input and all movies in the dataset
    user_sim = cosine_similarity(user_tfidf, X_tfidf)
    
    # Get the top 5 most similar movies (excluding the input movie itself)
    similar_movie_indices = np.argsort(user_sim[0])[-6:-1]  # Get indices of top 5 similar movies

    
    # Display the top 5 recommended movies
    st.subheader("Top 5 Recommended Movies:")
    
    name=[]
    story=[]

    # Loop over the similar movie indices
    for idx in similar_movie_indices:
        # Display movie name and storyline
        st.write(f"Movie name :{csv_files['name'][idx]}")
        st.write(f"Storylines:{csv_files['story'][idx]}")  # Display stemmed storyline
        st.markdown("---")
        name.append(csv_files['name'][idx])
        story.append(user_sim[0][idx])   
        
    
    df_similar_movies = pd.DataFrame({"Movie": name, "Similarity Score": story})

    # Plot scatter chart
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df_similar_movies, x="Similarity Score", y="Movie", palette="coolwarm", ax=ax)
    ax.set_title("Similarity Scores of Recommended Movies")
    ax.set_xlabel("Similarity Score")
    ax.set_ylabel("Movie Name")
     
    st.pyplot(fig)     