# 💼 Smart Resume ATS (Local & Free with LLaMA3)

> A privacy-first resume analysis tool powered by a local LLM (LLaMA3) and built with Streamlit.

---

## 🚀 Features

- ✅ **Local AI-Powered Evaluation** (via [Ollama](https://ollama.com/))
- 📄 **Resume Parsing from PDF**
- 🔍 **Job Description Matching Percentage**
- ❗ **Missing Keywords Detection**
- 📄 **Profile Summary Generation**
- 🧠 **100% Offline** – No external APIs or data leaks

---

## 📸 Preview

![App Preview](assets/preview.png)

After launching the app, you’ll see a simple interface:
- 📌 **Paste the Job Description** into the text area.
- 📎 **Upload your resume** (PDF format only).
- Click **🔍 Analyze Resume** to evaluate your resume against the job description.

The app runs fully locally using LLaMA3 via Ollama and processes the input in real-time.

---

## 🛠️ Tech Stack

- 🐍 Python 3.10+
- 🦙 [Ollama](https://ollama.com/) + LLaMA3
- 📚 PyPDF2
- 🌐 Streamlit

---

## 🧾 Sample Output

![Sample Output](assets/output.png)

Once analyzed, the tool will show:
- 🔍 **Job Description Match** – how well your resume aligns with the job description (in %).
- ❗ **Missing Keywords** – important terms or skills missing in your resume that appear in the job description.
- 📄 **Profile Summary** – a short AI-generated overview of your profile strengths and gaps.

You can also expand/collapse sections and **download the analysis as a `.json`** file.

---

## 🧪 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Thrishanc/Resume-ATS.git
cd Resume-ATS
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install and run LLaMA3 locally with Ollama
```bash
# Download the model (one time)
ollama run llama3
```

### 5. Run the Streamlit app
```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
Resume-ATS/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md             # You're here!
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ by [Thrishanc](https://github.com/Thrishanc)

---

> If you like this project, please ⭐ star the repo and feel free to contribute or fork it!
