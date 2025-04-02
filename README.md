#  IMDb Movie Recommendation System  

##  Overview  
This project is an **IMDb Movie Recommendation System** that suggests movies based on their textual descriptions using **Natural Language Processing (NLP)** and **Machine Learning** techniques. 

## Libraries used
<a href="https://selenium.dev/documentation/" target="_blank"><b>Selenium</b></a><br>
<a href="https://pandas.pydata.org/docs/" target="_blank"><b>Pandas</b></a><br>
<a href="https://numpy.org/doc/stable/" target="_blank"><b>NumPy</b></a><br>
<a href="https://www.nltk.org/" target="_blank"><b>NLTK</b></a><br>
<a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html" target="_blank"><b>TF-IDF Vectorizer (Scikit-learn)</b></a><br>

##  Dataset Collection  
- **Tools Used:** Selenium, Pandas  
- **Approach:**  
  - Scraped IMDb movie data based on genres.  
  - Extracted movie details using **tag names** and **class names** in Selenium.  
  - Converted extracted data into a Pandas DataFrame (`pd.DataFrame()`).  
  - Added a **"genre" column** for better categorization.  
  - Saved all movie data into a single `.csv` file.  

##  Text Preprocessing  
- **Tools Used:** NLTK, SpaCy  
- **Steps:**  
  - Removed **numbers, symbols, and special characters**.  
  - **Stopword removal** (e.g., "the", "is", "and").  
  - **Stemming/Lemmatization** to reduce words to their root forms.  
  - Converted all text to **lowercase** for consistency.  

##  Text Representation (Feature Engineering)  
- **TF-IDF Vectorizer** (from Scikit-learn)  
  - Converts movie descriptions into numerical values.  
  - Assigns **higher importance to unique words** in descriptions.  
- **PCA (Dimensionality Reduction)**  
  - Used **Principal Component Analysis (PCA)** to reduce feature space for better visualization.  

##  Similarity Check  
- **Cosine Similarity**  
  - Measures similarity between movies based on their textual descriptions.  
  - Finds the **most relevant** movies for recommendations.  

##  Deployment on streamlit 

https://github.com/user-attachments/assets/9c0a8083-8f01-4835-88e3-35d666608301

