# Housekeeping-Allocation-Agent

# AI Housekeeping Allocation Agent Using Agentic AI

An Agentic AI-based hotel housekeeping assistant that generates a housekeeping allocation plan and allows users to ask natural-language questions about the plan.

**Project ID:** PS268  
**Domain:** Travel, Hospitality & Aviation  
**Program:** NVIDIA × Dayananda Sagar University – RTD 2026 GenAI & LLM Boot Camp

---

## 1. Project Overview

The system automates hotel housekeeping task allocation using room checkout time, housekeeping priority, and a predefined housekeeping staff pool.

The project has two main parts:

1. **Housekeeping Allocation Engine**  
   Reads the processed hotel dataset, selects rooms with `Dirty` status, prioritizes them, assigns housekeeping staff, and generates `housekeeping_plan.csv`.

2. **Agentic AI Assistant**  
   Uses Google's Gemini model through LangChain to answer natural-language questions using the generated housekeeping plan.

A Gradio web interface is provided for interacting with the AI assistant.

---

## 2. Key Features

- Automated housekeeping room allocation
- Priority-based room scheduling
- Checkout-time-based ordering
- Staff assignment across a predefined housekeeping team
- Pending task tracking
- Estimated room completion time
- Natural-language querying using Gemini
- Gradio-based web interface
- CSV-based data pipeline

---

## 3. Project Structure

```text
Housekeeping Agent (RTD project)/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│   └── processed/
│       ├── housekeeping_dataset.csv
│       └── housekeeping_plan.csv
│
├── src/
│   ├── agent.py
│   └── allocation.py
│
└── notebooks/
    └── data_cleaning.ipynb
```

### Important files

| File | Purpose |
|---|---|
| `app.py` | Launches the Gradio web application |
| `src/allocation.py` | Generates the housekeeping allocation plan |
| `src/agent.py` | Runs the AI assistant in the terminal |
| `data/processed/housekeeping_dataset.csv` | Processed input dataset |
| `data/processed/housekeeping_plan.csv` | Generated housekeeping schedule |
| `requirements.txt` | Python dependencies |
| `.env` | Stores the Gemini API key locally |

---

# 4. Requirements

Before starting, install:

- Python 3.11+ recommended
- Git
- Internet connection
- A Google Gemini API key

The application uses:

- Python
- Pandas
- NumPy
- Gradio
- LangChain
- `langchain-google-genai`
- `python-dotenv`

---

# 5. Clone the Repository

Open a terminal or PowerShell and run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then enter the project directory:

```bash
cd "Housekeeping Agent (RTD project)"
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual GitHub repository URL.

---

# 6. Create a Virtual Environment

Creating a virtual environment keeps the project dependencies isolated from other Python projects.

### Windows PowerShell

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, your terminal should show something similar to:

```text
(.venv)
```

---

# 7. Install Dependencies

Make sure the virtual environment is activated.

Then run:

```bash
python -m pip install --upgrade pip
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

This may take a few minutes.

---

# 8. Configure the Gemini API Key

The AI assistant uses Google's Gemini model.

Create a file named:

```text
.env
```

in the project root, at the same level as `app.py`.

Add:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your own API key.

### Important security note

**Never upload your real `.env` file or API key to GitHub.**

Add `.env` to `.gitignore`:

```gitignore
.env
.venv/
venv/
__pycache__/
.gradio/
```

If an API key has already been uploaded publicly, revoke/rotate that key and create a new one before publishing the repository.

---

# 9. Generate the Housekeeping Plan

The project already contains a generated:

```text
data/processed/housekeeping_plan.csv
```

However, if you want to regenerate it from the processed dataset, run this command from the project root:

```bash
python src/allocation.py
```

The script:

1. Loads `housekeeping_dataset.csv`
2. Selects rooms whose status is `Dirty`
3. Converts priority levels into priority scores
4. Sorts rooms by:
   - Priority
   - Checkout hour
5. Assigns rooms to housekeeping staff
6. Adds task status
7. Calculates an estimated finish hour
8. Saves the result to:

```text
data/processed/housekeeping_plan.csv
```

The generated plan contains:

```text
room_id
hotel_name
priority
checkout_hour
assigned_staff
task_status
estimated_finish_hour
```

---

# 10. Run the AI Assistant in the Terminal

From the project root:

```bash
python src/agent.py
```

You should see:

```text
Housekeeping plan loaded.
```

Then the program will ask:

```text
Ask Housekeeping Agent (type exit to quit):
```

Example questions:

```text
Which rooms should be cleaned first?
```

