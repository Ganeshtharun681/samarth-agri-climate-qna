Project Samarth – Intelligent Agri-Climate Q&A System
Overview

Project Samarth is a functional prototype of an intelligent question-answering system built using live datasets from the Government of India’s data.gov.in portal.
The system allows users to ask natural language questions about India’s agricultural economy and its relationship with climate patterns. It retrieves and analyzes data directly from government sources to generate accurate, traceable, and data-backed insights.

Objective

Government datasets from different ministries, such as the Ministry of Agriculture & Farmers Welfare and the India Meteorological Department (IMD), exist in diverse formats. This project integrates those datasets into a unified system and provides an interactive interface that enables policy analysts, researchers, and students to easily access cross-domain insights.

Datasets Used

Rainfall Dataset (IMD) – Annual and forecasted rainfall data for different years.

Crop Production Dataset (Ministry of Agriculture) – Crop production and storage capacity data for Indian states.

Technologies and Libraries

Python 3.10+

Streamlit – for building the user interface

Pandas – for data cleaning and processing

Requests – for accessing live APIs from data.gov.in

System Design

Data Fetching:
The data_fetch.py script connects to the data.gov.in API using provided API keys and downloads live data into CSV format.

Data Processing:
The execute.py script cleans, merges, and structures the rainfall and crop data for further analysis.

Interactive Q&A Interface:
The app.py script runs a Streamlit web app that provides a simple interface for users to ask analytical questions and view data-backed answers.

How to Run Locally

Clone this repository or download it as a ZIP file.

Open a terminal in the project folder.

Run the following commands:

pip install -r requirements.txt
streamlit run app.py


Once it runs, open the link shown in your terminal (usually http://localhost:8501
) to access the prototype.