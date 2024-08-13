import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer

class MentalHealthDatasetVisualization():
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Health Dataset Visualization")
        self.df = pd.read_csv("mental_health_data.csv")
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM)
        self.create_buttons()

    def create_buttons(self):
        button1 = tk.Button(self.button_frame, text="Status Distribution", command=self.plot_status_correlations)
        button1.pack(side=tk.LEFT)

        button2 = tk.Button(self.button_frame, text="Day of Week Distribution", command=self.plot_day_of_week_distribution)
        button2.pack(side=tk.LEFT)

        button3 = tk.Button(self.button_frame, text="Status Over Time", command=self.plot_status_over_time)
        button3.pack(side=tk.LEFT)

        button4 = tk.Button(self.button_frame, text="Word Cloud", command=self.plot_word_cloud)
        button4.pack(side=tk.LEFT)

        button5 = tk.Button(self.button_frame, text="Pie Chart", command=self.plot_pie_chart)
        button5.pack(side=tk.LEFT)

        button6 = tk.Button(self.button_frame, text="Status Correlation", command=self.plot_status_correlation)
        button6.pack(side=tk.LEFT)

        button7 = tk.Button(self.button_frame, text="Line Graph", command=self.plot_line_graph)
        button7.pack(side=tk.LEFT)

        button8 = tk.Button(self.button_frame, text="Scoreboard", command=self.plot_scoreboard)
        button8.pack(side=tk.LEFT)

        button9 = tk.Button(self.button_frame, text="Sentiment Analysis", command=self.plot_sentiment_analysis)
        button9.pack(side=tk.LEFT)

    def plot_status_correlations(self):
        self.ax.clear()
        weekday_status_matrix = self.df.pivot_table(index="text", columns="predicted_mood", aggfunc="size", fill_value=0)
        corr_matrix = weekday_status_matrix.corr()
        sns.heatmap(corr_matrix, ax=self.ax, annot=True, cmap='coolwarm', cbar=False)
        self.ax.set_title("Status Correlations")
        self.canvas.draw()

    def plot_day_of_week_distribution(self):
        self.ax.clear()
        self.df['day'].value_counts().plot(kind='bar', ax=self.ax)
        self.ax.set_title("Day of Week Distribution")
        self.canvas.draw()

    def plot_status_over_time(self):
        self.ax.clear()
        self.df.groupby('day')['predicted_mood'].value_counts().unstack().plot(kind='line', ax=self.ax)
        self.ax.set_title("Status Over Time")
        self.canvas.draw()

    def plot_word_cloud(self):
        self.ax.clear()
        wordcloud = WordCloud().generate(' '.join(self.df['text']))
        self.ax.imshow(wordcloud, interpolation='bilinear')
        self.ax.axis("off")
        self.ax.set_title("Word Cloud")
        self.canvas.draw()

    def plot_pie_chart(self):
        self.ax.clear()
        self.df['predicted_mood'].value_counts().plot(kind='pie', ax=self.ax, autopct='%1.1f%%')
        self.ax.set_title("Status Pie Chart")
        self.canvas.draw()

    def plot_status_correlation(self):
        self.ax.clear()
        corr_matrix = pd.crosstab(self.df["predicted_mood"], self.df["predicted_mood"])
        sns.heatmap(corr_matrix, ax=self.ax, annot=True, cmap="coolwarm", square=True, cbar=False)
        self.ax.set_title("Correlation Heatmap")
        self.canvas.draw()

    def plot_line_graph(self):
        self.ax.clear()
        weekday_status_counts = self.df.groupby(["day", "predicted_mood"]).size().unstack()
        weekday_status_counts.plot(kind="bar", ax=self.ax)
        self.ax.set_title("Status Distribution by Weekday")
        self.ax.set_xlabel("Weekday")
        self.ax.set_ylabel("Count")
        self.ax.legend(title="Status")
        self.canvas.draw()

    def plot_scoreboard(self):
        self.ax.clear()
        status_counts = self.df["predicted_mood"].value_counts()
        scoreboard = pd.DataFrame({
            "Status": status_counts.index,
            "Count": status_counts.values,
            "Percentage": (status_counts.values / len(self.df)) * 100
        })
        scoreboard["Rank"] = scoreboard["Count"].rank(ascending=False).astype(int)
        self.ax.axis('off')
        self.ax.table(cellText=scoreboard.values, colLabels=scoreboard.columns, loc="center")
        self.canvas.draw()

    def plot_sentiment_analysis(self):
        self.ax.clear()
        sia = SentimentIntensityAnalyzer()
        sentiments = self.df["text"].apply(lambda x: sia.polarity_scores(x)["compound"])
        self.ax.bar(range(len(sentiments)), sentiments)
        self.ax.set_xlabel("Text Index")
        self.ax.set_ylabel("Sentiment Score")
        self.ax.set_title("Sentiment Analysis")
        self.canvas.draw()
    
if __name__ == "__main__":
    root = tk.Tk()
    gui = MentalHealthDatasetVisualization(root)
    root.mainloop()