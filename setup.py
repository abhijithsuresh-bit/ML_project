from setuptools import find_packages,setup

setup(
    name="Mentall_Illness",
    author="",
    author_email="abhijithsuresh563@gmail.com",
    version="0.0.1",
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "streamlit",
        "openpyxl"    
],
    packages=find_packages()
)