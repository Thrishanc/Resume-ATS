import streamlit as st
import os
import PyPDF2 as pdf
import json
import ollama

def get_ollama_response(prompt, model="llama3"):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Prompt Template
def build_prompt(resume_text, jd_text):
    return f"""
Act like a skilled ATS (Application Tracking System) with expertise in tech fields like software engineering, data science, analytics, and big data engineering. 

Evaluate the resume below based on the job description and provide:
- JD Match % (how well the resume matches)
- Missing important keywords
- A concise profile summary

Return ONLY valid JSON in the following format:
{{
  "JD Match": "<percentage as string>%",
  "MissingKeywords": [<list of missing keywords>],
  "Profile Summary": "<summary>"
}}

Resume:
{resume_text}

Job Description:
{jd_text}
"""

# Streamlit app
st.set_page_config(page_title="Smart ATS", layout="centered")
st.title("📄 Resume ATS (with LLaMA3)")
st.caption("Analyze and improve your resume using a free, private AI running locally on your machine.")

jd = st.text_area("📌 Paste the Job Description")
uploaded_file = st.file_uploader("📎 Upload Your Resume (PDF)", type="pdf", help="Upload only PDF files")

if st.button("🔍 Analyze Resume"):
    if uploaded_file is not None and jd.strip() != "":
        resume_text = input_pdf_text(uploaded_file)
        prompt = build_prompt(resume_text, jd)
        with st.spinner("🤖 Analyzing with LLaMA3..."):
            response = get_ollama_response(prompt)

        # Larger header for ATS Analysis Result
        st.markdown("<h2 style='margin-bottom: 20px;'>📊 ATS Analysis Result</h2>", unsafe_allow_html=True)

        try:
            # Extract JSON safely
            start = response.find("{")
            end = response.rfind("}") + 1
            json_part = response[start:end]
            ats_result = json.loads(json_part)

            # Larger label and value with emoji after
            st.markdown(f"<h3 style='margin-bottom: 0;'>Job Description Match 🔍</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#2E86C1;'>{ats_result.get('JD Match', 'N/A')}</h2>", unsafe_allow_html=True)

            # Highlight missing keywords with emoji after
            missing = ats_result.get("MissingKeywords", [])
            st.markdown("<h3 style='margin-top: 30px;'>Missing Keywords ❗</h3>", unsafe_allow_html=True)
            if missing:
                badges_html = " ".join([
                    f"<span style='background-color:#FF6347; color:white; padding:4px 10px; border-radius:12px; margin-right:6px; font-weight:bold;'>{kw}</span>"
                    for kw in missing
                ])
                st.markdown(badges_html, unsafe_allow_html=True)
            else:
                st.success("✅ No major missing keywords found!")

            # Profile Summary
            st.markdown("<h3 style='margin-top: 30px;'>Profile Summary 📄</h3>", unsafe_allow_html=True)
            st.info(ats_result.get("Profile Summary", "No summary provided."))

            # Download Button
            st.download_button("📥 Download Result", json.dumps(ats_result, indent=2), file_name="ats_result.json")

        except Exception as e:
            st.error("⚠️ Couldn't parse the ATS result properly. Showing raw output:")
            st.text(response)
    else:
        st.warning("⚠️ Please provide both a Job Description and a Resume.")