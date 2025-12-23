# Gaming Hours vs. Academic & Work Performance Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Computation-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-7db0bc?style=for-the-badge)
![SciPy](https://img.shields.io/badge/SciPy-Statistics-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-Machine_Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Random Forest](https://img.shields.io/badge/Model-Random_Forest-2ea44f?style=for-the-badge)

> **Key Concepts:** Statistics • Random Forest Regression • Performance Modeling • Data Visualization • Hypothesis Testing

## 1. About the Program
**What problem does this solve?**
This project explores the correlation between video gaming habits and productivity levels in academic and professional settings. By analyzing user data, the program aims to determine if increased gaming hours statistically impact performance metrics such as GPA or work efficiency ratings.

**Key Features:**
* **Data Analysis:** Utilizes statistical methods to identify trends and outliers within the dataset.
* **Visualization:** Generates plots (such as histograms, scatter plots, and heatmaps) to visually represent the relationship between gaming duration and performance scores.
* **Prediction:** Uses data modeling to predict potential performance outcomes based on daily gaming hours.

## 2. Data Source
**Dataset Name:** Gaming Hours vs Academic & Work Performance: https://www.kaggle.com/datasets/prince7489/gaming-hours-vs-academic-and-work-performance

**Description:**
The dataset serves as the foundation for this analysis. It contains data points representing individual gaming habits (hours played) alongside performance indicators (grades, test scores, or work evaluations). The goal is to provide a real-world basis for testing statistical hypotheses regarding leisure time and productivity.

## 3. Setup & Installation
To set up this project locally, follow these steps:

**Prerequisites:**
* Python 3.8 or higher
* pip (Python package installer)

**Installation Steps:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gaming-performance-analysis.git
   cd gaming-performance-analysis

2. **Create a virtual environment (optional but recommended):**
   ```bash
    python -m venv venv

    #Windows
    source venv/bin/activate  
    # On Mac/Linux
    venv\Scripts\activate
    ```

3. **Install required packages:**
   ```bash
    pip install -r requirements.txt
    ```

4. **Run the analysis script:**
    ```bash
     jupyter notebook game_analysis.ipynb
    ```

5. **Run the Streamlit app**
    ```bash
     streamlit run app.py
    ```
