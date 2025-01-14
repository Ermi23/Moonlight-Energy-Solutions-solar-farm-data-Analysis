import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

class CorrelationAnalysis:
    def __init__(self, df):
        self.df = df

    def plot_correlation_matrix(self, columns):
        corr_matrix = self.df[columns].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix Heatmap')
        plt.show()

    def plot_pairplot(self, columns):
        sns.pairplot(self.df[columns])
        plt.title('Pair Plot for Selected Variables')
        plt.show()
        
    def plot_correlation_matrix_streamlit(self, columns):
        corr_matrix = self.df[columns].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix Heatmap')
        st.pyplot(plt)

    def plot_pairplot_streamlit(self, columns):
        sns.pairplot(self.df[columns])
        plt.title('Pair Plot for Selected Variables')
        st.pyplot(plt)
