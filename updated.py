from model import patient_df
import pandas  as pd

patient_df.loc[(patient_df['Age Group']=='UNKNOWN') & (patient_df['Veteran Status']=='YES'),\
 ['Age Group','Veteran Status']]

patient_df.loc[(patient_df['Age Group']=='UNKNOWN')&(patient_df['Veteran Status']=='YES'),'Age Group']='ADULT' #this will change veteran yes to age grop adult

patient_df.loc[(patient_df['Autism Spectrum']=='UNKNOWN') & (patient_df['Veteran Status']=='YES'),'Autism Spectrum']='NO'

patient_df.loc[(patient_df['Neurological Condition']=='NO') & (patient_df['Traumatic Brain Injury']=='NO'),\
               ['Hearing Impairment', 'Visual Impairment', 'Speech Impairment']
               ]='NO'

patient_df.loc[(patient_df['Sex']=='UNKNOWN') & (patient_df['Transgender']=='NO, NOT TRANSGENDER')&\
               (patient_df['Veteran Status']=='YES'),'Sex'
               ]='MALE'

patient_df.loc[(patient_df['High Blood Pressure']=='UNKNOWN') & (patient_df['Obesity']=='NO')&\
               (patient_df['Heart Attack']=='NO') & (patient_df['Stroke']=='NO') & (patient_df['Other Cardiac']=='NO')\
               ,'High Blood Pressure'
               ]='NO'

patient_df.loc[(patient_df['High Blood Pressure']=='UNKNOWN') & (patient_df['Obesity']=='YES')&\
               (patient_df['Heart Attack']=='YES') | (patient_df['Stroke']=='YES') | (patient_df['Other Cardiac']=='YES')\
               ,'High Blood Pressure'
               ]='YES'

mask_yes_hyper = (
    (patient_df['Hyperlipidemia'] == 'UNKNOWN') &
    (
        (patient_df['Obesity'] == 'YES') |
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['High Blood Pressure'] == 'YES') |
        (patient_df['Heart Attack'] == 'YES') |
        (patient_df['Stroke'] == 'YES') |
        (patient_df['Other Cardiac'] == 'YES')
    )

)
patient_df.loc[mask_yes_hyper, 'Hyperlipidemia'] = 'YES'

mask_no_hyper = (
    (patient_df['Hyperlipidemia'] == 'UNKNOWN') &
    (patient_df['Obesity'] == 'NO') &
    (patient_df['Diabetes'] == 'NO') &
    (patient_df['High Blood Pressure'] == 'NO') &
    (patient_df['Heart Attack'] == 'NO') &
    (patient_df['Stroke'] == 'NO') &
    (patient_df['Other Cardiac'] == 'NO')
)
patient_df.loc[mask_no_hyper, 'Hyperlipidemia'] = 'NO'

mask_yes_diabetes = (
    (patient_df['Diabetes'] == 'UNKNOWN') &
    (patient_df['Obesity'] == 'YES') &
    (
        (patient_df['High Blood Pressure'] == 'YES') |
        (patient_df['Hyperlipidemia'] == 'YES') |
        (patient_df['Heart Attack'] == 'YES') |
        (patient_df['Other Cardiac'] == 'YES')
    )
)
patient_df.loc[mask_yes_diabetes, 'Diabetes'] = 'YES'

mask_no_diabetes = (
    (patient_df['Diabetes'] == 'UNKNOWN') &
    (patient_df['Obesity'] == 'NO') &
    (patient_df['High Blood Pressure'] == 'NO') &
    (patient_df['Hyperlipidemia'] == 'NO') &
    (patient_df['Heart Attack'] == 'NO') &
    (patient_df['Other Cardiac'] == 'NO')
)
patient_df.loc[mask_no_diabetes, 'Diabetes'] = 'NO'

mask_yes_obesity = (
    (patient_df['Obesity'] == 'UNKNOWN') &
    (
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['High Blood Pressure'] == 'YES') |
        (patient_df['Hyperlipidemia'] == 'YES') |
        (patient_df['Heart Attack'] == 'YES') |
        (patient_df['Stroke'] == 'YES') |
        (patient_df['Other Cardiac'] == 'YES') |
        (patient_df['Joint Disease'] == 'YES')
    )
)
patient_df.loc[mask_yes_obesity, 'Obesity'] = 'YES'

mask_no_obesity = (
    (patient_df['Obesity'] == 'UNKNOWN') &
    (patient_df['Diabetes'] == 'NO') &
    (patient_df['High Blood Pressure'] == 'NO') &
    (patient_df['Hyperlipidemia'] == 'NO') &
    (patient_df['Heart Attack'] == 'NO') &
    (patient_df['Stroke'] == 'NO') &
    (patient_df['Other Cardiac'] == 'NO') &
    (patient_df['Joint Disease'] == 'NO')
)
patient_df.loc[mask_no_obesity, 'Obesity'] = 'NO'

