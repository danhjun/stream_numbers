import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load data from an Excel file
def load_data(file_path):
    sheets = pd.read_excel(file_path, sheet_name=None)
    return sheets

# Function to generate bar graphs for the top 10 sheets with highest playlist streams
def generate_bar_graphs(data):
    sorted_sheets = sorted(data.items(), key=lambda x: x[1]['Playlist Streams'].sum(), reverse=True)
    top_10_sheets = sorted_sheets[:10]

    st.markdown("### Top 10 Sheets with Highest Playlist Streams")
    for sheet_name, sheet_data in top_10_sheets:
        plt.figure(figsize=(10, 6))
        plt.bar(sheet_data['Date'], sheet_data['Playlist Streams'])
        plt.xlabel('Date')
        plt.ylabel('Playlist Streams')
        plt.title(f'Trends for {sheet_name}')
        plt.xticks(rotation=45)
        st.pyplot(plt)

# Main Streamlit app
def main():
    st.title("Playlist Streams Analysis")
    file_path = 'data/stream numbers.xlsx'

    if file_path is not None:
        data = load_data(file_path)
        generate_bar_graphs(data)

if __name__ == '__main__':
    main()
