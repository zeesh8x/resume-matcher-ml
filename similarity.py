# similarity.py

from sentence_transformers import SentenceTransformer, util

# Load pre-trained model (downloads first time)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2') 

def calculate_similarity(text1, text2):
    # Create embeddings
    embedding1 = model.encode(text1, convert_to_tensor=True)
    embedding2 = model.encode(text2, convert_to_tensor=True)
    
    # Compute cosine similarity
    cosine_score = util.pytorch_cos_sim(embedding1, embedding2)
    return cosine_score.item()  # Get float value