mask_yes_heart_attack = (
    (patient_df['Heart Attack'] == 'UNKNOWN') &
    (
        (patient_df['High Blood Pressure'] == 'YES') |
        (patient_df['Hyperlipidemia'] == 'YES') |
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['Obesity'] == 'YES') |
        (patient_df['Other Cardiac'] == 'YES') |
        (patient_df['Stroke'] == 'YES')
    )
)
patient_df.loc[mask_yes_heart_attack, 'Heart Attack'] = 'YES'

mask_no_heart_attack = (
    (patient_df['Heart Attack'] == 'UNKNOWN') &
    (patient_df['High Blood Pressure'] == 'NO') &
    (patient_df['Hyperlipidemia'] == 'NO') &
    (patient_df['Diabetes'] == 'NO') &
    (patient_df['Obesity'] == 'NO') &
    (patient_df['Other Cardiac'] == 'NO') &
    (patient_df['Stroke'] == 'NO')
)
patient_df.loc[mask_no_heart_attack, 'Heart Attack'] = 'NO'

mask_yes_stroke = (
  (patient_df['Stroke'] == 'UNKNOWN') &
    (
        (patient_df['High Blood Pressure'] == 'YES') |
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['Heart Attack'] == 'YES') |
        (patient_df['Hyperlipidemia'] == 'YES') |
        (patient_df['Other Cardiac'] == 'YES') |
        (patient_df['Obesity'] == 'YES')
    )
)
patient_df.loc[mask_yes_stroke, 'Stroke'] = 'YES'

mask_no_stroke = (
    (patient_df['Stroke'] == 'UNKNOWN') &
    (patient_df['High Blood Pressure'] == 'NO') &
    (patient_df['Diabetes'] == 'NO') &
    (patient_df['Heart Attack'] == 'NO') &
    (patient_df['Hyperlipidemia'] == 'NO') &
    (patient_df['Other Cardiac'] == 'NO') &
    (patient_df['Obesity'] == 'NO')
)
patient_df.loc[mask_no_stroke, 'Stroke'] = 'NO'

mask_yes_other_cardiac = (
    (patient_df['Other Cardiac'] == 'UNKNOWN') &
    (
        (patient_df['High Blood Pressure'] == 'YES') |
        (patient_df['Hyperlipidemia'] == 'YES') |
        (patient_df['Heart Attack'] == 'YES') |
        (patient_df['Stroke'] == 'YES') |
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['Obesity'] == 'YES')
    )
)
patient_df.loc[mask_yes_other_cardiac, 'Other Cardiac'] = 'YES'

mask_no_other_cardiac = (
    (patient_df['Other Cardiac'] == 'UNKNOWN') &
    (patient_df['High Blood Pressure'] == 'NO') &
    (patient_df['Hyperlipidemia'] == 'NO') &
    (patient_df['Heart Attack'] == 'NO') &
    (patient_df['Stroke'] == 'NO') &
    (patient_df['Diabetes'] == 'NO') &
    (patient_df['Obesity'] == 'NO')
)
patient_df.loc[mask_no_other_cardiac, 'Other Cardiac'] = 'NO'

mask_yes_asthma = (
    (patient_df['Pulmonary Asthma'] == 'UNKNOWN') &
    (
        (patient_df['Smokes'] == 'YES') |
        (patient_df['Obesity'] == 'YES') |
        (patient_df['Cannabis Recreational Use'] == 'YES') |
        (patient_df['Cannabis Medicinal Use'] == 'YES') |
        (patient_df['Other Chronic Med Condition'] == 'YES')
    )
)
patient_df.loc[mask_yes_asthma, 'Pulmonary Asthma'] = 'YES'

mask_no_asthma = (
    (patient_df['Pulmonary Asthma'] == 'UNKNOWN') &
    (patient_df['Smokes'] == 'NO') &
    (patient_df['Obesity'] == 'NO') &
    (patient_df['Cannabis Recreational Use'] == 'NO') &
    (patient_df['Cannabis Medicinal Use'] == 'NO') &
    (patient_df['Other Chronic Med Condition'] == 'NO')
)
patient_df.loc[mask_no_asthma, 'Pulmonary Asthma'] = 'NO'

mask_yes_dementia = (
    (patient_df['Alzheimer or Dementia'] == 'UNKNOWN') &
    (patient_df['Age Group'] == 'ADULT') &
    (
        (patient_df['Neurological Condition'] == 'YES') |
        (patient_df['Traumatic Brain Injury'] == 'YES') |
        (patient_df['Veteran Status'] == 'YES')
    )
)
patient_df.loc[mask_yes_dementia, 'Alzheimer or Dementia'] = 'YES'

