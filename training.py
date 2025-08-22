from sklearn.model_selection import train_test_split
from model import patient_df
import updated
import pandas as pd
a=['Survey Year', 'Program Category', 'Region Served', 'Age Group', 'Sex',
       'Transgender', 'Sexual Orientation', 'Hispanic Ethnicity', 'Race',
       'Living Situation', 'Household Composition', 'Preferred Language',
       'Religious Preference', 'Veteran Status', 'Employment Status',
       'Number Of Hours Worked Each Week', 'Education Status',
       'Special Education Services', 'Mental Illness',
       'Intellectual Disability', 'Autism Spectrum',
       'Other Developmental Disability', 'Alcohol Related Disorder',
       'Drug Substance Disorder', 'Opioid Related Disorder',
       'Mobility Impairment Disorder', 'Hearing Impairment',
       'Visual Impairment', 'Speech Impairment', 'Hyperlipidemia',
       'High Blood Pressure', 'Diabetes', 'Obesity', 'Heart Attack', 'Stroke',
       'Other Cardiac', 'Pulmonary Asthma', 'Alzheimer or Dementia',
       'Kidney Disease', 'Liver Disease', 'Endocrine Condition',
       'Neurological Condition', 'Traumatic Brain Injury', 'Joint Disease',
       'Cancer', 'Other Chronic Med Condition', 'No Chronic Med Condition',
       'Unknown Chronic Med Condition', 'Cannabis Recreational Use',
       'Cannabis Medicinal Use', 'Smokes', 'Received Smoking Medication',
       'Received Smoking Counseling', 'Serious Mental Illness',
       'Alcohol 12m Service', 'Opioid 12m Service',
       'Drug/Substance 12m Service', 'Principal Diagnosis Class',
       'Additional Diagnosis Class', 'SSI Cash Assistance',
       'SSDI Cash Assistance', 'Veterans Disability Benefits',
       'Veterans Cash Assistance', 'Public Assistance Cash Program',
       'Other Cash Benefits', 'Medicaid and Medicare Insurance',
       'No Insurance', 'Unknown Insurance Coverage', 'Medicaid Insurance',
       'Medicaid Managed Insurance', 'Medicare Insurance', 'Private Insurance',
       'Child Health Plus Insurance', 'Other Insurance',
       'Criminal Justice Status', 'Three Digit Residence Zip Code'
    ]

patient_df=pd.get_dummies(patient_df,columns=a,drop_first=True,dtype=int)

patient_df

# Separate features (X) and target (y)
X = patient_df.drop('Mental Illness_YES', axis=1)
y = patient_df['Mental Illness_YES']

# Split into 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Confirm shapes
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

from sklearn.linear_model import LogisticRegression

# Create the model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

# Predict the target values for the test set
y_pred = model.predict(X_test)

# Calculate accuracy by comparing predicted and actual values
accuracy = accuracy_score(y_test, y_pred) # to accuracy we use both test data

print(f"Accuracy: {accuracy:.4f}")

def predict_patient(model, new_raw_dict, X_train_columns):
    # Convert new input to DataFrame
    new_df = pd.DataFrame([new_raw_dict]) # we use [] in new raw data is we cannot pass dict

    # One-hot encode with drop_first=True (just like training)
    new_encoded = pd.get_dummies(new_df, drop_first=True) # we just pass the colmns

    # Ensure all expected columns are present
    new_encoded = new_encoded.reindex(columns=X_train_columns, fill_value=0) # alling the colmns same as training colmns
# this is important
    # Predict
    pred = model.predict(new_encoded)[0] # why [0] because data return like array so to take 1st element
    return "YES" if pred == 1 else "NO"
