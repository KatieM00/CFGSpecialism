# Theory Questions
### 1.1 
The role of a data scientist involves collecting, cleaning, analyzing, and interpreting large amounts of data to extract insights that can be used to improve business/ research decisions.
### 1.2 
An outlier is a data point that differs significantly from other data points in a set. Outliers can be caused by a variety of factors, such as errors in data collection or measurement, or by the presence of rare or unusual events.

Some examples are: A height of 7 feet in a dataset of human heights, or a test score of 100% in a class of students who typically score in the 70s and 80s.

The decision of whether or not to remove outliers depends on the specific dataset and the purpose of the analysis. In some cases, outliers can be legitimate data points that should not be removed. For example, if the dataset includes the heights of professional basketball players, a height of 7 feet would not be considered an outlier. However, in other cases, outliers may be caused by errors or anomalies in the data, and removing them may improve the accuracy of the analysis.
### 1.3

Data cleaning is the process of identifying and correcting errors, inconsistencies, and missing data in a dataset.

Data cleaning is important for a number of reasons, including:

-   To improve the accuracy and reliability of the data. 
-   To make the data more consistent and easier to understand.
-   To remove any errors or anomalies that could skew the results of any analysis.
-   To make the data more useful for decision-making.

Most common mistakes are: 

- Missing data
- Duplicated data
- Inconsistent data
- Corrupted data
- Outliers
- Human errors e.g. typos

### 1.4 

Unsupervised learning is a type of machine learning where the algorithm learns from unlabeled data. The algorithm does not have any prior knowledge about the labels, so it must find patterns in the data itself. Clustering is a type of unsupervised learning that is used to group similar data points together.

Unsupervised learning is used in a variety of applications, including:

- Customer segmentation (Group customers together based on their purchase behaviourm demographicsm or other).
- Data compression (Compress data by grouping similar data points together. This can save space and improve the efficiency of data storage and retrieval)
- Image segmentation (Segment images into different regions. Used for tasks such as object detection and recognition)
- Natural language processing (Group words together based on their meaning. Used for tasks such as text classification and sentiment analysis).

*Real world Application*

One possible real-world application of unsupervised learning is to group customers together based on their purchase behavior. This information can be used to develop targeted marketing campaigns. For example, a retailer could cluster its customers into groups based on their spending habits, age, or location. Then, the retailer could target different marketing campaigns to each group.

*Limitations* 

One of the main limitations of unsupervised learning is that it can be difficult to interpret the results. The algorithm may find patterns in the data that are not meaningful or relevant to the problem at hand. Another limitation is that unsupervised learning can be computationally expensive, especially for large datasets

### 1.5

Supervised learning is a type of machine learning where the algorithm learns from labeled data. The algorithm is given a set of data points, each of which has a label that indicates the desired output. The algorithm then learns to map the input data to the output labels.

Supervised learning is used in a variety of applications:

- Classification (The algorithm learns to classify data points into different categories such as images, or to classift text such as positive or negative sentiment)
- Regression (Predict a continuous value, e.g. price of a house)
- Recommendation systems (Recommend products or services to users. Could be used to recommend movies to users based on their past viewing history)
- Fraud detection (Detect fraudulent transactions. Detect credit card fraud by analysing the patterns of spending)

*Real world applications*

One possible real-world application of supervised learning is to classify spam emails. This can be done by training an algorithm on a dataset of emails that have already been labeled as spam or ham. The algorithm can then learn to identify the features that are common in spam emails, and use these features to classify new emails.

*What is needed*

Labelled data to know the desired output for each data point. 

*What you should consider*

- Missing data
- Outliers
- Normalisation
- Feature selection (Features that are most relevant to the problem should be selected)