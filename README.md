# Ai-voice-interview-assistant

## Description

The AI Interview Assistant is a Python-based application that simulates an interview experience. It asks **HR**, **Python**, or **Technical** interview questions, accepts answers either by typing or voice, evaluates responses based on predefined keywords, provides instant feedback, calculates a score, and saves the interview results in a JSON file.

The project uses **speech recognition** for voice input and **text-to-speech** to communicate with the user, making the interview experience interactive.

## Features

* Conducts HR, Python, and Technical interviews.
* Supports both **text** and **voice** answer modes.
* Uses Text-to-Speech (TTS) to ask interview questions.
* Uses Speech Recognition for voice responses.
* Randomly selects interview questions.
* Evaluates answers using keyword matching.
* Provides instant feedback and scores.
* Calculates the total interview score.
* Saves interview results in a JSON file.

## Project Structure

```text
AI-Interview-Assistant/
│── main.py
│── questions.py
│── interview_results.json
│── README.md
```

## Technologies Used

* Python 3
* SpeechRecognition
* pywin32 (Windows Speech API)
* PyAudio
* JSON
* random
* time

## Requirements

Install the required libraries before running the project:

```bash
pip install SpeechRecognition
pip install pywin32
pip install pyaudio
```

> **Note:** PyAudio installation may require platform-specific setup. On Windows, install the appropriate wheel if needed.

## Algorithm

### `questions.py`

1. Store interview questions in separate lists:

   * HR Questions
   * Python Questions
   * Technical Questions
2. Create keyword dictionaries for each question.
3. Each question has a set of expected keywords used for evaluation.
4. Export all questions and keyword dictionaries for use in `main.py`.

### `main.py`

1. Import the required libraries and question data.
2. Welcome the candidate.
3. Ask the candidate to enter their name.
4. Let the candidate choose an interview category:

   * HR Interview
   * Python Interview
   * Technical Interview
5. Let the candidate choose the answer mode:

   * Type answers
   * Speak answers
6. Randomly select five interview questions.
7. Ask each question using Text-to-Speech.
8. Accept the candidate's response.
9. Compare the response with predefined keywords.
10. Assign a score and provide feedback.
11. Store the interview details.
12. Calculate the total score.
13. Display the overall performance.
14. Save all interview results in `interview_results.json`.

## Scoring System

| Keyword Match                | Score | Feedback           |
| ---------------------------- | ----: | ------------------ |
| No answer                    |     0 | No answer provided |
| No keywords matched          |     1 | Needs Improvement  |
| One keyword matched          |     2 | Good Answer        |
| Two or more keywords matched |     3 | Excellent Answer   |

## Sample Output



https://github.com/user-attachments/assets/126e0494-118c-455d-b672-be732097408e




## Output File

After the interview, the application generates:

```text
interview_results.json
```

The file stores:

* Candidate Name
* Interview Category
* Questions
* Answers
* Individual Scores
* Feedback


## Note

* The project currently runs on **Windows** because it uses the Windows Speech API (`pywin32`) for text-to-speech.
* A microphone is required for voice interview mode.
* An active internet connection is required for Google Speech Recognition.
* Interview questions and evaluation keywords are stored in `questions.py`.
* Interview results are automatically saved in `interview_results.json`.

## Author

**Bhargavi**