mask_no_dementia = (
    (patient_df['Alzheimer or Dementia'] == 'UNKNOWN') &
    (patient_df['Age Group'] == 'CHILD') &
    (patient_df['Neurological Condition'] == 'NO') &
    (patient_df['Traumatic Brain Injury'] == 'NO')
)
patient_df.loc[mask_no_dementia, 'Alzheimer or Dementia'] = 'NO'

mask_yes_kidney = (
    (patient_df['Kidney Disease'] == 'UNKNOWN') &
    (
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['High Blood Pressure'] == 'YES') |
        (patient_df['Heart Attack'] == 'YES') |
        (patient_df['Other Cardiac'] == 'YES') |
        (patient_df['Obesity'] == 'YES') |
        (patient_df['Hyperlipidemia'] == 'YES')
    )
)
patient_df.loc[mask_yes_kidney, 'Kidney Disease'] = 'YES'

mask_no_kidney = (
    (patient_df['Kidney Disease'] == 'UNKNOWN') &
    (patient_df['Diabetes'] == 'NO') &
    (patient_df['High Blood Pressure'] == 'NO') &
    (patient_df['Heart Attack'] == 'NO') &
    (patient_df['Other Cardiac'] == 'NO') &
    (patient_df['Obesity'] == 'NO') &
    (patient_df['Hyperlipidemia'] == 'NO')
)
patient_df.loc[mask_no_kidney, 'Kidney Disease'] = 'NO'

mask_yes_liver = (
    (patient_df['Liver Disease'] == 'UNKNOWN') &
    (
        (patient_df['Alcohol Related Disorder'] == 'YES') |
        (patient_df['Drug Substance Disorder'] == 'YES') |
        (patient_df['Obesity'] == 'YES') |
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['Hyperlipidemia'] == 'YES')
    )
)
patient_df.loc[mask_yes_liver, 'Liver Disease'] = 'YES'

mask_no_liver = (
    (patient_df['Liver Disease'] == 'UNKNOWN') &
    (patient_df['Alcohol Related Disorder'] == 'NO') &
    (patient_df['Drug Substance Disorder'] == 'NO') &
    (patient_df['Obesity'] == 'NO') &
    (patient_df['Diabetes'] == 'NO') &
    (patient_df['Hyperlipidemia'] == 'NO')
)
patient_df.loc[mask_no_liver, 'Liver Disease'] = 'NO'

mask_yes_endocrine = (
    (patient_df['Endocrine Condition'] == 'UNKNOWN') &
    (
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['Obesity'] == 'YES') |
        (patient_df['Hyperlipidemia'] == 'YES') |
        (patient_df['High Blood Pressure'] == 'YES') |
        (patient_df['Other Chronic Med Condition'] == 'YES')
    )
)
patient_df.loc[mask_yes_endocrine, 'Endocrine Condition'] = 'YES'

mask_no_endocrine = (
    (patient_df['Endocrine Condition'] == 'UNKNOWN') &
    (patient_df['Diabetes'] == 'NO') &
    (patient_df['Obesity'] == 'NO') &
    (patient_df['Hyperlipidemia'] == 'NO') &
    (patient_df['High Blood Pressure'] == 'NO') &
    (patient_df['Other Chronic Med Condition'] == 'NO')
)
patient_df.loc[mask_no_endocrine, 'Endocrine Condition'] = 'NO'

mask_yes_neuro = (
    (patient_df['Neurological Condition'] == 'UNKNOWN') &
    (
        (patient_df['Traumatic Brain Injury'] == 'YES') |
        (patient_df['Alzheimer or Dementia'] == 'YES') |
        (patient_df['Stroke'] == 'YES') |
        (patient_df['Autism Spectrum'] == 'YES') |
        (patient_df['Other Developmental Disability'] == 'YES')
    )
)
patient_df.loc[mask_yes_neuro, 'Neurological Condition'] = 'YES'

mask_no_neuro = (
    (patient_df['Neurological Condition'] == 'UNKNOWN') &
    (patient_df['Traumatic Brain Injury'] == 'NO') &
    (patient_df['Alzheimer or Dementia'] == 'NO') &
    (patient_df['Stroke'] == 'NO') &
    (patient_df['Autism Spectrum'] == 'NO') &
    (patient_df['Other Developmental Disability'] == 'NO')
)
patient_df.loc[mask_no_neuro, 'Neurological Condition'] = 'NO'

mask_yes_tbi = (
    (patient_df['Traumatic Brain Injury'] == 'UNKNOWN') &
    (
        (patient_df['Neurological Condition'] == 'YES') |
        (patient_df['Stroke'] == 'YES') |
        (patient_df['Alzheimer or Dementia'] == 'YES') |
        (patient_df['Other Developmental Disability'] == 'YES')
    )
)

