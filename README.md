# Zeolites App
Dominique Mahoner, Bucknell University

# Features 
-  seed
-  SiO2
-  NaOH
-  SDA
-  B2O3
-  H2O
-  "seed amount"
-  "temperature(°C)"
- "time (day)"
- "si/al(ICP-AES)"
- fd

# Output 
- Class: A binary variable indicating the outcome of zeolite formation
  -   Class "0": Failed experiments resulting in amorphous, mixed, dense, or layered phases.
  -    Class "1": Successful experiments resulting in a pure zeolite phase.

# Goals
This app contains the following steps:
- Data Preprocessing: Handles missing data, scales numerical values, and encodes categorical variables to prepare data for analysis.
- Predictive Modeling: Utilizes machine learning models to predict whether or not a zeolite will form.
- Feature Importance Analysis: Identifies key factors contributing to recurrence risk for accurate results.
- Visualization Tools: In order to help understnad model predictions a partial dependence plot was used.

# Heat Map
![image](https://github.com/user-attachments/assets/28ed6dd9-7374-433b-a269-e68d4c26852d)

# Model performance
![image](https://github.com/user-attachments/assets/395fd48e-fa55-4de0-9fd0-94a02494fb07)


