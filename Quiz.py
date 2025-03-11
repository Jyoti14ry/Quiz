def run_quiz(questions):
    score = 0
    for question, details in questions.items():
        print("\n" + question)
        for i, option in enumerate(details["options"], start=1):
            print(f"{i}. {option}")
        
        try:
            user_answer = int(input("Enter your choice (1-4): "))
            if 1 <= user_answer <= 4:
                if details["options"][user_answer - 1] == details["answer"]:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is: {details['answer']}\n")
            else:
                print("Invalid input! Please enter a number between 1 and 4.\n")
        except ValueError:
            print("Invalid input! Please enter a number.\n")

    print(f"Quiz completed! Your final score is: {score}/{len(questions)}")


quiz_questions = {
    "What is the capital of France?": {
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    "Which language is primarily used for web development?": {
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML"
    },
    "What is 5 + 3?": {
        "options": ["5", "8", "10", "15"],
        "answer": "8"
    },
    "Who wrote 'Hamlet'?": {
        "options": ["Charles Dickens", "William Shakespeare", "Leo Tolstoy", "Mark Twain"],
        "answer": "William Shakespeare"
    }
}

run_quiz(quiz_questions)
