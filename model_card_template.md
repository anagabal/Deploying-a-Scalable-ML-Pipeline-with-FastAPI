# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Ana Gabal created the model. It is a random forest classifier using some customized hyperparameters for n_estimators, max_depth, and min_samples_leaf.

## Intended Use
This model should be used to predict an individuals' salary based off several attributes from census data collection.

## Training Data
Training data is from the census dataset. The data was split by ... the training data is  __% of the original data.

## Evaluation Data
Evaluation data is from the census dataset. The data was split by ... the evaluation data is __% of the original data.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The metrics used to evaluate this model are precission, recall, and F1 score. ((include model metrics here))

## Ethical Considerations
No PII is present in the data used, even though the data was collected from people, they cannot be identified.

## Caveats and Recommendations
This model could be improved by using K-fold cross validation instead of sklearn's train_test_split to split the data into training and testing datasets. 
