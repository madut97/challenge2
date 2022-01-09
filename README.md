# *Save Qualified Loans as New CSV CLI*

**This project is a new feature which will be added to the our existing loan qualifier app. The new feature will allow users who would like to save their list of qualified loaners as a csv file. The main problem which has inspired us to add this feature is the lack of a save csv functionality, which makes it difficult for the user to access their list of qualified loaners, which they meet the criteria for.**

## Directory 

[Progam](app)
[Program Functions](qualifier)
[Data files](data)

---

## *Technologies*

This feature/project leverages Python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entry-point. 

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [sys](https://github.com/python/cpython/blob/main/Python/sysmodule.c) - For exiting the app if user credentials fail to meet criteria
---   

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
  pip install sys
```

## Usage

Step1: Asks user the csv path to rate-sheet to be used:

![Loan qualifier prompt 1](https://github.com/madut97/challenge2/blob/master/images/step_1.png)

Step2: If qualified loans exist for the user, feature asks user whether or not if they would like to save results to a new csv file:

![Loan qualifier prompt 2](images/step_2.png)

--- 

## Contributors

Brought to you by Michael Adut

* email: mia269@nyu.edu

* linkedin: https://www.linkedin.com/in/michael-adut-a3a43b100/

---

## License

When you share a project on a repository, especially a public one, it's important to choose the right license to specify what others can and can't with your source code and files. Use this section to include the license you want to use.
