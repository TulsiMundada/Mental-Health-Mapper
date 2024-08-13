import speech_recognition as sr
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import datetime
import joblib as j
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer
vector=j.load('vectorizer.pkl')
model=j.load('model.pkl')
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pandas as pd
import os

# Assuming you have 'vector' and 'model' defined elsewhere
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return ' '.join(tokens)

def predict_mood(text):
    vec = vector.transform([text])
    result = model.predict(vec)[0]
    return result

def save_to_csv(data, filename='mental_health_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, mode='a', header=not os.path.exists(filename), index=False)

class PatientDataCollector:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Data Collector")
        self.day_label = tk.Label(root, text="Day:")
        self.day_label.pack()
        self.day_entry = tk.Entry(root)
        self.day_entry.pack()
        self.record_button = tk.Button(root, text="Record Audio", command=self.record_audio, background="palegreen")
        self.record_button.pack()
        self.text_label = tk.Label(root, text="Text:")
        self.text_label.pack()
        self.text_box = tk.Text(root, height=10, width=40)
        self.text_box.pack()
        self.predict_button = tk.Button(root, text="Predict Mood", command=self.predict_mood, background="palegreen")
        self.predict_button.pack()
        self.result_label = tk.Label(root, text="Predicted Mood:")
        self.result_label.pack()
        self.result_box = tk.Text(root, height=1, width=40)
        self.result_box.pack()
        self.save_button = tk.Button(root, text="Save to CSV", command=self.save_to_csv , background="palegreen")
        self.save_button.pack()
        

    def record_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Please say something:")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="en-US")
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, text)
            except sr.UnknownValueError:
                messagebox.showerror("Error", "Google Speech Recognition could not understand your audio")
            except sr.RequestError as e:
                messagebox.showerror("Error", "Could not request results from Google Speech Recognition service; {0}".format(e))

    def predict_mood(self):
        text = self.text_box.get(1.0, tk.END)
        preprocessed_text = preprocess_text(text)
        predicted_mood = predict_mood(preprocessed_text)
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, predicted_mood)

    def save_to_csv(self):
        day = self.day_entry.get()
        text = self.text_box.get(1.0, tk.END).rstrip('\n')
        predicted_mood = self.result_box.get(1.0, tk.END).rstrip('\n')
        data = [{'day': day, 'text': text, 'predicted_mood': predicted_mood}]
        save_to_csv(data)
        messagebox.showinfo("Success", "Data saved to CSV file")

if __name__ == "__main__":
    root = tk.Tk()
    collector = PatientDataCollector(root)
    root.mainloop()