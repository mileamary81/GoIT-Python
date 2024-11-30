
import pandas as pd

# Reading the file from path
survey_results = pd.read_csv("C:/Users/marim/Documents/Data Analyst DA3/Capitolul 4 - Python/lectia 4/survey_results_public.csv",)
print(survey_results)
print("---------------------")

# Number of respondents
print("1) How many respondents have completed the survey?")
resp_no = len(survey_results)
print(f"The number of respondents is: {resp_no}")
print("---------------------")

# x=0
# # Traverse all cells in the DataFrame
# for index, row in survey_results.iterrows():
#     if row.notnull().all():
#         x=x+1
# print(x)

# Number of respondents who have answered to all questions
print("2) How many respondents have answered all the questions?")
respondents_completed = survey_results.notnull().all(axis=1)
full_answers_count = respondents_completed.sum()
print(f"The number of respondents who have answered all questions is: {full_answers_count}")
print("---------------------")

# Measures of central tendency for "WorkExp"
print(f"3) What are the values for measures of central tendency for work experience")
mean_value = round(survey_results["WorkExp"].mean())
print(f"a. The mean value of work experience field is: {mean_value}")
median_value = round(survey_results["WorkExp"].median())
print(f"b. The median value of work experience field is: {median_value}")
mode_work_exp = round(survey_results["WorkExp"].mode().values[0])
print(f"c. The mode value of work experience field is: {mode_work_exp}")
print("---------------------")

# Number of respondents that work remote?
print("4) How many respondents work remote?")
remote_workers = 0
for i in survey_results["RemoteWork"]:
    if i == "Remote":
        remote_workers += 1
print(f"The number of respondents that work remote is: {remote_workers}")
print("---------------------")

# Percentage of respondents who program in Python?
print(f"5) What percentage of respondents program in Python?")
python_programmers = 0
for i in survey_results["LanguageHaveWorkedWith"]:
    if "Python" in str(i):
           python_programmers += 1
python_programmers_percentage = round(python_programmers / resp_no * 100, 2)
print(f"The percentage of respondents that program in Python is: {python_programmers_percentage}")
print("---------------------")

# Number of respondents who have learned to program through online courses
print(f"6) How many respondents have learned to program through online courses?")
online_learners = 0
for i in survey_results["LearnCode"]:
    if "Online" and "online" in str(i):
           online_learners += 1
print(f"The number of respondents who have learned to program through online courses is: {online_learners}")
print("---------------------")

# Mean and median value of the remuneration per country among the Python programmers?
print(f"7) What is the mean and median value of the remuneration per country among the Python programmers?")
python_respondents = survey_results[survey_results["LanguageHaveWorkedWith"].str.contains("Python", case=False, na=False)]
remuneration_status = round(python_respondents.groupby("Country")["ConvertedCompYearly"].agg(["mean", "median"]), 2)
print(remuneration_status)
print("---------------------")

# Education level for top 5 respondents with the highest compensation
print(f"8) What is the education level for top 5 respondents with the highest compensation?")
# Top 5 respondents with the highest compensation
highest_comp = survey_results.sort_values(by = "ConvertedCompYearly", ascending = False).head()
education_level = highest_comp[["EdLevel", "ConvertedCompYearly"]]
print(f"The education level for top 5 respondents with the highest compensation is: {education_level}")













