from sentence_transformers import SentenceTransformer
import joblib

#We're loading models outside the function because we need them loaded only once not every time using function
# Load the SentenceTransformer model for embeddings
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')
# Load the saved classification model
classifier_model = joblib.load('models/log_classifier.joblib')


def classify_with_bert(log_message):
    # compute embeddings for the log_message
    message_embedding = transformer_model.encode(log_message)
    probabilities = classifier_model.predict_proba([message_embedding])[0]

    # Predict the log_message category (we're putting a threshold to be based on it)
    if max(probabilities) < 0.3:
        return "Unclassified"

    predicted_label = classifier_model.predict([message_embedding])[0]
    return predicted_label

if __name__ == "__main__":
    logs = [
        "GET /v1/resource HTTP/1.1 200 OK",
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "GET / v2 / [\w]+/servers/detail HTTP/1\.1 RCODE\s+200len:(\d+)\s+time:(\d+\.\d+)",
        "System crashed due to drivers errors when restarting the server",
        "Test none",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer",
        "Firewall rule added: Restrict traffic to IP [\w]+"
    ]
    for log in logs:
        label = classify_with_bert(log)
        print(log, "->", label)