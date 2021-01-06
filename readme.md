## Overview

- crawler.py to crawl the wiki pages for the dataset
- model.py creating training and validation datasets, training the model
- classification.ipynb a jupiter notebook to test the classification of the model
- similaritycalc.py a algorithm to calculate the most similar image to a given image from the dataset

### Approach

For the machine learning model I chose a very simple CNN. There are much more sophisticated models out there (ResNet, Inception, Xception). However, due to the nature of the challenge and the small training sample I opted for reduced complexity.

The similarity calculation is done by removing the classification layer of the trained model and then returning a vector with 128 values. This vector is a "compressed" representation of the image. By comparing the vectors with each other, the similarity can be calculated. A database of all training images is created. For each new image the Manhatten distance to all entries in the database is calculated and the closest image is displayed. There are other methods of measuring similarity e.g. Cosine similarty or Euclidian distance. An extensive analysis of the model and testing data could be used to choose the optimal algorithm.

### Challenges

Machine learning has many challenges, in this specific case the amount of training data is limited. Due to some experiments with the similarity algorithms and classification it seams like the model favours the background and color of the cars over design features. 

### improvement

To improve on the current model there are three things I would do.

1. Collect more training data
2. Use a more complex model
3. Use explainable AI

Both 1. and 2. have already been explained in the previous two sections. To improve performance of ML model efficiantly I would use Layer-Wise Relevance Propagation. With this explainable AI method it is possible to visualize the decision process of the model. By doing so, flaws can be spotted and compensated by altering and expanding the trainingdata.

