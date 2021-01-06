## Overview

- crawler.py to crawl the wiki pages for the dataset
- model.py creating training and validation datasets, training the model
- classification.ipynb a jupiter notebook to test the classification of the model
- similaritycalc.py an algorithm to calculate the most similar image to a given image from the dataset

### Approach

For the machine learning model I chose a very simple CNN. There are much more sophisticated models out there (ResNet, Inception, Xception). However, due to the nature of the challenge and the small training sample I opted for reduced complexity.

The similarity calculation is done by removing the classification layer of the trained model and then returning a vector with 128 values. This vector is a "compressed" representation of the image. By comparing the vectors with each other, the similarity can be calculated. A database of all training images is created. For each new image the Manhattan distance to all entries in the database is calculated and the closest image is displayed. There are other methods of measuring similarity e.g. Cosine similarity or Euclidean distance. An extensive analysis of the model and testing data could be used to choose the optimal algorithm.

### Challenges

Machine learning has many challenges, in this specific case the amount of training data is limited. Due to some experiments with the similarity algorithms and classification it seems like the model favors the background and color of the cars over design features. Additionally, the dataset is unbalanced therefore a weighting of the training process is needed.

### Improvement

To improve on the current model there are three things I would do.

1. Collect more training data

More training data would most certainly increase the classification accuracy because the current training set is just too small and uneven. 

1. Use a more complex model

As mentioned above a more complex model could increase accuracy. For this use case a model specialized to recognize small objects such as logos on cars could be explored. As the current model is very low in complexity just using a more complex model could already show improvements.

1. Use explainable AI

To improve performance of ML model efficiently I would use Layer-Wise Relevance Propagation. With this explainable AI method it is possible to visualize the decision process of the model. By doing so, flaws can be spotted and compensated by altering and expanding the training data.