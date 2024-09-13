# feedback.py
def collect_feedback(feedback):
    with open('feedback.txt', 'a') as f:
        f.write(feedback + '\n')

if __name__ == "__main__":
    feedback = input("Please provide feedback: ")
    collect_feedback(feedback)
