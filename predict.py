import pickle

# Use the full path to the model
with open("/Users/jt-mac14/Downloads/percentage_classifier/model.pkl", "rb") as f:
    model = pickle.load(f)

sample_question = "How do I calculate profit percentage?"

predicted_class = model.predict([sample_question])[0]

print(f"Predicted category: {predicted_class}")
