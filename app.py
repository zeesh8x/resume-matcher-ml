import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from parser import extract_text_from_pdf
from preprocess import preprocess
from similarity import calculate_similarity
from keyword_matcher import keyword_match

st.set_page_config(page_title="Resume Matcher", page_icon="📝", layout="wide")
st.title("📝 Resume Matcher")

resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste the job description here")

if st.button("Match Now", key="match_button"):
    if not resume_file or not job_desc.strip():
        st.warning("Please upload a resume and enter a job description.")
    else:
        with st.spinner("🔍 Analyzing..."):
            resume_text = extract_text_from_pdf(resume_file)
            clean_resume = preprocess(resume_text)
            clean_job = preprocess(job_desc)

            # Similarity Score
            score = calculate_similarity(clean_resume, clean_job)
            st.subheader(f"📊 Similarity score: {score*100:.2f}%")

            # Keyword Matching
            matched, missing = keyword_match(resume_text, job_desc)
            st.subheader("✅ Matched Keywords")
            st.write(", ".join(matched) if matched else "None")

            st.subheader("❌ Missing Keywords")
            st.write(", ".join(missing) if missing else "None")

            # 🎯 Visual Summary Layout
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🔵 Pie Chart - Keyword Coverage")
                fig1, ax1 = plt.subplots()
                ax1.pie(
                    [len(matched), len(missing)],
                    labels=["Matched", "Missing"],
                    colors=["green", "red"],
                    autopct="%1.1f%%",
                    startangle=140,
                )
                ax1.axis("equal")
                st.pyplot(fig1)

            with col2:
                st.markdown("### ☁️ Word Cloud - Resume Keywords")
                wordcloud = WordCloud(width=600, height=400, background_color="white").generate(clean_resume)
                fig2, ax2 = plt.subplots()
                ax2.imshow(wordcloud, interpolation="bilinear")
                ax2.axis("off")
                st.pyplot(fig2)

            # 💡 Improvement Tips
            st.subheader("💡 Improvement Tips")
            if missing:
                st.info(f"Your resume is missing **{len(missing)}** important keywords.")
                st.write("Consider adding or emphasizing these:")
                st.markdown(", ".join(missing[:10]))
            else:
                st.success("🎉 Your resume includes all key terms from the job description!")

