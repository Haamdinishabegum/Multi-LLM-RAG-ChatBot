**Introduction:**

The Multi-LLM Match Dataset Chatbot is a Python-based project that uses Large Language Models (LLMs) to answer natural-language questions about a structured match dataset.

The chatbot converts user questions into executable Pandas queries, retrieves relevant information from the dataset, and generates short summaries of the results. It uses Llama 3.2 and DeepSeek-R1 through Ollama to improve query generation reliability.

**Features:**

1.Natural Language Querying: Ask questions about the match dataset using everyday language.

2.Multiple LLMs: Uses Llama 3.2 and DeepSeek-R1 to generate Pandas queries.

3.Rule-Based Fallback: Uses predefined queries for common questions about home teams, venues, and results.

4.Query Validation: Attempts to execute generated queries and handles invalid queries.

5.Result Display: Displays retrieved data in a readable tabular format.

6.AI-Generated Summaries: Produces short summaries of query results.

7.Automated Testing: Includes test cases for valid questions and invalid dataset columns.

**Technologies Used:**

-Python

-Pandas

-Ollama

-Llama 3.2

-DeepSeek-R1

-Requests

**Requirements:**

--Before running the project, make sure you have:

--Python 3.10 or a compatible Python version

--Ollama installed and running

--The Llama 3.2 and DeepSeek-R1 models downloaded

--The required Python libraries installed

**Installation and Setup:**

1. Clone the repository:
   git clone https://github.com/Haamdinishabegum/Multi-LLM-RAG-ChatBot

2. Install the required libraries

python -m pip install pandas requests

3. Install and download the Ollama models

Install Ollama from https://ollama.com.

Download the required models by running:

ollama pull llama3.2
ollama pull deepseek-r1

4. Start Ollama

Make sure the Ollama service is running. On systems where it is not already running automatically, execute:

ollama serve

If Ollama is already running, you do not need to start it again.

5. Run the chatbot

Ensure that project.py and DS_match.csv are in the same directory. Then run:

python project.py

**How It Works:**

1.Dataset Loading: Pandas loads the match dataset from DS_match.csv.

2.Data Preparation: Whitespace is removed from column names.

3.Query Generation: Llama 3.2 and DeepSeek-R1 generate Pandas queries for general questions.

4.Fallback Logic: Predefined queries handle selected common questions.

5.Query Execution: The program attempts to execute generated queries against the dataset.

6.Result Summarization: Llama 3.2 generates a short summary of the retrieved results.
