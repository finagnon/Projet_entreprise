from transformers import BertTokenizer, BertForSequenceClassification

# Charger le tokenizer et le modèle pré-entraîné
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=1)  # 1 classe pour la sémantique politique

# Prétraitement du texte
text = "Votre texte à analyser"
inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")

# Faire la prédiction
outputs = model(**inputs)
predictions = outputs.logits.sigmoid().item()  # Utiliser la fonction sigmoid pour obtenir une probabilité entre 0 et 1

# Définir un seuil pour décider si la sémantique est politique ou non
seuil = 0.5
if predictions >= seuil:
    print("Le texte contient une sémantique politique.")
else:
    print("Le texte ne contient pas de sémantique politique.")
