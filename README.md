# Book Recommendation System  
A **Content-Based Recommendation System** built using Python that suggests books to users based on their description. The system utilizes a **Bag of Words (BoW)** model and **cosine similarity** to find books similar to the one selected by the user. The project also includes a **Streamlit-based web application** to provide an interactive interface for recommendations.  

## Features  
1. **Content-Based Filtering**: Recommends books based on textual descriptions.  
2. **Bag of Words Model**: Represents the text data.  
3. **Cosine Similarity**: Measures the similarity between book descriptions.  
4. **Streamlit Application**: Provides an easy-to-use web interface.  

---

## Methodology  

### 1. Data Preparation  
- Collect a dataset containing books and their descriptions.  
- Preprocess the text data by:  
  - Removing stop words.  
  - Tokenizing the text.  
  - Stemming/lemmatizing (if required).  

### 2. Bag of Words Model  
The **Bag of Words (BoW)** model is created to represent the textual data. This involves:  
BoW Vector = [Frequency of Term 1, Frequency of Term 2, ..., Frequency of Term N]  
Where N is the size of the vocabulary.  

### 3. Cosine Similarity  
To measure the similarity between book descriptions, we calculate cosine similarity:  
Cosine Similarity = (A · B) / (||A|| ||B||)  
Where:  
- A and B are BoW vectors of two book descriptions.  
- ||A|| and ||B|| are the magnitudes of the vectors.  

### 4. Recommendation Process  
- Compute the cosine similarity between the user's selected book and all other books.  
- Rank the books based on similarity scores.  
- Display the top k recommendations to the user.  

---

## Web Application (Streamlit)  

### Home Page  
- Displays the list of available books for selection.  
- Allows users to choose a book to get recommendations.  

### Recommendation Page  
- Shows the top k books similar to the selected book.  
- Displays similarity scores alongside recommendations.  

---

## Installation  

### Prerequisites  
- Python 3.10 or above  
- Required Python libraries:  
  pip install streamlit pandas scikit-learn numpy  

### Running the Application  
1. Clone the repository:  
   git clone https://github.com/Srujanrana07/book-recomender-system.git  
2. Run the Streamlit app:  
   streamlit run app.py  

---

## Example Workflow  

1. User selects a book (e.g., "The Hobbit").  
2. System processes the description and computes cosine similarity.  
3. Recommended books based on similarity are displayed:  
   - "The Lord of the Rings"  
   - "Harry Potter and the Sorcerer's Stone"  
   - "Percy Jackson & The Olympians"  

---

## Mathematical Insights  

### Text Representation (BoW):  
Vector for "The Hobbit" = [1, 2, 0, ..., 1]  
Where each element represents the frequency of a specific word.

### Cosine Similarity Calculation Example:  
A = [1, 2, 1], B = [2, 1, 3]  
Cosine Similarity = ((1*2) + (2*1) + (1*3)) / sqrt(1^2 + 2^2 + 1^2) * sqrt(2^2 + 1^2 + 3^2) = 0.89  

---

## Future Improvements  
1. Incorporate user feedback for better personalization.  
2. Extend to hybrid recommendation systems.  
3. Use advanced NLP techniques like **TF-IDF** or **word embeddings** for better text representation.  

---

## License  
This project is licensed under the MIT License.  

---
## Live Demo
[Live Demo](https://books-by-srujan0.streamlit.app/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen)](https://books-by-srujan0.streamlit.app/)

