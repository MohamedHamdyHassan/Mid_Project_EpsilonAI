# Glaucoma Detection Dataset
____________________________

### Purpose
> #### --> A dataset containing all the required fields to build AI/ML models to detect glaucoma.

### Description
> #### --> 10,000 records of glaucoma detection dataset, containing:

        -   Patient ID
        -   Age
        -   Gender
        -   Visual Acuity Measurements
        -   Intraocular Pressure (IOP)
        -   Cup-to-Disc Ratio (CDR)
        -   Family History
        -   Medical History
        -   Medication Usage
        -   Visual Field Test Results
        -   Optical Coherence Tomography (OCT) Results
        -   Pachymetry
        -   Cataract Status
        -   Angle Closure Status
        -   Visual Symptoms
        -   Diagnosis
        -   Glaucoma Type

### EDA (Exploratory Data Analysis)

> #### --> Shape(10000,17)
> #### --> Contains Null-values
> #### --> Data Cleaning:

	-  Rename the columns.
	-  Correction the datatype.
	-  I standarized the measurements and changed their names according to the medical concepts.
	-  We have null-values in the medical history, Because there are other reasons that cause the disease, So we made a fillna for it with other.
	-  We have null-values in medical usage, So i found the most common medicine used for glaucoma patients from data via made and created fillna for this medicine. 
	-  I made an adjustment to the visual field test result, Which contains the sensitivity and specificity readings together, So i left each reading in a separate column, I made the same adjustment to the optical coherence tomography (OCT).
	-  We created a new column that includes the number of medications that each patient takes in order to know whether one treatment condition is sufficient to treat the disease according to the diagnosis of the case, Or whether more than one treatment is required.
	-  I changed IOP (Intraocular Pressure) column to categorical data in order to know whether he is has the disease or not, And i specified the ranges, And i made the same adjustment to the CDR(Cup-to-Disc Ratio) and pachymetry.

### Data Analysis
> #### --> Questions:

1)##### The Highst Age that contains patients.
2)##### The ranges of age that can be (Absent or Present) & (Open or Closed).
3)##### The Highst age that have (Glaucoma, No Glaucoma).
4)##### The weight of gender.
5)##### The Highst gender that have family history.
6)##### The Highst Medical History.
7)##### The Highst gender that have medical history.
8)##### The most gender have glaucoma.
9)##### The weight of family history.
10)##### Is it a condition that I have a (family history) or (medical history) of glaucoma?
11)##### The most 5 medication used.
12)##### The relation between visual acuity measurments and age.
13)##### The weight of people visual acuity measurement.
14)##### The Realation between Intraocular Pressure (IOP) and age.
15)##### The Relation between IOP and Diagnosis? 
16)##### The weight of the Cup-to-Disc Ratio (CDR) (Case of Glaucoma, Normal), and the relation between CDR and Diagnosis.
17)##### The Average of Optical Coherence Tomography (OCT) Results.
18)##### The weight of the Pachymetry.
19)##### The Relation between the Pachymetry and Diagnosis.
20)##### The weight of Cataract status and the relation with gender and diagnosis.
21)##### The weight of angle_closure_status.
22)##### How does angle closure affect glaucoma?
23)##### what is the highst type of glaucoma?


> #### --> Insights:

1)##### The Highst age that contains patients is 18 followed by 59.
2)##### We found that the highst age that had closed angle closure is 18 and otherwise that had open angle closure is 70.
3)##### One of the risk factors is advanced age, which is more susceptible to the disease than anything else.
4)##### The weight of the gender is (Male: 50.29%, Female: 49.71).
5)##### The Highst gender that have family history is Male.
6)##### The most medical history that have people is Other followed by Hypertension and Glaucoma in family.
7)##### The most gender that affected by glaucoma is male, while those who do not have it are female.
8)##### Family history is not a major cause of glaucoma.
9)##### The most susceptible medical history to disease is (Diabetes, Hypertension, other).
10)##### The most 5 medication used:
>      - Amoxicillin
>      - Metformin
>      - Atorvastatin	
>      - Ibuprofen
>      - Lisinopril

11)##### We found that there is no strong relationship between age and visual acuity measurement, and that the most common measurement is 6/6. This confirms that visual acuity measurements are not one of the main reasons for identifying the disease.
12)##### The relation between age and Intraocular Pressure (IOP) is strong negative and the most of the people their IOP is Normal.
13)##### we found that the highst people have glaucoma when their IOP is (High IOP) and the highst they don't have glaucoma is (Normal IOP).
14)##### The most people their CDR is (Case of glaucoma: 58.40%), and the other people is (Normal: 39.54%) and we found that the highst people have glaucoma because their CDR is Case of glaucoma itis means that CDR could told me that if itis glaucoma or not.
15)##### The important result that appear if the person have glaucoma or not is RNFL Thickness.
16)##### The most of the people their Pachymetry is (Normal: 5073) and the other (Thick: 4927).
17)##### We found the relation between Pachymetry and IOP, the highest people have High IOP their pachymetry is Thick, and the people that have Normal IOP have Normal pachymetry.
18)##### The Absent people is more than Present, and the males is more than females.
19)##### we found that the most people that have glaucoma their cataract status is Absent .
20)##### The angle_closure_status affect on Glaucoma and the most of people that their angle_closure_status is closed their have glaucoma.
21)##### The highst type of glaucoma is (Juvenile Glaucoma) followed by (Normal-Tension Glaucoma).

### PreProcessing Data
>	- String Operations
>	- Data Cleaning
>	- Detect and Handle Outliers
>	- Work with Categorical data




	