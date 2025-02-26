from setuptools import setup, find_packages

setup(
    name="electricity_bill_prediction",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "tensorflow",
        "streamlit",
        "joblib"
    ],
    author="Your Name",
    description="A machine learning model to predict electricity bills",
    
)
