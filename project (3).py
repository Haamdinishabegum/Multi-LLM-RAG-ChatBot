import pandas as pd
import requests

API = "http://localhost:11434/api/generate"
MODEL1 = "llama3.2"
MODEL2 = "deepseek-r1"

df = pd.read_csv("DS_match.csv")
df.columns = df.columns.str.strip()

print("Dataset loaded:", df.shape)
print("Columns:", list(df.columns))

def send_request(model, prompt):
    try:
        res = requests.post(
            API,
            json={"model": model, "prompt": prompt, "stream": False}
        )
        return res.json().get("response", "")
    except:
        return ""

def create_prompt(question):
    return f"""
Convert this question into a SINGLE LINE pandas query.

DataFrame name: df

Columns:
{list(df.columns)}

Rules:
- Return only code
- No explanation
- No print
- No import

Question:
{question}
"""

def clean(text):
    return text.replace("```python", "").replace("```", "").strip()

def get_query(question):
    q = question.lower()

    if "home team" in q:
        return "df[['home_team_name']].head(5)", df[['home_team_name']].head(5)

    if "venue" in q:
        return "df[['venue_name']].head(5)", df[['venue_name']].head(5)

    if "result" in q:
        return "df[['result']].head(5)", df[['result']].head(5)

    if "salary" in q:
        return None, None

    prompt = create_prompt(question)

    q1 = clean(send_request(MODEL1, prompt))
    q2 = clean(send_request(MODEL2, prompt))

    for q in [q2, q1]:
        if "df" not in q:
            continue
        try:
            result = eval(q, {"__builtins__": {}}, {"df": df, "pd": pd})
            return q, result
        except:
            continue

    return None, None

def summarize(result):
    prompt = f"""
Summarize this result in ONE short sentence:

{result.to_string()}
"""
    return send_request(MODEL1, prompt)

def chatbot():
    print("\nMatch Dataset Chatbot")
    print("Using dual LLMs for query generation.\n")

    while True:
        user_input = input("Enter your question (or exit): ")

        if user_input.lower() == "exit":
            break

        query, result = get_query(user_input)

        if result is None:
            print("\nCould not generate valid query.\n")
            continue

        if hasattr(result, "__len__") and len(result) > 10:
            print("\nToo many results. Please refine your query.\n")
            continue

        print("\nQuery Used:\n", query)

        print("\nResult:\n")
        if hasattr(result, "head"):
            print(result.head())
        else:
            print(result)

        summary = summarize(result)

        print("\nSummary:\n", summary)

if __name__ == "__main__":
    chatbot()