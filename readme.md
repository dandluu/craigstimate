# CRAIGSTIMATE

Access to the live demo: 
[DEMO](https://craigstimate-301619.uc.r.appspot.com/)


Similar to a zillow estimate, Craigstimate attempts to give an estimated rent prediction within a region based on certain features. 

This project contains webscrapped data from craigslist from June of 2020. Approximately 380,000 records were obtained from different regions across the United States and trained using Random Forest Regression. This project represents a time constraint of 2 weeks to complete everything from cleaning, modeling, training, followed by creating a useable application and deploying it to production. Application was built using only Flask. Datebase chosen for this project was Firebase's real-time database to better understand Firebase's ecosystem.

Features that were included in model training:
- Region area
- Housing type
- Square footage
- number of bedrooms
- number of bathrooms
- laundry options
- pets
- smoking

Involved Processes include:
- Data wrangling and cleaning
- Outlier removal 
- Dimensionality reduction
- Possible feature selections/removal
- One Hot Encoding with Column Transformation
- Training with different models
- Cross score validation

### Flaws in data
- Relies on accurate Craiglist postings. A lot of the data was removed due to being nonsensical/outliers but there could still be artifacts within the trained data that might have been missed, see the notebook for a better understanding.
- Data is only trained at one point in time, not dynamically retrained. To better predict rental prices during certain time periods would require webscrapping the data at a more consistent schedule and to redo the data cleaning.
- Scope: The model  attempts to train the data across the United States at once. This is not an ideal approach, ideally to get more precise measurements data would need to be acquired from those regions instead and a better model can be built, and trained regionally
- Currently the data was trained with the removal of state specification (it was under prior assumption that regions would be unique to the state) so there are regions within the United States that have the same name and thus predictions on these regions should not be counted (this can be fixed at a later time, it can be easily removed but it was decided to stay as is for the time being)
- Model is slightly overfitted with certain combination of features


### Next questions to ask / Future Directions
- Should we remove certain features to better predict price? (ie. pets, smoking, laundry, parking options)
- Bin pricing to tiers of luxury, high cost
- Can we dynamically retrain this model every X amounts of months to retrain the model to give more updated rent estimations?
- What would happen if we trained the model using deep learning and neural networks instead of random forest? This would probably result in better predictiors and shorten training time significantly to train on a GPU instead of a CPU. 
- Other ways to avoid overfitting?


Author note: ~~Jupyter Notebooks will be displayed and released as soon as the developer cleans up their notebook.~~ Jupyter Notebook is released.