patient_df.loc[mask_yes_tbi, 'Traumatic Brain Injury'] = 'YES'

mask_no_tbi = (
    (patient_df['Traumatic Brain Injury'] == 'UNKNOWN') &
    (patient_df['Neurological Condition'] == 'NO') &
    (patient_df['Stroke'] == 'NO') &
    (patient_df['Alzheimer or Dementia'] == 'NO') &
    (patient_df['Other Developmental Disability'] == 'NO')
)

patient_df.loc[mask_no_tbi, 'Traumatic Brain Injury'] = 'NO'

mask_yes_joint_disease = (
    (patient_df['Joint Disease'] == 'UNKNOWN') &
    (
        (patient_df['Obesity'] == 'YES') |
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['Mobility Impairment Disorder'] == 'YES') |
        (patient_df['Age Group'] == 'ADULT')
    )
)
patient_df.loc[mask_yes_joint_disease, 'Joint Disease'] = 'YES'

mask_no_joint_disease = (
    (patient_df['Joint Disease'] == 'UNKNOWN') &
    (patient_df['Obesity'] == 'NO') &
    (patient_df['Diabetes'] == 'NO') &
    (patient_df['Mobility Impairment Disorder'] == 'NO') &
    (patient_df['Age Group'] == 'CHILD')
)
patient_df.loc[mask_no_joint_disease, 'Joint Disease'] = 'NO'

mask_yes_cancer = (
    (patient_df['Cancer'] == 'UNKNOWN') &
    (
        (patient_df['Age Group'] == 'ADULT') &
        (
            (patient_df['Smokes'] == 'YES') |
            (patient_df['Alcohol Related Disorder'] == 'YES') |
            (patient_df['Liver Disease'] == 'YES') |
            (patient_df['Other Chronic Med Condition'] == 'YES')
        )
    )
)
patient_df.loc[mask_yes_cancer, 'Cancer'] = 'YES'

mask_no_cancer = (
    (patient_df['Cancer'] == 'UNKNOWN') &
    (patient_df['Age Group'] == 'CHILD') &
    (patient_df['Smokes'] == 'NO') &
    (patient_df['Alcohol Related Disorder'] == 'NO') &
    (patient_df['Other Chronic Med Condition'] == 'NO')
)
patient_df.loc[mask_no_cancer, 'Cancer'] = 'NO'

mask_yes_other_chronic = (
    (patient_df['Other Chronic Med Condition'] == 'UNKNOWN') &
    (
        (patient_df['Obesity'] == 'YES') |
        (patient_df['Diabetes'] == 'YES') |
        (patient_df['High Blood Pressure'] == 'YES') |
        (patient_df['Joint Disease'] == 'YES') |
        (patient_df['Liver Disease'] == 'YES') |
        (patient_df['Kidney Disease'] == 'YES') |
        (patient_df['Endocrine Condition'] == 'YES') |
        (patient_df['Neurological Condition'] == 'YES') |
        (patient_df['Pulmonary Asthma'] == 'YES')
    )
)
patient_df.loc[mask_yes_other_chronic, 'Other Chronic Med Condition'] = 'YES'

mask_no_other_chronic = (
    (patient_df['Other Chronic Med Condition'] == 'UNKNOWN') &
    (patient_df[['Obesity', 'Diabetes', 'High Blood Pressure', 'Joint Disease',
                 'Liver Disease', 'Kidney Disease', 'Endocrine Condition',
                 'Neurological Condition', 'Pulmonary Asthma']].eq('NO').all(axis=1)) # because these values are colmnns
)
patient_df.loc[mask_no_other_chronic, 'Other Chronic Med Condition'] = 'NO'

chronic_conditions = [
    'Obesity', 'Diabetes', 'High Blood Pressure', 'Joint Disease',
    'Liver Disease', 'Kidney Disease', 'Endocrine Condition',
    'Neurological Condition', 'Pulmonary Asthma', 'Cancer',
    'Other Chronic Med Condition'
]

mask_yes_no_chronic = (
    (patient_df['No Chronic Med Condition'] == 'UNKNOWN') &
    (patient_df[chronic_conditions].eq('NO').all(axis=1))
)

patient_df.loc[mask_yes_no_chronic, 'No Chronic Med Condition'] = 'YES'

chronic_conditions = [
    'Obesity', 'Diabetes', 'High Blood Pressure', 'Joint Disease',
    'Liver Disease', 'Kidney Disease', 'Endocrine Condition',
    'Neurological Condition', 'Pulmonary Asthma', 'Cancer',
    'Other Chronic Med Condition'
]

