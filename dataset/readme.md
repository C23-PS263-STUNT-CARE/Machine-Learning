# Stunting Dataset

The Stunting Dataset is a comprehensive dataset that comprises 7 features and corresponding labels. The dataset was collected from various health centers in the surrounding area. To enhance the dataset's diversity and representativeness, synthetic data was generated using statistical similarity techniques.

## Dataset Information

The dataset consists of a total of 6500 cases, encompassing two categories: stunting and non-stunting. Stunting refers to impaired growth and development in children due to chronic malnutrition, while non-stunting represents cases where this condition is not observed.

## Feature Information 
Additional Feature Information for the Stunting Dataset:

-Age: Represents the age of the child in months.
Unit: Months

-Birth Weight: Refers to the weight of the child at birth.
Unit: Kilograms (kg)

-Body Weight: Indicates the current weight of the child.
Unit: Kilograms (kg)

-Birth Length: Represents the length of the child at birth.
Unit: Centimeters (cm)

-Body Length: Indicates the current length of the child.
Unit: Centimeters (cm)

Please note that the dataset utilizes the specified units for each respective feature to maintain consistency and facilitate accurate analysis.
## Dataset Details

- Features: The dataset contains 7 informative features that are crucial in understanding the stunting phenomenon.
- Labels: The dataset includes corresponding labels that categorize each case as either stunting or non-stunting.
- Total Cases: The dataset comprises 5000 cases, with 1812 cases classified as stunting and 3188 cases classified as non-stunting.
  - Then, the dataset will be: 

    | Stunting | Label | Amount
    |------------|------|------|
    | Yes | 1 | 1812 |
    | No  | 0 | 3188 |
    <br>
  - Since the datasets is super imbalanced, so we decide to balancing the dataset with increase the minor case which is Stunting condition using synthetic data so the datasets is changed to:
  
    | Stunting | Label | Amount
    |------------|------|------|
    | Yes | 1 | 3312 |
    | No | 0 | 3188 |
    <br>
## Dataset Source

The dataset was collected by conducting surveys and assessments in collaboration with local health centers and experts in the field. Samples were carefully selected to ensure a diverse representation of individuals in the target population. To enrich the dataset and address potential limitations of real-world data, synthetic data was generated using statistical techniques to create additional instances that closely resemble the observed patterns and characteristics.

## Potential Use Cases

The Stunting Dataset can be utilized for a variety of purposes, including but not limited to:

- Analyzing the prevalence and risk factors associated with stunting
- Developing predictive models to identify individuals at risk of stunting
- Exploring the impact of various interventions and policies on stunting prevalence
- Investigating the relationship between stunting and other health outcomes or socioeconomic factors

Researchers, practitioners, and policymakers in the field of public health, nutrition, and child development can leverage this dataset to gain valuable insights into stunting and devise evidence-based strategies to address this critical issue.

## Data Quality and Preprocessing

Great care was taken to ensure the quality and reliability of the collected data. Rigorous data cleaning and preprocessing techniques were applied to minimize errors and inconsistencies. However, it is essential to conduct thorough validation and verification of the data before using it for specific analysis or modeling purposes. Detailed documentation regarding data preprocessing steps and quality assurance procedures can be found in the accompanying documentation files.

## License and Citation

The Stunting Dataset is made available under a specific license. Please refer to the LICENSE file for detailed information on the terms of use, redistribution, and attribution requirements.

If you utilize this dataset in your research, projects, or any other work, we kindly request that you acknowledge its source by citing it as follows:

[Stunting Dataset](https://www.kaggle.com/datasets/muhtarom/stunting-dataset) - Stunting Dataset, 2023

Please note that while considerable effort has been made to ensure the accuracy and reliability of the dataset, the creators and contributors cannot guarantee its completeness or suitability for any specific purpose. Users are advised to exercise caution and perform due diligence when working with the dataset.

For any inquiries or collaborations related to the dataset, please contact [Muhtarom Ahkam Maulana](muhtaromahkam0@gmail.com), [Salma Atsila Shabiyya](salmaatsilashabiyya@gmail.com).

