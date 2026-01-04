def run_quiz():
    questions = {
        " What is the capital of Pakistan? ": "Islamabad",
        " What is the national language? ": "Urdu",
        "When did Pakistan gain independence ? ": "August 14, 1947"
    }
    
    score = 0
    print("--- Welcome to the Quick Quiz! ---\n")

    for question, correct_answer in questions.items():
        user_answer = input(question)
        
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
        print("-" * 20)

    print(f"\nQuiz Completed! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()