```text
Show all high priority rooms.
```

```text
Which staff member is assigned to room 1784?
```

```text
Which rooms have the earliest checkout time?
```

To stop the assistant:

```text
exit
```

---

# 11. Run the Gradio Web Application

The recommended way to use the project is through the Gradio interface.

From the project root:

```bash
python app.py
```

The application will start locally.

You should see a local URL similar to:

```text
http://127.0.0.1:7860
```

Open that URL in your browser.

You will see the:

**AI Housekeeping Agent**

interface with a text box where you can ask questions about the housekeeping plan.

---

# 12. Example Queries

Try questions such as:

### Priority

```text
Which rooms should be cleaned first today?
```

### Staff assignment

```text
Who is assigned to room 1784?
```

### Hotel

```text
Which rooms in InterContinental Singapore have high priority?
```

### Checkout

```text
Which rooms have the earliest checkout hour?
```

### Staff workload

```text
Show the rooms assigned to Alice.
```

### Combined reasoning

```text
Which high-priority rooms have the earliest checkout time and who are they assigned to?
```

---

# 13. How the Allocation Logic Works

The allocation engine first identifies rooms requiring housekeeping:

```python
df["room_status"] == "Dirty"
```

Priority is converted into numerical scores:

```text
High   → 3
Medium → 2
Low    → 1
```

Rooms are then sorted by:

```text
1. Priority score — highest first
2. Checkout hour — earliest first
```

The system then cycles through the housekeeping staff:

```text
Alice
Bob
Charlie
David
Emma
Frank
Grace
Henry
Ivy
Jack
```

Each generated task is marked:

```text
task_status = Pending
```

and the estimated finish time is calculated from the checkout hour.

---

# 14. How the AI Assistant Works

The Gradio application loads:

```text
data/processed/housekeeping_plan.csv
```

The housekeeping plan is inserted into the prompt sent to Gemini.

The user asks a natural-language question.

The Gemini model receives:

- The role of a hotel housekeeping manager
- The available housekeeping plan
- The user's question

The model then generates a response based on the supplied plan.

The application uses:

```text
Gemini 2.5 Flash
```

through:

```text
LangChain
```

and:

```text
langchain-google-genai
```

---

# 15. End-to-End Workflow

```text
Processed Hotel Dataset
          ↓
   allocation.py
          ↓
Priority + Checkout Sorting
          ↓
   Staff Assignment
          ↓
housekeeping_plan.csv
          ↓
      app.py
          ↓
     Gemini 2.5 Flash
          ↓
 Natural-Language Questions
          ↓
   Housekeeping Answers
```

---

# 16. Troubleshooting

## `ModuleNotFoundError`

If you see:

```text
ModuleNotFoundError
```

make sure the virtual environment is activated and run:

```bash
pip install -r requirements.txt
```

---

## Gemini API error

Check that `.env` exists in the project root:

```text
Housekeeping Agent (RTD project)/
├── app.py
├── .env
└── ...
```

The file should contain:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Make sure the API key is valid.

---

## Gradio does not start

Try:

```bash
python -m pip install --upgrade gradio
```

Then:

```bash
python app.py
```

---

## Housekeeping plan not found

Make sure this file exists:

```text
data/processed/housekeeping_plan.csv
```

If it does not exist, run:

```bash
python src/allocation.py
```

---

## Wrong file/path errors

Always run commands from the project root:

```text
Housekeeping Agent (RTD project)
```

For example:

```bash
python src/allocation.py
```

not from inside the `src` directory.

---

# 17. Notes for Developers

The current implementation is a prototype designed for demonstrating Agentic AI-based housekeeping decision support.

The allocation engine currently uses a deterministic priority and checkout-time sorting strategy, while Gemini provides the natural-language decision-support interface.

For production deployment, the system could be extended with:

- Real-time hotel management system integration
- Live staff availability
- Staff skill/capability matching
- Room location optimization
- Dynamic task reassignment
- Real-time task status updates
- Database integration
- Authentication and role-based access
- Monitoring and logging
- Production-grade API deployment

---

# 18. Project Information

**Project:** AI Housekeeping Allocation Agent Using Agentic AI  
**Project ID:** PS268  
**Domain:** Travel, Hospitality & Aviation  
**Program:** NVIDIA × Dayananda Sagar University – RTD 2026 GenAI & LLM Boot Camp

---

## Author

**Akkikhebbal Bhargava Surya**  
ENG23AM0104

**Project Guide:**  
Dr. Bahubali Shiragpur  
Department of Artificial Intelligence & Machine Learning  
Dayananda Sagar University
