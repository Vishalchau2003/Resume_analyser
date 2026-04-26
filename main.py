import json
import PyPDF2
import requests

CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "resume_path": r"C:\Users\Vishal\Desktop\RESUME\new.pdf"
,  # Your resume
    "ollama_url": "http://localhost:11434/api/generate",  # Ollama endpoint
    "model": "llama3"
}

def read_resume(path):
    """Extract text from PDF resume"""
    text = ""
    try:
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        text = f"Error reading resume: {e}"
    return text.strip()

def analyze_resume_with_ollama(resume_text):
    """Send resume to local Ollama Llama3 and get analysis"""
    prompt = f"""
You are a resume screening agent. Analyze the following resume and provide:
1. Key skills and strengths
2. Possible job roles suitable
3. Weak areas or improvements needed

Resume:
{resume_text}
"""
    try:
        response = requests.post(
            CONFIG["ollama_url"],
            json={"model": CONFIG["model"], "prompt": prompt},
            stream=True
        )

        result = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    result += data["response"]

        return result.strip()
    except Exception as e:
        return f"Error connecting to Ollama: {e}"

if __name__ == "__main__":
    print(json.dumps(CONFIG, indent=2))

    # Step 1: Read resume
    resume_text = read_resume(CONFIG["resume_path"])
    if not resume_text:
        print("⚠️ No text extracted from resume.")
    else:
        print("\n📄 Resume loaded successfully. Sending to Ollama...\n")

        # Step 2: Analyze with Ollama
        analysis = analyze_resume_with_ollama(resume_text)
        print("\n📝 Resume Analysis Result:\n")
        print(analysis)