mask_no_no_chronic = (
    (patient_df['No Chronic Med Condition'] == 'UNKNOWN') &
    (patient_df[chronic_conditions].eq('YES').any(axis=1))
)

patient_df.loc[mask_no_no_chronic, 'No Chronic Med Condition'] = 'NO'

# List of related chronic condition columns
chronic_conditions = [
    'Obesity', 'Diabetes', 'High Blood Pressure', 'Joint Disease',
    'Liver Disease', 'Kidney Disease', 'Endocrine Condition',
    'Neurological Condition', 'Pulmonary Asthma', 'Cancer',
    'Other Chronic Med Condition'
]

# Mask where Unknown Chronic Med Condition is UNKNOWN, and any related chronic condition is UNKNOWN
mask_unknown_chronic = (
    (patient_df['Unknown Chronic Med Condition'] == 'UNKNOWN') &
    (patient_df[chronic_conditions].eq('UNKNOWN').any(axis=1))
)

patient_df.loc[mask_unknown_chronic, 'Unknown Chronic Med Condition'] = 'YES'

# Optional: fill remaining UNKNOWNs as NO if no related UNKNOWN conditions
mask_no_unknown_chronic = (
    (patient_df['Unknown Chronic Med Condition'] == 'UNKNOWN') &
    (patient_df[chronic_conditions].eq('UNKNOWN').any(axis=1) == False)
)

patient_df.loc[mask_no_unknown_chronic, 'Unknown Chronic Med Condition'] = 'NO'

mask_yes_cannabis_recreational = (
    (patient_df['Cannabis Recreational Use'] == 'UNKNOWN') &
    (
        (patient_df['Drug Substance Disorder'] == 'YES') |
        (patient_df['Opioid Related Disorder'] == 'YES') |
        (patient_df['Alcohol Related Disorder'] == 'YES') |
        (patient_df['Cannabis Medicinal Use'] == 'YES') |
        (patient_df['Smokes'] == 'YES')
    )
)

patient_df.loc[mask_yes_cannabis_recreational, 'Cannabis Recreational Use'] = 'YES'

mask_no_cannabis_recreational = (
    (patient_df['Cannabis Recreational Use'] == 'UNKNOWN') &
    ~mask_yes_cannabis_recreational  # those not flagged above
)

patient_df.loc[mask_no_cannabis_recreational, 'Cannabis Recreational Use'] = 'NO'

mask_yes_cannabis_medicinal = (
    (patient_df['Cannabis Medicinal Use'] == 'UNKNOWN') &
    (
        (patient_df['Cannabis Recreational Use'] == 'NO') &
        (
            (patient_df['Neurological Condition'] == 'YES') |
            (patient_df['Cancer'] == 'YES') |
            (patient_df['Other Chronic Med Condition'] == 'YES')  # if this covers relevant conditions
        )
    )
)

patient_df.loc[mask_yes_cannabis_medicinal, 'Cannabis Medicinal Use'] = 'YES'

mask_no_cannabis_medicinal = (
    (patient_df['Cannabis Medicinal Use'] == 'UNKNOWN') &
    ~mask_yes_cannabis_medicinal
)

patient_df.loc[mask_no_cannabis_medicinal, 'Cannabis Medicinal Use'] = 'NO'

mask_yes_smokes = (
    (patient_df['Smokes'] == 'UNKNOWN') &
    (
        (patient_df['Received Smoking Medication'] == 'YES') |
        (patient_df['Received Smoking Counseling'] == 'YES')
    )
)

patient_df.loc[mask_yes_smokes, 'Smokes'] = 'YES'

mask_no_smokes = (
    (patient_df['Smokes'] == 'UNKNOWN') &
    ~mask_yes_smokes
)

patient_df.loc[mask_no_smokes, 'Smokes'] = 'NO'

mask_yes_medication = (
    (patient_df['Received Smoking Medication'] == 'UNKNOWN') &
    (
        (patient_df['Smokes'] == 'YES') |
        (patient_df['Received Smoking Counseling'] == 'YES')
    )
)

patient_df.loc[mask_yes_medication, 'Received Smoking Medication'] = 'YES'

mask_no_medication = (
    (patient_df['Received Smoking Medication'] == 'UNKNOWN') &
    ~mask_yes_medication
)

patient_df.loc[mask_no_medication, 'Received Smoking Medication'] = 'NO'

mask_yes_counseling = (
    (patient_df['Received Smoking Counseling'] == 'UNKNOWN') &
    (
        (patient_df['Smokes'] == 'YES') |
        (patient_df['Received Smoking Medication'] == 'YES')
    )
)

patient_df.loc[mask_yes_counseling, 'Received Smoking Counseling'] = 'YES'

