from pathlib import Path
import pandas as pd
import gradio as gr

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

plan_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "housekeeping_plan.csv"
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def ask_agent(question):

    prompt = f"""
You are a hotel housekeeping manager.

Below is the housekeeping plan:

{plan_df.head(500).to_string()}

Answer the user's question using only the data.

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content

demo = gr.Interface(
    fn=ask_agent,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask housekeeping questions..."
    ),
    outputs="text",
    title="AI Housekeeping Agent",
    description="Hotel housekeeping assistant powered by Gemini"
)

demo.launch()