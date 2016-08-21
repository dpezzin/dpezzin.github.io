#!/usr/bin/env python
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics


# There are a lot of extensions that we could make to this algorithm to make it perform better. 
# We could look at n-grams instead of unigrams. We could remove punctuation and other non-characters. 
# We could remove stopwords. We could also perform stemming or lemmatization.

# We don't want to have to code the whole algorithm out every time, though. 
# An easier way to use naive bayes is to use the implementation in scikit-learn. 
# Scikit-learn is a python machine learning library that contains implementations 
# of all the common machine learning algorithms.

# Generate counts from text using a vectorizer.  There are other vectorizers available, and lots of options you can set.
# This performs our step of computing word counts.
vectorizer = CountVectorizer(stop_words='english')
train_features = vectorizer.fit_transform([r[0] for r in reviews])
test_features = vectorizer.transform([r[0] for r in test])

# Fit a naive bayes model to the training data.
# This will train the model using the word counts we computer, and the existing classifications in the training set.
nb = MultinomialNB()
nb.fit(train_features, [int(r[1]) for r in reviews])

# Now we can use the model to predict classifications for our test features.
predictions = nb.predict(test_features)

# Compute the error.  It is slightly different from our model because the internals of this process work differently from our implementation.
fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
print("Multinomal naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))