mask_no_counseling = (
    (patient_df['Received Smoking Counseling'] == 'UNKNOWN') &
    ~mask_yes_counseling
)

patient_df.loc[mask_no_counseling, 'Received Smoking Counseling'] = 'NO'

mask_yes_smi = (
    (patient_df['Serious Mental Illness'] == 'UNKNOWN') &
    (
        (patient_df['Mental Illness'] == 'YES') |
        (patient_df['Principal Diagnosis Class'].str.contains('Serious Mental Illness|Schizophrenia|Bipolar', na=False)) |
        (patient_df['Additional Diagnosis Class'].str.contains('Serious Mental Illness|Schizophrenia|Bipolar', na=False))
    )
)

patient_df.loc[mask_yes_smi, 'Serious Mental Illness'] = 'YES'

mask_no_smi = (
    (patient_df['Serious Mental Illness'] == 'UNKNOWN') &
    (patient_df['Mental Illness'] == 'NO') &
    (~patient_df['Principal Diagnosis Class'].str.contains('Serious Mental Illness|Schizophrenia|Bipolar', na=False)) &
    (~patient_df['Additional Diagnosis Class'].str.contains('Serious Mental Illness|Schizophrenia|Bipolar', na=False))
)

patient_df.loc[mask_no_smi, 'Serious Mental Illness'] = 'NO'

# Fill UNKNOWN with YES if related conditions indicate likely service
mask_yes = (
    (patient_df['Alcohol 12m Service'] == 'UNKNOWN') &
    (
        (patient_df['Alcohol Related Disorder'] == 'YES') |
        (patient_df['Serious Mental Illness'] == 'YES')
    )
)
patient_df.loc[mask_yes, 'Alcohol 12m Service'] = 'YES'

# Fill remaining UNKNOWN with NO
mask_no = (patient_df['Alcohol 12m Service'] == 'UNKNOWN')
patient_df.loc[mask_no, 'Alcohol 12m Service'] = 'NO'

# Fill 'YES' where opioid disorder or serious mental illness is present
mask_yes_opioid = (
    (patient_df['Opioid 12m Service'] == 'UNKNOWN') &
    (
        (patient_df['Opioid Related Disorder'] == 'YES') |
        (patient_df['Serious Mental Illness'] == 'YES')
    )
)
patient_df.loc[mask_yes_opioid, 'Opioid 12m Service'] = 'YES'

# Fill remaining UNKNOWN with 'NO'
mask_no_opioid = (patient_df['Opioid 12m Service'] == 'UNKNOWN')
patient_df.loc[mask_no_opioid, 'Opioid 12m Service'] = 'NO'

mask_yes_drug_service = (
    (patient_df['Drug/Substance 12m Service'] == 'UNKNOWN') &
    (
        (patient_df['Drug Substance Disorder'] == 'YES') |
        (patient_df['Opioid Related Disorder'] == 'YES') |
        (patient_df['Cannabis Recreational Use'] == 'YES') |
        (patient_df['Cannabis Medicinal Use'] == 'YES') |
        (patient_df['Smokes'] == 'YES')
    )
)
patient_df.loc[mask_yes_drug_service, 'Drug/Substance 12m Service'] = 'YES'

# Fill the rest of the UNKNOWNs with 'NO'
mask_no_drug_service = (patient_df['Drug/Substance 12m Service'] == 'UNKNOWN')
patient_df.loc[mask_no_drug_service, 'Drug/Substance 12m Service'] = 'NO'

mask_yes_ssi = (
    (patient_df['SSI Cash Assistance'] == 'UNKNOWN') &
    (
        (patient_df['Serious Mental Illness'] == 'YES') |
        (patient_df['Intellectual Disability'] == 'YES') |
        (patient_df['Autism Spectrum'] == 'YES') |
        (patient_df['Other Developmental Disability'] == 'YES') |
        (patient_df['Veterans Disability Benefits'] == 'YES') |
        (patient_df['Public Assistance Cash Program'] == 'YES') |
        (patient_df['Other Cash Benefits'] == 'YES')
    )
)

patient_df.loc[mask_yes_ssi, 'SSI Cash Assistance'] = 'YES'

# Remaining UNKNOWNs → NO
mask_no_ssi = (patient_df['SSI Cash Assistance'] == 'UNKNOWN')
patient_df.loc[mask_no_ssi, 'SSI Cash Assistance'] = 'NO'

mask_yes_ssdi = (
    (patient_df['SSDI Cash Assistance'] == 'UNKNOWN') &
    (
        (patient_df['Serious Mental Illness'] == 'YES') |
        (patient_df['Intellectual Disability'] == 'YES') |
        (patient_df['Autism Spectrum'] == 'YES') |
        (patient_df['Other Developmental Disability'] == 'YES') |
        (patient_df['Veterans Disability Benefits'] == 'YES') |
        (patient_df['Other Cash Benefits'] == 'YES') |
        (patient_df['Veterans Cash Assistance'] == 'YES')
    )
)

