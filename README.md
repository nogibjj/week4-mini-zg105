[![CI](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml/badge.svg)](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml)
# IDS706-Week4-miniProject
In this project, I change the actions setting and add a new strategy to test python versions for 3.6, 3,7, 3.8 and 3.9. I read students' scores from class_grades.csv. Then used Polars to analysis the data and created data visualization by main.ipynb. The output shows the distribution and summary of input class_grades.csv file. The lib.py file stores code shared by main.ipynb and test_main.ipynb. The generate.py is used to generate class_grades.csv
- ``.devcontainer`` The `Dockerfile` lists configurations for Docker, the `devcontainer.json` is for Visual Studio Code extension.

- ``workflows`` is for github actions, enables automated CI/CD for the project. Add new strategy to test python version 3.6 to 3.9

- ``Makefile`` lists make instruments

- ``requirements.txt`` lists the dependencies for the project

- ``lib.py`` library for sharing code between main.ipynb and test_main.ipynb
  
- ``main.ipynb`` uses polars to do data analysis on input .csv file, including mean, median and std. I also plot the distribution of grades using matplot.

- ``test_main.ipynb`` testing scripts for CI
