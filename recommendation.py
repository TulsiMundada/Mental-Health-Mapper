import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

class MentalHealthAssessmentGUI():
    def __init__(self,root):
        self.root = root
        self.root.title("Mental Health Assessment")

        # Create a file selection button
        self.file_button = tk.Button(self.root, text="Select CSV File", command=self.select_file ,background="SlateBlue1")
        self.file_button.pack()

        # Create a label to display the file name
        self.file_label = tk.Label(self.root, text="")
        self.file_label.pack()

        # Create a button to visualize and assess
        self.assess_button = tk.Button(self.root, text="We recommend you to", command=self.visualize_and_assess,background="SlateBlue1")
        self.assess_button.pack()

        # Create a text box to display the results
        self.results_text = tk.Text(self.root, width=40, height=10)
        self.results_text.pack()

    def select_file(self):
        filename = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "mental_health_data.csv")])
        self.file_label.config(text=f"Selected file: {filename}")

    def visualize_and_assess(self):
        filename = self.file_label.cget("text").split(": ")[1]
        df = pd.read_csv(filename)

        mood_counts = df['predicted_mood'].value_counts()

        most_common_mood = mood_counts.idxmax()

        health_status = ""
        recommendations = []

        if most_common_mood == 'happy':
            health_status = 'The patient is fit.'
            recommendations = [
                'Continue engaging in activities that bring you joy.',
                'Maintain a healthy lifestyle with balanced nutrition and regular exercise.',
                'Consider setting new personal goals and challenges to stay motivated.'
            ]
        elif most_common_mood == 'Normal':
            health_status = 'The patient is in a normal mental state.'
            recommendations = [
                'Keep up with your current routines and practices.',
                'Stay connected with friends and family to maintain social support.',
                'Regularly check in with yourself to ensure you’re managing stress effectively.'
            ]
        elif most_common_mood == 'depression':
            health_status = 'The patient is depressed.'
            recommendations = [
                'Consider seeking support from a mental health professional.',
                'Engage in activities that you used to enjoy, even if it’s difficult.',
                'Reach out to trusted friends or family members for support and understanding.'
            ]
        elif most_common_mood == 'suicidal':
            health_status = 'The patient is not in a healthy mental state.'
            recommendations = [
                'Seek immediate help from a mental health professional or counselor.',
                'Contact crisis support services or helplines for urgent assistance.',
                'Ensure you have a support network in place and communicate openly about your feelings.'
            ]
        else:
            health_status = 'Unknown mood state.'
            recommendations = [
                'Consider reviewing the mood prediction model for accuracy.',
                'Ensure proper data collection and preprocessing to improve predictions.',
                'Consult with a mental health professional to understand the implications of your data.'
            ]

        results = f"Most common mood: {most_common_mood}\n{health_status}\nRecommendations:\n"
        for suggestion in recommendations:
            results += f"- {suggestion}\n"

        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, results)

  #  def run(self):
  #      self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = MentalHealthAssessmentGUI(root)
    root.mainloop()