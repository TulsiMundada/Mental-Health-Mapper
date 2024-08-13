import tkinter as tk
from datavisualisation import MentalHealthDatasetVisualization
from speech_to_text import PatientDataCollector
from recommendation import MentalHealthAssessmentGUI
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, bg="lightblue",width=300, height=600)
        self.frame.pack(side="left", fill="y")
        self.label = tk.Label(self.frame, text="Main Menu")
        self.label.pack()

        self.button1 = tk.Button(self.frame, text="Speech To Text", command=self.speech_to_text)
        self.button1.pack(pady=20)

        self.button2 = tk.Button(self.frame, text="Data Visualisation", command=self.data_visualisation)
        self.button2.pack(pady=20)

        self.button3 = tk.Button(self.frame, text="Recommendation", command=self.recommendation)
        self.button3.pack(pady=20)
            # Create a frame to fill the unused space
        self.fill_frame = tk.Frame(master, bg="gray")  # Use a different bg color
        self.fill_frame.pack(side="right", fill="both", expand=True)

    def speech_to_text(self):
        new_window = tk.Toplevel(self.master)
        gui = PatientDataCollector(new_window)
        new_window.title("Dear Dairy , Today.... !")
        new_window.wm_geometry("+200+0")

    def data_visualisation(self):
        new_window = tk.Toplevel(self.master)
        gui = MentalHealthDatasetVisualization(new_window)
        new_window.title("Lets see how you have been till now!")
        new_window.wm_geometry("+200+0")

    def recommendation(self):
        new_window = tk.Toplevel(self.master)
        gui = MentalHealthAssessmentGUI(new_window)
        new_window.title("Recommendations to your Well Being!")
        new_window.wm_geometry("+200+0")

root = tk.Tk()
root.title("Main Window")
root.geometry("600x400")
app = MainWindow(root)
root.mainloop()