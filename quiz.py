def print_question(question, options):
  print(question)
  for idx, option in enumerate(options, start=1):
      print(f"{idx}. {option}")

def get_user_answer():
  while True:
      user_input = input("Enter your answer (1, 2, 3, or 4): ")
      if user_input.isdigit() and 1 <= int(user_input) <= 4:
          return int(user_input)
      else:
          print("Invalid input. Please enter a number between 1 and 4.")

def evaluate_answer(user_answer, correct_answer, score):
  if user_answer == correct_answer:
      print("Correct!")
      score += 1
  else:
      print("Incorrect. The correct answer is:", correct_answer)
  return score

def main():
  questions = [
      {
          "question": "Which of the following data types is immutable in Python",
          "options": ["List", "Dictionary", "Tuple", "Set"],
          "correct_answer": 3
      },
      {
          "question": "Which data structure follows the LIFO principle?",
          "options": ["Queue", "Stack", "Linked List", "Tree"],
          "correct_answer": 2
      },
      {
          "question": "Which sorting algorithm is known for its stability?",
          "options": ["Merge Sort", "Quick Sort", "Selection Sort", "Heap Sort"],
          "correct_answer": 1 
      },
  ]

  score = 0

  print("Welcome to the Quiz Game!")
  print("You will be asked a series of questions. Enter the number of your choice as the answer.")

  for idx, question in enumerate(questions, start=1):
      print("\nQuestion", idx)
      print_question(question["question"], question["options"])
      user_answer = get_user_answer()
      score = evaluate_answer(user_answer, question["correct_answer"], score)

  print("\nQuiz complete!")
  print("Your final score is:", score)

if __name__ == "__main__":
  main()
