# Day 20 — ML Foundations Summary

## 1. Decision Trees

A Decision Tree is a supervised learning algorithm that makes predictions through a sequence of feature-based splits.

- **Root node:** The first split in the tree.
- **Internal node:** A decision based on a feature.
- **Branch:** The outcome of a decision.
- **Leaf node:** The final prediction.

### Advantages
- Easy to visualize and interpret.
- Handles nonlinear relationships.
- Requires little feature preprocessing.
- Can work with numerical and categorical features, depending on implementation.

### Limitations
- Deep trees can overfit training data.
- Small data changes may produce a different tree.
- Greedy splitting does not guarantee a globally optimal tree.

Common controls against overfitting include `max_depth`, `min_samples_split`, `min_samples_leaf`, and pruning.

## 2. Gini Impurity

Gini impurity measures how often a randomly selected sample would be incorrectly classified if it were labelled according to the class distribution at a node.

For class proportions \(p_1, p_2, \ldots, p_k\):

**Gini = 1 - sum(p_i^2)**

- Gini = 0 means the node contains only one class.
- Higher values indicate a more mixed class distribution.
- For a binary classification problem with equally represented classes, Gini = 0.5.

Example: a node contains 6 positive and 4 negative samples.

- Positive proportion = 0.6
- Negative proportion = 0.4
- Gini = 1 - (0.6² + 0.4²) = 0.48

A split is evaluated by the weighted impurity of its child nodes. A good split reduces impurity.

## 3. Entropy and Information Gain

Entropy measures uncertainty in the class distribution of a node.

**Entropy = -sum(p_i * log2(p_i))**

For a binary classification node:
- Entropy = 0 when all samples belong to one class.
- Entropy = 1 bit when both classes are equally represented.

Using the previous 60% / 40% example:

Entropy = -(0.6 * log2(0.6) + 0.4 * log2(0.4))
         ≈ 0.971 bits

### Information Gain

Information Gain measures the reduction in entropy after a split.

Information Gain = parent entropy - weighted child entropy

A split with greater information gain reduces uncertainty more. Decision Tree implementations may use Gini impurity or entropy as their splitting criterion.

## 4. Decision Tree vs. Random Forest

| Property | Decision Tree | Random Forest |
|---|---|---|
| Model structure | One tree | Many trees |
| Training data | Usually the full training set | Usually bootstrap samples |
| Feature selection at splits | Searches eligible features | Considers a random subset of features at each split |
| Prediction | One tree's output | Aggregated tree predictions |
| Interpretability | Usually easier to explain | More difficult to explain globally |
| Variance | Can be high | Often lower through ensemble averaging |
| Overfitting risk | High if unconstrained | Often reduced, but not eliminated |
| Compute cost | Lower | Higher |
| Main strength | Simplicity and interpretability | Robust predictive performance |

For classification, a Random Forest commonly uses majority voting or averages class probabilities. For regression, it commonly averages predictions.

## 5. Bagging (Bootstrap Aggregating)

Bagging trains multiple models on bootstrap samples drawn from the training data.

A bootstrap sample is created by sampling observations **with replacement**, usually producing a sample the same size as the original training set.

### Workflow
1. Draw multiple bootstrap samples from the training set.
2. Train one base model on each sample.
3. Combine predictions from all models.
4. Use voting for classification or averaging for regression.

### Why it helps
- Reduces prediction variance for unstable learners such as Decision Trees.
- Makes the overall model less sensitive to individual training examples.
- Can improve generalization.

Random Forest adds **random feature selection at each split** to bagged Decision Trees. This decorrelates trees, making their combined predictions more effective.

## 6. Feature Scaling

Feature scaling transforms numerical features to comparable scales.

### Standardization (Z-score scaling)

z = (x - mean) / standard deviation

The transformed feature has mean approximately 0 and standard deviation approximately 1 when calculated using the same data.

Useful for:
- Logistic Regression
- Support Vector Machines
- K-Nearest Neighbors
- PCA
- Gradient-based models

### Min-Max Normalization

x_scaled = (x - minimum) / (maximum - minimum)

This usually maps values to the interval [0, 1].

Useful when a bounded feature range is desired. It is sensitive to outliers because extreme values determine the minimum and maximum.

### Robust Scaling

Transforms values using the median and interquartile range:

x_scaled = (x - median) / IQR

This is less sensitive to extreme values than standardization or min-max scaling.

### Do Decision Trees Need Scaling?

Usually, no. Tree-based models split features using thresholds, so monotonic scaling generally preserves the ordering of observations and candidate partitions. Decision Trees and Random Forests typically do not require standardization or min-max scaling.

Scaling is more important for algorithms that depend on distances, dot products, or gradient optimization.

## 7. Avoiding Data Leakage

Fit preprocessing transformations using the training data only. Then apply the learned transformation to validation and test data.

For example:
1. Split data into training and test sets.
2. Fit a scaler on the training features.
3. Transform the training features.
4. Transform test features using that same fitted scaler.

Never fit a scaler on the full dataset before splitting, because information from the test set can leak into training.

## 8. Practical Selection Guide

- Choose a **Decision Tree** when interpretability and a simple decision structure are priorities.
- Choose a **Random Forest** when a strong general-purpose tree-based baseline is needed and additional computation is acceptable.
- Use **Gini impurity** or **entropy/information gain** to evaluate classification splits.
- Use **bagging** to reduce variance by aggregating models trained on bootstrap samples.
- Scale features for distance-based and many gradient-based algorithms; scaling is generally unnecessary for standard tree-based models.

## Key Takeaways

1. Gini impurity and entropy measure node impurity in different ways.
2. Information Gain is the reduction in entropy after a split.
3. Random Forest combines bagging with random feature selection.
4. Ensemble averaging often reduces variance compared with a single tree.
5. Feature scaling is algorithm-dependent; tree models usually do not need it.
6. Fit preprocessing only on training data to avoid data leakage.
