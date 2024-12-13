import streamlit as st
import random
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "options": ["90 degrees Celsius", "100 degrees Celsius", "80 degrees Celsius", "120 degrees Celsius"],
        "answer": "100 degrees Celsius"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Gold", "Osmium", "Silver"],
        "answer": "Oxygen"
    },
    {
        "question": "What is the capital city of Japan?",
        "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
        "answer": "Tokyo"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["Nucleus", "Ribosome", "Mitochondria", "Golgi apparatus"],
        "answer": "Mitochondria"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Graphite"],
        "answer": "Diamond"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "answer": "Canberra"
    }

]
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "score" not in st.session_state:
    st.session_state.score = {"correct": 0, "incorrect": 0}
if "total_attempts" not in st.session_state:
    st.session_state.total_attempts = 0

st.title("Simple Quiz App")
def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_question = random.choice(questions)
    st.session_state.total_attempts = 0
    st.session_state.score = {"correct": 0, "incorrect": 0}
def get_new_question():
    st.session_state.current_question = random.choice(questions)

if not st.session_state.quiz_started:
    if st.button("Start New Quiz"):
        start_quiz()
else:
    current_question = st.session_state.current_question
    if current_question:
        st.write(f"### {current_question['question']}")
        selected_option = st.radio("Select an option:", current_question["options"], key="options")

        if st.button("Submit Answer"):
            st.session_state.total_attempts += 1
            if selected_option == current_question["answer"]:
                st.session_state.score["correct"] += 1
                st.success("Correct answer!")
            else:
                st.session_state.score["incorrect"] += 1
                st.error(f"Incorrect! The correct answer is: {current_question['answer']}")
            get_new_question()
    st.write("### Quiz Progress")
    st.write(f"Total Questions Answered: {st.session_state.total_attempts}")
    st.write(f"Correct: {st.session_state.score['correct']}, Incorrect: {st.session_state.score['incorrect']}")
