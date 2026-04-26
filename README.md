# Resume_analyser


# Local AI Resume Analyzer using Ollama (LLaMA3)

This project is a simple AI-powered Resume Analyzer that runs completely **locally** using **Ollama (LLaMA3)**.

It reads a resume PDF, extracts text, and uses a locally running LLM to analyze:
- Key skills & strengths
- Suitable job roles
- Weak areas / improvements

⚡ No cloud APIs  
🔒 Fully private  
💻 Runs locally  

---

## 📌 Features

- 📄 Extracts text from PDF resumes
- 🤖 Uses LLaMA3 via Ollama (local LLM)
- 📊 Generates structured analysis:
  - Skills
  - Job roles
  - Improvements
- ⚡ Fast and offline execution

---

## 🛠️ Tech Stack

- Python  
- PyPDF2  
- Requests  
- Ollama (LLaMA3)  

---

## ⚙️ Setup Instructions

### 🔹 Step 1: Install Python

Check if Python is installed:

```bash
python --version


🔹 Step 2: Install Required Libraries
pip install PyPDF2 requests


🔹 Step 3: Install Ollama

Download and install Ollama:

👉 https://ollama.com

🔹 Step 4: Pull LLaMA3 Model
ollama pull llama3


🔹 Step 5: Run Ollama
ollama run llama3

This starts the local server at:

http://localhost:11434


▶️ How the Project Works
Step 1: Provide Resume Path

Update this in main.py:

"resume_path": "path_to_your_resume.pdf"


Step 2: Extract Resume Text
Uses PyPDF2 to read PDF
Converts resume into text


Step 3: Send Data to Local LLM
Sends resume text to Ollama API:
http://localhost:11434/api/generate


Step 4: AI Processing
LLaMA3 analyzes resume
Generates:
Skills
Job roles
Improvements


Step 5: Output
Results printed in terminal
▶️ Run the Project
python main.py


📂 Project Structure
resume_analysis_agent/
│── main.py
│── README.md
│── resume.pdf


🧠 Example Output
Key Skills:
- Machine Learning
- Python
- Computer Vision

Job Roles:
- AI/ML Engineer
- Data Scientist

Weak Areas:
- Improve project descriptions
- Add impact metrics
🔥 Why This Project?
Uses Local LLM (Ollama)
No API cost
Fully offline & private
Real-world AI use case
🚀 Future Improvements
Add UI (Streamlit/Flask)
Resume scoring system
ATS keyword matching
Multiple resume comparison
🤝 Contributing

Feel free to fork and improve!

⭐ Support

If you like this project, give it a ⭐ on GitHub!


---
 

---

If you want, I can next:
✅ Give you **perfect GitHub description + tags**  
✅ OR help you make **UI version (next level project)** 🚀
