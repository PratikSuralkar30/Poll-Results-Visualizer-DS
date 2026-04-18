# 📊 Poll Results Visualizer

An end-to-end data analysis and visualization dashboard built for parsing, analyzing, and presenting poll and survey responses.

## 🚀 Features
- **Interactive Dashboard:** Built with Streamlit for live filtering.
- **Demographic Filters:** Analyze data by Country, Gender, and Loyalty Level.
- **Key Metrics:** Instantly view Total Responses, Average Satisfaction, and Quality Ratings.
- **Rich Visualizations:** Pie charts, Bar charts, and Histograms powered by Plotly.
- **EDA Pipeline:** Standalone Python script (`src/eda_analysis.py`) for static chart generation using Seaborn & Matplotlib.

## 🛠️ Tech Stack
- **Python 3.x**
- **Pandas & NumPy** (Data Manipulation)
- **Matplotlib & Seaborn** (Static EDA Visualizations)
- **Plotly Express** (Interactive Web Charts)
- **Streamlit** (Web Application Framework)

## 📂 Project Structure
```text
Poll-Results-Visualizer/
├── data/                  # Contains 'customer_feedback.csv'
├── src/                   # Helper scripts like eda_analysis.py
├── outputs/               # Saved static charts from EDA
├── app.py                 # Main Streamlit Dashboard application
├── project_documentation.md # Full 16-step execution guide
├── requirements.txt       # Dependencies
└── README.md              # This file
```

## 💻 How to Run

1. **Clone the repository** and navigate to the project directory.
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Dashboard:**
   ```bash
   streamlit run app.py
   ```
5. **Run the EDA Script (Optional):**
   ```bash
   cd src
   python eda_analysis.py
   ```

## 📸 Screenshots
*(Add screenshots of the dashboard and charts in the `images/` folder and link them here)*

---
*Developed as an industry-standard portfolio project for Data Analysis and Research roles.*
