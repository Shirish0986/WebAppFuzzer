import os

def run_static_analysis():
    print("Running Bandit for static security analysis...")
    os.system("bandit -r .")  # Replace with your app folder path
    
    print("Running Pylint for code quality analysis...")
    os.system("pylint .")  # Replace with the folder you want to analyze

# Example usage
if __name__ == "__main__":
    run_static_analysis()
