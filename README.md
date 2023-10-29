# Stack_overflow-2023_analysis-salary-prediction

To Explore Interactive Visualizations which Designed by with Plotly: Access the Kaggle Notebook [Here]([https://www.kaggle.com/code/mbhosseini70/stack-overflow-2023-salary-prediction]):


[](url)
The primary objective of this project is to conduct a comprehensive data analysis on a selected column from the Stack Overflow Developer Survey 2023 dataset, extracting valuable insights from the data.

Additionally, I aim to develop a predictive model for determining developer salaries. This endeavor will facilitate a deeper understanding of the key factors influencing developer salaries.

Furthermore, I plan to create a user-friendly web application using Streamlit, which will be hosted on my GitHub repository for the broader data science community.
**Link:** 

**During our modeling phase, we implemented XGBoost, CatBoost, and a Neural Network model. However, the best Mean Absolute Error (MAE) we achieved was around 23,000, which is not a very satisfactory result. This indicates that there is room for improvement in our models. If you have any suggestions or insights on how I could enhance the model's performance, please feel free to share them. Your expertise and recommendations are invaluable, and they will contribute significantly to the optimization of this predictive model.**

**Additionally, your feedback and suggestions are highly valued. If you have any comments or insights that could enhance the quality of this notebook and contribute to my personal growth in this field, I would greatly appreciate your input. Thank you for your support!**




## Crucial Findings from the Data Analysis Segment:

**Demographics of Developers:**

* A significant 57% of developers fall within the age bracket of under 34 years old, highlighting the youthfulness of the developer community.

**Work Arrangements:**

* The preferred work arrangement among developers is hybrid work, which combines remote and in-person work, showcasing the adaptability of the workforce.

**Remote Work Preference:**

* Approximately one-third of developers express a preference for remote work, reflecting the growing popularity of flexible work environments.

**Company Size:**

* One-third of developers are employed by small or medium-sized organizations, indicating the diversity in the scale of the companies that engage with developers.

**Specializations:**

* A significant 50% of developers are engaged in website programming, making it the dominant specialization within the developer community.

**Data Science and ML Engineers:**

* A minority, less than two percent, are working in the fields of data science or machine learning engineering, suggesting these areas remain relatively niche.

**Geographic Distribution:**

* Roughly one-third of developers are based in the United States, underlining the country's continued prominence in the tech industry.

**Salary Disparity:**

* Developers in the United States enjoy significantly higher salaries compared to their counterparts in other countries, emphasizing the economic differences within the global developer workforce.


## Crucial Findings from the Model Development:

1. Dominance of 'Country':

* In both models, the 'Country' feature significantly influences the predictions, highlighting the critical role of geographic location on the salary. It’s crucial to note that this high dominance doesn’t necessarily imply causation, and other underlying factors related to the country, such as cost of living, economic conditions, and employment opportunities, might be contributing to this observed effect.

2. Importance of Three Features in Both Models:

* Both models consistently identify 'Country', 'DevType', and 'YearsCodePro' as important features, although they assign different levels of importance to each. This consistency across different algorithms underscores the significance of these features in predicting the dependent variable. It also indicates that geographic location, job role, and professional coding experience play crucial roles in the model's predictions.

3. Remote Work, Organization Size, and Education Level:

* While 'RemoteWork', 'OrgSize', and 'EdLevel' do contribute to the models' predictions, their impact is substantially less compared to 'Country', 'DevType', and 'YearsCodePro'.

4. Age and Educational Level:

* The age of the developer and their educational background appear to have a minimal impact on the salary, holding the least significance among the factors considered in the model. 
