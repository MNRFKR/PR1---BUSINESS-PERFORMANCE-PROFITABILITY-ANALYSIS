* **Introduction**

This project focuses on predicting customer Lifetime Value (LTV) using behavioral metrics such as Frequency, Recency, and Average Order Value (AOV).

&nbsp;By applying machine learning models, the goal was to identify high-value customers and segment them into actionable groups for targeted marketing strategies.



* **Abstract**

The task involved building a predictive pipeline that transforms raw transactional data into meaningful features, trains models (Random Forest and XGBoost), and evaluates them using R², RMSE, and MAE. The models achieved very high accuracy, enabling reliable segmentation of customers into Low, Medium, and High LTV tiers. This segmentation provides a foundation for data-driven decision-making in customer retention and growth.



* **Tools Used**

\- Python (Pandas, NumPy) for data preprocessing and feature engineering.

\- Scikit-learn for train/test split, Random Forest modeling, and evaluation metrics.

\- XGBoost for gradient boosting regression.

\- Matplotlib for visualizations (bar charts, scatter plots, box plots, pie charts).

\- Google Colab as the development environment for execution and experimentation.



* **Steps Involved in Building the Project**

\- Data Loading \& Preparation: Imported customer transaction data into a Pandas DataFrame and created a unique Customer\_ID.

\- Feature Engineering: Calculated Frequency (purchase count), Recency (days since last purchase), and AOV (average order value).

\- Target Variable Creation: Summarized total Revenue per customer to serve as the prediction target.

\- Model Training: Split data into train/test sets and trained Random Forest and XGBoost regressors.

\- Model Evaluation: Validated models using R², RMSE, and MAE, confirming strong predictive performance.

\- Segmentation: Grouped customers into Low, Medium, and High LTV tiers using quantile-based thresholds.

\- Visualization: Showcased results with bar graphs, scatter plots, box plots, and pie charts to illustrate accuracy, distribution, and segment proportions.



* ###### Conclusion

The project successfully demonstrated how machine learning can predict customer LTV with high accuracy. Random Forest slightly outperformed XGBoost, but both models provided reliable insights. Segmentation into LTV tiers enables businesses to tailor strategies for retention, upselling, and loyalty programs. Visualizations further enhanced interpretability, making the results actionable for stakeholders.



