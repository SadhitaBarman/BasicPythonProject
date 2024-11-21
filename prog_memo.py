def quizApp():
    quizData = [
        {
            "question": "Which language uses npm?",
            "options": ["1. Node.js", "2. Python", "3. C", "4. Ruby"],
            "answer": 1
        },
        {
            "question": "Which programming language is known as the backbone of web development?",
            "options": ["1. Python", "2. JavaScript", "3. C++", "4. Java"],
            "answer": 2
        },
        {
            "question": "Try-Else block is not used in which language?",
            "options": ["1. Python", "2. JavaScript", "3. R", "4. Perl"],
            "answer": 1
        }
    ]

    print("Welcome to the Quiz App!\n")
    score = 0

    for i, q in enumerate(quizData):
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        while True:
            try:
                user_answer = int(input("Enter your answer (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}: {q['options'][q['answer'] - 1]}\n")

    print(f"Quiz Over! Your final score is {score}/{len(quizData)}")

if __name__ == "__main__":
    quizApp()
