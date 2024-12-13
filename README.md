# Simple Quiz App

This is a simple quiz application built using **Streamlit**, a Python library for building web applications. The app allows a single user to start a new quiz session, answer multiple-choice questions, and track their progress.

## Features

1. **Start New Quiz**: The user can initiate a new quiz session, which resets the progress.
2. **Random Questions**: The app fetches a random multiple-choice question from a predefined list.
3. **Answer Submission**: Users can select an answer from the options and submit their choice.
4. **Quiz Progress Tracking**: Tracks total questions answered, the number of correct answers, and incorrect answers.

## How It Works

- The app uses a list of questions stored in a dictionary format with keys for the question, options, and correct answer.
- Streamlit's session state variables are used to persist quiz progress between interactions.
- Feedback is provided after each answer submission, indicating whether the user's choice was correct or incorrect.

## Requirements

- Python 3.7 or higher
- Streamlit library

Install Streamlit using pip if not already installed:

```bash
pip install streamlit
```

## How to Run the App

1. Clone the repository or copy the code to a file named `app.py`.
2. Navigate to the directory containing the file in your terminal.
3. Run the app using the following command:

```bash
streamlit run app.py
```

4. The app will open in your default web browser. You can also access it at `http://localhost:8501`.

## File Structure

```
|-- app.py             # Main Python script for the Streamlit app
|-- README.md          # Documentation for the app
```

## Future Enhancements

- Integrate with a database for storing and managing questions.
- Add a timer for answering questions.
- Implement user authentication for tracking individual user progress.
- Add more customization options for the quiz.


## Contributing

Contributions are welcome! If you would like to add features or fix issues, please fork the repository and submit a pull request.

## Author
Aman Singh Chauhan
