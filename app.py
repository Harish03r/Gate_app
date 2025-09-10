import streamlit as st
from qa import ask_gemini
from test_engine import generate_test, evaluate_test
from progress_tracker import log_result,analyze_progress

st.sidebar.title("📘 GATE Tutor")
choice = st.sidebar.radio("Navigation", ["Exam Info", "Q&A", "Take Test", "Progress Report", "Past Tests"])

if choice == "Exam Info":
    st.header("📘 About GATE Exam")
    st.write("""
    - Duration: 3 hours  
    - Total: 65 questions, 100 marks  
    - Sections: Aptitude (15), Core (85)  
    - Negative Marking applies for MCQs  
    """)

elif choice == "Q&A":
    st.header("Ask a Question")
    if "last_answer" not in st.session_state:
        st.session_state.last_answer = ""
    q = st.text_input("Enter your GATE question:")
    if st.button("Get Answer"):
        ans = ask_gemini(q)
        st.session_state.last_answer=ans
        st.success(ans)
    
    follow = st.text_input("Clarify Doubt:")
    if st.button("Clarify"):
        if st.session_state.last_answer:
            ans2 = ask_gemini(follow, context=st.session_state.last_answer)
            st.info(ans2)
        else:
            st.warning("⚠️ Please ask a main question first before clarifying doubts.")

elif choice == "Take Test":
    st.header("GATE Mock Test")
    test = generate_test(5)  # for demo, 65 for full test
    responses = []
    for q in test:
        st.write(q["question"])
        ans = st.text_input(f"Answer for Q{q['id']}")
        q["user_answer"] = ans
        responses.append(q)

    if st.button("Submit Test"):
        score, details = evaluate_test(responses)
        st.success(f"Your Score: {score}/100")
        log_result("Mock Test", score, details)

elif choice == "Progress Report":
    st.header("Your Progress")
    report = analyze_progress()
    st.write(report)

elif choice == "Past Tests":
    st.header("Past Test Records")
    st.dataframe(analyze_progress()["history"])