patient_df.loc[mask_yes_ssdi, 'SSDI Cash Assistance'] = 'YES'

# Fill remaining UNKNOWNs with 'NO'
mask_no_ssdi = (patient_df['SSDI Cash Assistance'] == 'UNKNOWN')
patient_df.loc[mask_no_ssdi, 'SSDI Cash Assistance'] = 'NO'

mask_yes_vet_disability = (
    (patient_df['Veterans Disability Benefits'] == 'UNKNOWN') &
    (patient_df['Veteran Status'] == 'YES') &
    (
        (patient_df['Serious Mental Illness'] == 'YES') |
        (patient_df['Intellectual Disability'] == 'YES') |
        (patient_df['Other Developmental Disability'] == 'YES') |
        (patient_df['Mobility Impairment Disorder'] == 'YES') |
        (patient_df['Hearing Impairment'] == 'YES') |
        (patient_df['Visual Impairment'] == 'YES') |
        (patient_df['Speech Impairment'] == 'YES') |
        (patient_df['Traumatic Brain Injury'] == 'YES')
    )
)

patient_df.loc[mask_yes_vet_disability, 'Veterans Disability Benefits'] = 'YES'

# Remaining UNKNOWNs can be safely set to NO
mask_no_vet_disability = (patient_df['Veterans Disability Benefits'] == 'UNKNOWN')
patient_df.loc[mask_no_vet_disability, 'Veterans Disability Benefits'] = 'NO'

mask_yes_vet_cash = (
    (patient_df['Veterans Cash Assistance'] == 'UNKNOWN') &
    (patient_df['Veteran Status'] == 'YES') &
    (
        (patient_df['Veterans Disability Benefits'] == 'YES') |
        (patient_df['SSI Cash Assistance'] == 'YES') |
        (patient_df['SSDI Cash Assistance'] == 'YES')
    )
)

patient_df.loc[mask_yes_vet_cash, 'Veterans Cash Assistance'] = 'YES'

# Remaining UNKNOWNs can be set to NO if no indication of assistance
mask_no_vet_cash = (patient_df['Veterans Cash Assistance'] == 'UNKNOWN')
patient_df.loc[mask_no_vet_cash, 'Veterans Cash Assistance'] = 'NO'

mask_yes_public_cash = (
    (patient_df['Public Assistance Cash Program'] == 'UNKNOWN') &
    (
        (patient_df['SSI Cash Assistance'] == 'YES') |
        (patient_df['SSDI Cash Assistance'] == 'YES') |
        (patient_df['Veterans Cash Assistance'] == 'YES')
    )
)

patient_df.loc[mask_yes_public_cash, 'Public Assistance Cash Program'] = 'YES'

mask_no_public_cash = (
    (patient_df['Public Assistance Cash Program'] == 'UNKNOWN') &
    (
        (patient_df['SSI Cash Assistance'] == 'NO') &
        (patient_df['SSDI Cash Assistance'] == 'NO') &
        (patient_df['Veterans Cash Assistance'] == 'NO')
    )
)

patient_df.loc[mask_no_public_cash, 'Public Assistance Cash Program'] = 'NO'

mask_yes_other_cash = (
    (patient_df['Other Cash Benefits'] == 'UNKNOWN') &
    (
        (patient_df['SSI Cash Assistance'] == 'YES') |
        (patient_df['SSDI Cash Assistance'] == 'YES') |
        (patient_df['Veterans Cash Assistance'] == 'YES') |
        (patient_df['Public Assistance Cash Program'] == 'YES')
    )
)

patient_df.loc[mask_yes_other_cash, 'Other Cash Benefits'] = 'YES'

mask_no_other_cash = (
    (patient_df['Other Cash Benefits'] == 'UNKNOWN') &
    (
        (patient_df['SSI Cash Assistance'] == 'NO') &
        (patient_df['SSDI Cash Assistance'] == 'NO') &
        (patient_df['Veterans Cash Assistance'] == 'NO') &
        (patient_df['Public Assistance Cash Program'] == 'NO')
    )
)

patient_df.loc[mask_no_other_cash, 'Other Cash Benefits'] = 'NO'

insurance_cols = [
    'Medicaid and Medicare Insurance',
    'Medicaid Insurance',
    'Medicaid Managed Insurance',
    'Medicare Insurance',
    'Private Insurance',
    'Child Health Plus Insurance',
    'Other Insurance'
]

