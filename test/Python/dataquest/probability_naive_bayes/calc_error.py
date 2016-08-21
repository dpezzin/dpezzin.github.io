#!/usr/bin/env python


# Now that we know the predictions, we'll compute error using the area under the ROC curve. 
# This will tell us how "good" the model is -- closer to 1 means that the model is better.
# Computing error is very important to knowing when your model is "good", and when it is 
# getting better or worse.
actual = [int(r[1]) for r in test]

from sklearn import metrics

# Generate the roc curve using scikits-learn.
fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)

# Measure the area under the curve.  The closer to 1, the "better" the predictions.
print("AUC of the predictions: {0}".format(metrics.auc(fpr, tpr)))
