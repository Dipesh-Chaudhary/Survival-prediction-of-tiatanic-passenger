# Survival-prediction-of-tiatanic-passenger
It was a task given by [Treeleaf technology](https://treeleaf.ai/) as a technical assesment for the ML engineer role [Click Here to see the task](https://github.com/Dipesh-Chaudhary/Survival-prediction-of-tiatanic-passenger/blob/main/Task%20-%20ML%20Engineer.pdf)


**Since, the best suited data for the task was already available in the kaggle for the competition named [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data),so I downloaded the dataset from there .**

***Out of 3 availabale CSVs files the one named "train.csv" was for the actual use in the task and the file named "test.csv" was just to evaluate the accuracy for the competition. So For the task , i downloaded "train.csv" and renamed it as "[titanic_dataset.csv](https://github.com/Dipesh-Chaudhary/Survival-prediction-of-tiatanic-passenger/blob/main/Datasets/titanic_dataset.csv)"***

**Data Dictionary**
<table>
  <tr>
    <th> Variable</th>
    <th>Definition</th>
    <th>Key</th>
  </tr>
  <tr>
    <td>survived</td>
    <td>Survival</td>
    <td>0 = No, 1 = Yes</td>
  </tr>
  <tr>
    <td>pclass</td>
    <td>Ticket class</td>
    <td>1 = 1st, 2 = 2nd, 3 = 3rd</td>    
  </tr>
  <tr>
    <td>sex</td>
    <td>Gender</td>
    <td></td>    
  </tr>
  <tr>
    <td>Age</td>
    <td>Age in years</td>
    <td></td>    
  </tr>
  <tr>
    <td>sibsp</td>
    <td># of siblings / spouses aboard the Titanic</td>
    <td></td>    
  </tr>
  <tr>
    <td>parch</td>
    <td># of parents / children aboard the Titanic</td>
    <td></td>    
  </tr>
  <tr>
    <td>ticket</td>
    <td>Ticket number</td>
    <td></td>    
  </tr>
  <tr>
    <td>fare</td>
    <td>Passenger fare</td>
    <td></td>    
  </tr>
  <tr>
    <td>cabin</td>
    <td>Cabin number</td>
    <td></td>    
  </tr>
  <tr>
    <td>embarked</td>
    <td>Port of Embarkation C = Cherbourg, Q = Queenstown, S = Southampton</td>
    <td></td>    
  </tr>
</table>


**Variable Notes**

**pclass**: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower

**age**: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

**sibsp**: The dataset defines family relations in this way...

Sibling = brother, sister, stepbrother, stepsister
Spouse = husband, wife (mistresses and fiancés were ignored)

**parch**: The dataset defines family relations in this way...

Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.





**STEPS INVOLVED:**
**1.** Firstly, the data was clearly preprocessed and analysed and saved the preprocessed dataset as [titanic_processed.csv](https://github.com/Dipesh-Chaudhary/Survival-prediction-of-tiatanic-passenger/blob/main/Datasets/titanic_processed.csv).[Click here](https://github.com/Dipesh-Chaudhary/Survival-prediction-of-tiatanic-passenger/blob/main/Notebook/1%20Data_selection_%2B_EDA_%2B_Preprocessing_SURVIVAL_PREDICTION_OF_TITANIC.ipynb) for complete walk through
**2.** And then, 3 models as mentioned in task was trained and evaluated in those 4 essential evaluation metrics(accuracy , precision, recall and f1 score)[Click here for complete walk through](https://github.com/Dipesh-Chaudhary/Survival-prediction-of-tiatanic-passenger/blob/main/Notebook/2%20MODEL_TRAINING_%2B_EVALUATION_.ipynb)
    
  ![4af96cb0-8bba-4706-9d77-b7aaaf9a9f9c](https://github.com/user-attachments/assets/3bd11caa-0585-450a-9f42-e8f366c9c9dd)
  
  ![28b16a71-75f5-4df4-918b-fdc48d66ca82](https://github.com/user-attachments/assets/1c8ea6d3-9a87-4de5-8c32-8cce8a21702b)
  
  ![7221eb10-f13f-41b5-a490-08e222cccdb9](https://github.com/user-attachments/assets/e812ed36-01da-4fad-9f88-1962b5532833)




  **Test Set Accuracy Scores:**
  * **Random Forest:** Accuracy = 0.8156, Precision = 0.8361, Recall = 0.6892, F1 Score = 0.7556
  * **Logistic Regression:** Accuracy = 0.7933, Precision = 0.7681, Recall = 0.7162, F1 Score = 0.7413
  * **Neural Network:** Accuracy = 0.7877, Precision = 0.7903, Recall = 0.6622, F1 Score = 0.7206

**3.** Lastly, an UI was made and deployed using streamlit cloud [CLICK HERE TO USE](https://survival-prediction-of-tiatanic-passenger.streamlit.app/) 




