# Reviewer Databricks Pipeline



### Extract

In the first screenshot, I am reading through each JSON file (one file contains all reviews for one Steam game) and uploading them into a Pandas Dataframe. This process is to extract the information that is necessary, because the JSON files schema are situated in a difficult manner for Spark to deal with itself.

![image](https://github.com/Ninsta22/reviewer-databricks-pipeline/assets/55768636/147f8c14-7b2f-44bd-964d-8d1176c2547b)

From this second screenshot, now that the pandas dataframe is fully loaded, it is converted to a Spark dataframe, and saved as a Delta Table. Spark makes interacting with a Delta Table incredibly easy and intuitive, and can store the large, unedited, steam review table.

![image](https://github.com/Ninsta22/reviewer-databricks-pipeline/assets/55768636/67888ba2-bb53-4834-abcf-88f655289c93)

### Transform

 Now, in this step, I begin transforming the data. First, I re-load the raw steam review data into a SparkSession, and convert the information to a Spark Dataframe. From here, I utilize Spark to transform the data to only include the columsn that were important, and columns where the weighted_vote_score is greater than 1. An important feature of Delta Lake is Schema Enforcement, so after the transformation, I needed to verify that when I save the transformed data into a new Delta Table, it still conforms to the Delta enforced schema. The benefit of consistency with the same data allowed for easier debugging.

![image](https://github.com/Ninsta22/reviewer-databricks-pipeline/assets/55768636/d4a78770-3e7a-41ba-8cbb-1bf15d5ecbc4)

### Load (Graphic)

Below, I am trying to evaluate concerns surrounding Steams Weighted Vote Score. There are concerns related to how the vote score does not accuratly represent a review's impact to the game. One of the suposed contributions to the metric is the number of comments that are underneath the comment. The graph below shows a scatterplot of weighted vote score and comment count. What was intended was a linear graph, but suprisingly it had little pattern. In fact, it seems a transformation would be necessary for future investigation.

![image](https://github.com/Ninsta22/reviewer-databricks-pipeline/assets/55768636/decbb0f6-9d71-4029-a82c-98e963fa7867)

### Workflow

The following below shows all 3 files previously mentioned stitched together, in order to act as a total Steam Reviewer Pipeline. It will first read in whatever new files are added to Github, and then will be able to constantly create an updated graphic. More importantly however, it will constantly be able to incorporate the contents of a new JSON File review into our totla raw steam review table, more importantly, have our transformed Delta table always updated with this information. As can be seen below, the Workflow is scheduled to run every week at a certain time, which means that it will have weekly updates to the Delta Table. This automates any future work necessary with the steam reviews.

![image](https://github.com/Ninsta22/reviewer-databricks-pipeline/assets/55768636/77cf3956-ced8-46f4-9fcb-028a804505cb)