# 1. Fill UNKNOWN with 'NO' if any insurance = 'YES'
mask_no_no_insurance = (
    (patient_df['No Insurance'] == 'UNKNOWN') &
    (patient_df[insurance_cols].eq('YES').any(axis=1))
)
patient_df.loc[mask_no_no_insurance, 'No Insurance'] = 'NO'

# 2. Fill UNKNOWN with 'YES' if all insurance = 'NO'
mask_yes_no_insurance = (
    (patient_df['No Insurance'] == 'UNKNOWN') &
    (patient_df[insurance_cols].eq('NO').all(axis=1))
)
patient_df.loc[mask_yes_no_insurance, 'No Insurance'] = 'YES'

# 3. Leave the rest as UNKNOWN (no change)
# Fill Medicare Insurance = NO if age group is CHILD (unlikely to have Medicare)
mask_no_medicare_child = (
    (patient_df['Medicare Insurance'] == 'UNKNOWN') &
    (patient_df['Age Group'] == 'CHILD')
)
patient_df.loc[mask_no_medicare_child, 'Medicare Insurance'] = 'NO'

# Fill Medicare Insurance = YES if Medicaid and Medicare combined insurance is YES
mask_yes_medicare_combined = (
    (patient_df['Medicare Insurance'] == 'UNKNOWN') &
    (patient_df['Medicaid and Medicare Insurance'] == 'YES')
)
patient_df.loc[mask_yes_medicare_combined, 'Medicare Insurance'] = 'YES'

# For adults without Medicare info, you can either keep UNKNOWN or fill based on age if available
other_insurance_cols = [
    'Medicaid and Medicare Insurance',
    'Medicaid Insurance',
    'Medicaid Managed Insurance',
    'Medicare Insurance',
    'Child Health Plus Insurance',
    'Other Insurance'
]

# 1. If Private Insurance is UNKNOWN but any other public insurance is YES, likely NO
mask_private_no = (
    (patient_df['Private Insurance'] == 'UNKNOWN') &
    (patient_df[other_insurance_cols].eq('YES').any(axis=1))
)
patient_df.loc[mask_private_no, 'Private Insurance'] = 'NO'

# 2. If Private Insurance is UNKNOWN and all other insurance are NO, fill with YES or keep UNKNOWN based on domain knowledge
mask_private_yes = (
    (patient_df['Private Insurance'] == 'UNKNOWN') &
    (patient_df[other_insurance_cols].eq('NO').all(axis=1))
)
patient_df.loc[mask_private_yes, 'Private Insurance'] = 'YES'  # or 'UNKNOWN' if unsure

# If Child Health Plus Insurance is UNKNOWN and Age Group is ADULT, mark NO
mask_no_child_health_plus = (
    (patient_df['Child Health Plus Insurance'] == 'UNKNOWN') &
    (patient_df['Age Group'] == 'ADULT')
)
patient_df.loc[mask_no_child_health_plus, 'Child Health Plus Insurance'] = 'NO'

# If Child Health Plus Insurance is UNKNOWN and Medicaid Insurance is YES, mark YES (some overlap possible)
mask_yes_child_health_plus = (
    (patient_df['Child Health Plus Insurance'] == 'UNKNOWN') &
    (patient_df['Medicaid Insurance'] == 'YES')
)
patient_df.loc[mask_yes_child_health_plus, 'Child Health Plus Insurance'] = 'YES'

insurance_cols = [
    'Medicaid and Medicare Insurance',
    'Medicaid Insurance',
    'Medicaid Managed Insurance',
    'Medicare Insurance',
    'Private Insurance',
    'Child Health Plus Insurance'
]

mask_other_no = (
    (patient_df['Other Insurance'] == 'UNKNOWN') &
    (patient_df[insurance_cols].eq('NO').all(axis=1))
)
patient_df.loc[mask_other_no, 'Other Insurance'] = 'NO'

# Optionally, if any other insurance is YES, keep UNKNOWN or fill as NO
mask_other_unknown = (
    (patient_df['Other Insurance'] == 'UNKNOWN') &
    (patient_df[insurance_cols].eq('YES').any(axis=1))
)
# You might choose to keep it UNKNOWN or set NO, depending on your data
# patient_df.loc[mask_other_unknown, 'Other Insurance'] = 'NO'

# If Criminal Justice Status is UNKNOWN and no evidence of involvement, fill NO
mask_no_cjs = (
    (patient_df['Criminal Justice Status'] == 'UNKNOWN')
    # you can add any conditions here if you have other related columns
)
patient_df.loc[mask_no_cjs, 'Criminal Justice Status'] = 'NO'

patient_df.columns = patient_df.columns.str.strip()  # Removes leading/trailing spaces this is important do this before converting to 0 and 1

patient_df.columns


