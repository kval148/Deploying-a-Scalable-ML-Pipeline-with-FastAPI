# Model Card

## Model Details
> **Model Version:** 1.0.0
> 
> **Author:** Katherine Austin created this model using code and templates provided by Udacity course instructors.
> 
> **Overview:** This model uses a Random Forest Classifier with the default parameters from scikit-learn 1.5.1.

## Intended Use
> This model is designed to predict whether an individual has a salary >50K or not, based off of values in the other remaining attributes. Users of this model may include those interested in targeted marketing or fundraising campaigns or those interested in using this model for educational purposes.

## Training Data
> The data was obtained from the [Census Dataset](https://archive.ics.uci.edu/dataset/20/census+income) from the UC Irvine Machine Learning Repository. The original dataset has 32561 records and was split into training and testing sets using an 80-20 split, respectively. Due to a 25-75 class imbalance between those with a salary >50K or not, respectively, stratification was done on the target `salary` column. Before fitting the model, the data was processed using a One Hot Encoder on categorical columns and a Label Binarizer on the target `salary` column.

## Evaluation Data
> The test data set was used to evaluate the model and consists of 20% of the original dataset, stratified on the `salary` column.

## Metrics
> The model's overall performance was evaluated using precision, recall, and F1 scores, which were 0.7353, 0.6378, and 0.6831, respectively.

## Ethical Considerations
> This dataset contains data pertaining to protected classes, such as race, sex, and national origin. Since this dataset includes a direct relationship between individuals and their salary level, this model has the potential to impact people of different socio-economic backgrounds differently, depending on the use and intent of those using this model. The data itself and resulting model may also include some degree of society error bias.

## Caveats and Recommendations
> This model is currently version 1.0.0 and is not intended as a final product. The performance metrics for this model can almost certainly be improved following additional data processing, model selection, and hyperparameter tuning. For example, there are currently missing values encoded into the dataset that have not yet been removed. Removing records with missing values will likely reduce noise and increase model performance. Also, model comparisons and hyperparameter tuning have not yet been completed, but are recommended for future versions. As such, use of the current model is not advised until a more refined version is released.
