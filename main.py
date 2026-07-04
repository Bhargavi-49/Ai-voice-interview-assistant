
import win32com.client as wc
import time
import random
import json
import speech_recognition as sr
from questions import hr_questions, python_questions,technical_questions, hr_keywords, python_keywords,technical_keywords

speaker = wc.Dispatch("SAPI.SpVoice")
recognizer = sr.Recognizer()

# speak function
def speak(text):
    print(text)
    speaker.Speak(text)
    time.sleep(0.2) 

# listen function for voice answer
def listen_answer():
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        
        answer = recognizer.recognize_google(audio)
        print("You said:", answer)
        return answer

    except sr.UnknownValueError:
        speak("Sorry, I could not understand the audio.")
        return ""
    
    except sr.RequestError:
        speak("Speech service error.")
        return ""

# main function
def main():
    speak("Welcome to the AI Interview Assistant")

    candidate_name = input("Enter your name: ").strip()
    if candidate_name == "":
        candidate_name = "Candidate"

    # Choose interview type    
    print("Choose interview type")
    print("1. HR Interview")
    print("2. Python Interview")
    print("3.Technical Interview")
    speak("Choose interview type. Press 1 for HR Interview, 2 for Python Interview, or 3 for Technical Interview.")

    user_choice = input("Enter 1/2/3: ")
    print("You selected:", user_choice)

    if user_choice == "1":
        selected_questions = hr_questions.copy()
        selected_keywords = hr_keywords
        category = "HR"
    elif user_choice == "2":
        selected_questions = python_questions.copy()
        selected_keywords = python_keywords
        category = "Python"
    elif user_choice == "3":
        selected_questions = technical_questions.copy()
        selected_keywords = technical_keywords
        category = "Technical"    
    else:
        speak("Invalid choice. Please select 1,2 or 3.")
        return

    # choose answer mode
    print("Choose answer mode")
    print("1. Type your answer")
    print("2. Speak your answer")
    speak("Choose answer mode. Press 1 to type your answer or press 2 to speak your answer.")

    answer_mode = input("Enter 1 or 2: ")

    # interview data storage
    interview_data = []

    # shuffle questions and take 5 random questions
    random.shuffle(selected_questions)
    speak(f"{candidate_name}, your {category} interview will start now.")
    selected_questions = selected_questions[:5]

    for i, question in enumerate(selected_questions, start=1):
        speak(question)
        if answer_mode == "1":
            answer = input("Enter your answer: ")
        elif answer_mode == "2":
            answer = listen_answer()
        else:
            speak("Invalid answer mode. Using typing mode by default.")
            answer = input("Enter your answer: ")
        answer_lower = answer.lower()

        keywords = selected_keywords[question]
        match_score = 0

        for word in keywords:
            if word.lower().strip() in answer_lower:
                match_score += 1
        if len(answer.strip()) == 0:
            score = 0
            feedback = "No answer provided."
        elif match_score == 0:
            score = 1
            feedback = "Needs improvement"
        elif match_score == 1:
            score = 2
            feedback = "Good answer"
        else:
            score = 3
            feedback = "Excellent answer"
        speak(feedback)
        print()
        print("Score:", score)

        data = {
            "Candidate name":candidate_name,
            "question": question,
            "answer": answer,
            "Category": category,
            "score": score,
            "feedback": feedback
        }
        interview_data.append(data)

    # total score
    total_score = 0
    for item in interview_data:
        total_score += item["score"]

    speak(f"Your total score is {total_score}")

    if total_score > 8:
        result = "Excellent performance!"
    elif total_score > 5:
        result = "Good performance!"
    elif total_score > 3:
        result = "Average performance!"
    else:
        result = "Needs improvement!"


    speak(f"Overall Result: {result}")
    speak("Interview completed. Thank you for participating!")

    with open("interview_results.json", "w") as file:
        json.dump(interview_data, file, indent=4)

    print("\nInterview results saved in interview_results.json")

main()

