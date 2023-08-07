
**Sleep Disorder Prediction**

**Aim of the Project:**
The main objective of this project is to analyze various lifestyle and medical factors, such as age, BMI, physical activity, sleep duration, blood pressure, etc., in order to predict the presence and type of sleep disorder.

**About the Dataset:**
The Sleep Health and Lifestyle Dataset consists of 400 rows and 13 columns, encompassing a wide range of variables related to sleep and daily habits. It includes information like gender, age, occupation, sleep duration, quality of sleep, physical activity level, stress levels, BMI category, blood pressure, heart rate, daily steps, and whether a sleep disorder is present.

**Key Features of the Dataset:**
	Comprehensive Sleep Metrics: The dataset provides insights into sleep duration, quality, and factors influencing sleep patterns.

	Lifestyle Factors: It allows the analysis of physical activity levels, stress levels, and BMI categories, shedding light on their impact on sleep.

	Cardiovascular Health: Blood pressure and heart rate measurements enable an examination of cardiovascular health in relation to sleep.

	Sleep Disorder Analysis: The dataset helps in identifying the occurrence of sleep disorders, including Insomnia and Sleep Apnea, based on various factors.

**Data Dictionary:**

Here's a breakdown of the columns in the dataset:

	Person_ID: A unique ID assigned to each individual.

	Gender: The gender of the person (Male/Female).

	Age: The age of the person in years.

	Occupation: The occupation of the person.

	Sleep_duration: The duration of sleep for the person in hours.

	Quality_of_sleep: A subjective rating of sleep quality, ranging from 1 to 10.

	Physical_activity: The level of physical activity of the person (Low/Medium/High).

	Stress Level: A subjective rating of stress level, ranging from 1 to 10.

	BMI_category: The BMI category of the person (Underweight/Normal/Overweight/Obesity).

	Blood_pressure: The blood pressure of the person in mmHg.

	Heart_rate: The heart rate of the person in beats per minute.

	Daily Steps: The number of steps taken by the person per day.

	Sleep_disorder: Indicates the presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).

**Data Preprocessing - Splitting Blood Pressure:**

The "Blood Pressure" column is split into "Systolic_BP" and "Diastolic_BP" columns by applying a lambda function to extract the values before and after the slash ("/"). High blood pressure is defined as having a systolic blood pressure - [Systolic_BP] (the top number) of 140 mmHg or higher and/or a diastolic blood pressure - [Diastolic_BP] (the bottom number) of 90 mmHg or higher.

**Exploratory Data Analysis Insights:**

Gender, Occupation, and BMI are identified as three key factors affecting sleep disorders. Males have a higher incidence of Insomnia, while females are more affected by Sleep Apnea. Certain occupations, such as nurses, show higher susceptibility to sleep disorders. BMI is also found to play a crucial role in predicting sleep disorders, with individuals categorized as Obese or Overweight being more prone to such disorders.
Check the Power BI for the data analysis.

**Splitting the Dataset for Training and Testing:**

The balanced dataset is split into training and testing sets using the `train_test_split` function. The training set will be used to build the models, while the testing set will be used to evaluate them.

**Model Building - Random Forest Classifier and Decision Tree Classifier:**

A Random Forest Classifier model is created using the RandomForestClassifier class from scikit-learn. The `n_estimators` parameter specifies the number of decision trees in the forest, and `n_jobs` specifies the number of jobs to run in parallel for fitting.
A Decision Tree Classifier model is created using the DecisionTreeClassifier class from scikit-learn.

**Model Evaluation**

Confusion Matrix and Accuracy: The confusion matrix and accuracy score are computed using scikit-learn's `confusion_matrix` and `accuracy_score` functions. The confusion matrix is visualized using a heatmap from Seaborn. A Random Forest Classifier model achieves 92% accuracy and Decision Tree Classifier model achieves 90% accuracy.

**Visualization - Actual vs. Predicted Values:**

The actual and predicted values of the "Sleep Disorder" column are visualized using Seaborn's `distplot`. The actual values are shown in red, while the predicted values are shown in blue.

**Conclusion and Model Performance:**

Two classification models, Random Forest Classifier and Decision Tree Classifier, were built and evaluated. Both models demonstrated good performance in predicting sleep disorders. The Random Forest Classifier outperformed the Decision Tree Classifier, achieving an accuracy of 92% on the test set. The results indicate that the Random Forest model is more robust and reliable for predicting sleep disorders in this dataset.

