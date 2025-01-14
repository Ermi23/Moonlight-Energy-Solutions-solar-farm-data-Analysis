# time_series.py
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class TimeSeriesAnalysis:
    def __init__(self, df):
        self.df = df

    def plot_time_series(self, columns):
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
        plt.figure(figsize=(15, 8))
        for col in columns:
            plt.plot(self.df['Timestamp'], self.df[col], label=col)
        plt.legend()
        plt.title('Time Series Analysis')
        plt.show()

    def plot_time_series_streamlit(self, columns):
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
        plt.figure(figsize=(15, 8))
        for col in columns:
            plt.plot(self.df['Timestamp'], self.df[col], label=col)
        plt.legend()
        plt.title('Time Series Analysis')
        st.pyplot(plt)
