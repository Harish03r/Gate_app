import json
import google.generativeai as genai

# =========================



# 1. Load your dataset
# =========================
def load_dataset(path="C:\\Users\\sathi\\tutor_app"):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

# =========================
# 2. Configure Gemini
# =========================
genai.configure(api_key="AIzaSyDEhseO5PfFX4626xIBoirhPrJKwwpTqnI")   # 🔑 replace with your API key

model = genai.GenerativeModel("gemini-1.5-flash")  # small + fast model

# =========================
# 3. Query Gemini
# =========================
def ask_gemini(question,context=None):
    prompt = question
    if context:
        prompt = f"{context}\n\nFollow-up: {question}"
    response = model.generate_content(question)
    return response.text

# =========================
# 4. Test Run
# =========================
if __name__ == "__main__":
    dataset = load_dataset("dataset.jsonl")
    print(f"Loaded {len(dataset)} Q&As from dataset.jsonl")

    # Example: take first question from dataset
    sample_q = dataset[0]["question"]
    correct_a = dataset[0]["answer"]

    print("\n🔹 Question:", sample_q)
    print("✅ Correct Answer:", correct_a)

    gemini_answer = ask_gemini(sample_q)
    print("🤖 Gemini Answer:", gemini_answer)
