from pathlib import Path
import pandas as pd

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

plan_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "housekeeping_plan.csv"
)

print("Housekeeping plan loaded.")
print(plan_df.shape)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

while True:

    question = input(
        "\nAsk Housekeeping Agent (type exit to quit): "
    )

    if question.lower() == "exit":
        break

    prompt = f"""
You are a hotel housekeeping manager.

Below is the housekeeping plan:

{plan_df.to_string()}

Answer the user's question using only the data provided.

Question:
{question}
"""

    response = llm.invoke(prompt)

    print("\nAGENT RESPONSE:\n")
    print(response.content)