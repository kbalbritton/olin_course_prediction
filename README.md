Olin Course Prediction
======================

A prediction tool for Olin College course enrollment based on preregistration survey data and Olin's course history. 

# Usage

    python olin_course_prediction.py

## Preconditions

Installation of scikit learn and its dependencies: http://scikit-learn.org/stable/install.html

Also, Make sure to specify the locations of the Olin Course History data and Pre-Registration survey data in the main function of olin_course_prediction.py. Those files should be in the 'csv' format. Additionally, all of the pre-registration survey csv-files should be speicific to one semester and contain the semester information in the filename (eg "FA10").

## Output

After running olin_course_prediction.py, there will be 2 files in the /results directory: 

  - test_data.xls: the course enrollment predictions for the 5 models (discussed below) we're considering to predict course enrollment with one sheet per course

  - model_comparison.xls: one sheet with the cumulative error of each model compared with the acutal past enrollment of those courses (for the semesters with pre-registration data). 

## 5 Models

To gauge how effective our predictions are, we run through the predictions for 5 different models, each having different amounts of feature input data:

  - Baseline Predicted Enrollment: No features, trains on past enrollment trends

  - Gender Feature Enrollment: the baseline predicted enrollment model with the addition of the gender of the sudent added to the feature data

  - Prereg Predicted Enrollment: the gender feature enrollment model with the addition of pre-registration data to the feature data

  - Course History Predicted Enrollment: the gender feature enrollment model with the addition of feature data values (boolean) for every course at Olin as well as the major of the student

  - Prereg + Course History Predicted Enrollment: the combination of all of our predictive strategies; this model *should* be the most effective at predicting course enrollment

Additionally, we compare each of these models' predicted enrollment with the actual enrollment and the pre-registration survey predicted enrollment. 

# Predictive Model

We used scikit learn's Linear Regression model: 

http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html 

Using the linear regression model, we can predict whether or not a student is likely to take a course in a specific semester, given their grade level. 

So, to predict the enrollment of Software Design in the 1415FA semester, we make 4 separate linear regression models, one for each grade of students. These models consider the course histories of all students, noting those who took Software Design in the fall semester of the specified grade as well as the preregistration data for how many students within that grade said that they would take Software Design. The model then predicts for each student at Olin that semester the probability that the student would take Software Design. These probabilities are summed to determine the predicted total enrollment of the course. 