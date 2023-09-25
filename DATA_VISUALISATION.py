def data_visualisation():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import matplotlib.pyplot as plt
    
    
    wine_data = pd.read_csv('winequality-red.csv')

    clean_data = wine_data.drop("residual sugar", axis = 1)

    #replace alcohol outlier with mean
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['alcohol'] = grouped['alcohol'].transform(replace_outliers_with_mean)

    #replace fixed acidity outlier with mean
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['fixed acidity'] = grouped['fixed acidity'].transform(replace_outliers_with_mean)

    #remove volatile acidity outlier
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['volatile acidity'] = grouped['volatile acidity'].transform(replace_outliers_with_mean)

    #remove citric acid outlier
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['citric acid'] = grouped['citric acid'].transform(replace_outliers_with_mean)

    #remove chloride outlier
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['chlorides'] = grouped['chlorides'].transform(replace_outliers_with_mean)

    #remove free sulfur dioxide outlier
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['free sulfur dioxide'] = grouped['free sulfur dioxide'].transform(replace_outliers_with_mean)

    #remove total sulfur dioxide outlier
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['total sulfur dioxide'] = grouped['total sulfur dioxide'].transform(replace_outliers_with_mean)

    #remove density outlier
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['density'] = grouped['density'].transform(replace_outliers_with_mean)

    #remove pH outlier
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['pH'] = grouped['pH'].transform(replace_outliers_with_mean)

    #remove sulphates outlier
    def replace_outliers_with_mean(data):
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
        return data

    # Group the data by quality
    grouped = clean_data.groupby('quality')

    # Replace the outlier values of alcohol with mean for each quality group
    clean_data['sulphates'] = grouped['sulphates'].transform(replace_outliers_with_mean)

    # Categorize the data
    cat_data = []
    for each in clean_data.quality:
        if 4 >= each >= 3:
            cat_data.append(0)
        elif 6 >= each >= 5:
            cat_data.append(1)
        else:
            cat_data.append(2)

    # Create a new dataframe with the same columns as the original dataframe
    new_data = clean_data.copy()

    # Add the categorized data to the new dataframe
    new_data['quality'] = cat_data

    # Get the value counts of the target variable
    class_counts = new_data['quality'].value_counts()

    st.title("Data Visualisation on 'quality'")
    st.write("The feature variable 'quality' serves as the focal point in this machine learning project, as it represents the target variable of paramount significance. Therefore, it is imperative to commence the analysis by delving into a comprehensive examination of the target variable itself.")

    st.subheader("Variable 'Quality' before Categorisation")#---------------------------------------------------------
    st.write("The charts below shown the feature variable 'Quality' before cetegorisation has been made. It can be observed that the highest percentage count is in the category of '5,' with a count of 42.6%. Furthermore, the category '6' also has a significant percentage, accounting for '39.9%' of the dataset. Both of these categories dominate the entire dataset, followed by the categories '7,' '4', '8', and lastly, '3'.")
    # Get the feature values and labels
    feature_values = wine_data['quality'].value_counts().values
    feature_labels = wine_data['quality'].value_counts().index

    # Create a DataFrame for the pie chart
    data = pd.DataFrame({'Value': feature_labels, 'Count': feature_values})

    # Create an interactive pie chart using Plotly Express
    quality_pie = px.pie(data, values='Count', names='Value', title='Pie Chart:',
                hover_data=['Value', 'Count'], labels={'Value': 'Quality'})
    
    # Create an interactive bar chart using Plotly Express
    quality_bar = px.bar(data, x='Value', y='Count', title='Bar Chart:',
                labels={'Value': 'Quality', 'Count': 'Count'})

    # Display the interactive plot using Streamlit
    st.plotly_chart(quality_pie)
    
    # Display the interactive plot using Streamlit
    st.plotly_chart(quality_bar)

    st.subheader("Variable 'Quality' after Categorisation")#---------------------------------------------------------
    st.write("The charts below shown the feature variable 'Quality' after cetegorisation has been made. The categories have been grouped into '0,' '1,' and '2,' with class '1' almost dominating the dataset, followed by '2,' and then '0.' This data format will later assist in building a more efficient machine learning model.")
    # Get the feature values and labels
    feature_values = new_data['quality'].value_counts().values
    feature_labels = new_data['quality'].value_counts().index

    # Create a DataFrame for the pie chart
    data = pd.DataFrame({'Value': feature_labels, 'Count': feature_values})

    # Create an interactive pie chart using Plotly Express
    quality_pie = px.pie(data, values='Count', names='Value', title='Pie Chart:',
                hover_data=['Value', 'Count'], labels={'Value': 'Quality'})
    
    # Create an interactive bar chart using Plotly Express
    quality_bar = px.bar(data, x='Value', y='Count', title='Bar Chart:',
                labels={'Value': 'Quality', 'Count': 'Count'})

    # Display the interactive plot using Streamlit
    st.plotly_chart(quality_pie)
    
    # Display the interactive plot using Streamlit
    st.plotly_chart(quality_bar)
    

#----------------------------------------------------------------------------------------------
    # Correlation Matrix
    # Calculate the correlation matrix
    corr = wine_data.corr(method='pearson')

    # Streamlit app
    st.title("Correlation Matrix")
    st.write("To drop a feature variable from the wine dataset, a correlation matrix must be evaluated. In the matrix, it can be concluded that the feature variable “residual sugar” has the least correlation to “quality” and other feature variables as well. Therefore, the developer has decided to drop this feature variable.")

    # Create a heatmap using Plotly Express with the 'Viridis' colorscale
    fig = px.imshow(corr, color_continuous_scale='Viridis')
    fig.update_layout(
        xaxis=dict(title='Feature Variables'),
        yaxis=dict(title='Features Variables')
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)

#------------------------------------------------------------------------------------------------------

    st.title("Feature Variables by 'quality'")
    st.write("Each of the feature variables in the dataset is visualized in the form of a bar chart, allowing for a comprehensive exploration of the data and facilitating the extraction of valuable insights to inform decision-making within the wine industry. These visual representations serve as a powerful tool for discerning patterns, trends, and correlations, aiding in the assessment of factors influencing wine quality, production processes, and market strategies.")

#------------------------------------------------------------------------------------------------
    #fixed acidity by quality 

    st.subheader("Mean Fixed Acidity by Quality")
    st.write("Based on the visualisation, there are no specific patterns or trends to discuss about the visualisation insights.")

    # Calculate the mean fixed acidity by quality
    mean_Fixed_Acidity = clean_data.groupby('quality')['fixed acidity'].mean().reset_index()

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_Fixed_Acidity, x='quality', y='fixed acidity')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='Fixed Acidity (g)')

    # Display the plot in Streamlit
    st.plotly_chart(fig)
#---------------------------------------------------------------------------------------------------------
    #volatile acidity by quality 

    st.subheader("Mean Volatile Acidity by Quality")
    st.write("The visualisation shown a very obvious pattern can be seen is that the higher the mean “volatile acidity”, the lower the “quality”. On the other hand, the lower the mean “volatile acidity”, the higher the wine quality. It can also be observed that the quality of 7 and 8 has quite close average volatile acidity. Therefore, to maintain a good wine quality, the winemaker should restrict the content of volatile acidity to below 0.40 grams per wine. ")

    # Calculate the mean fixed acidity by quality
    mean_volatile_acidity = clean_data.groupby('quality')['volatile acidity'].mean().reset_index()

    # Create a bar plot using Plotly Express
    fig = px.bar( mean_volatile_acidity, x='quality', y='volatile acidity')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='Volatile Acidity (g)')

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    #---------------------------------------------------------------------------------------------------
    #citric acidity by quality 

    # Calculate the mean citric acid by quality
    mean_citric_acid = clean_data.groupby('quality')['citric acid'].mean().reset_index()

    # Streamlit app
    st.subheader("Mean Citric Acid by Quality")
    st.write("Mean “citric acid” that falls below around 0.2 gram are in the “quality” category from 3 to 4, mean “citric acid” that falls above around 0.2 but below 0.3 gram are in the “quality” category from 5 to 6. With the mean “citric acid” of 0.39 and above, the wine will be able to hit a quality score of 7 to 8. Therefore, the winemaker should ensure that their wine at least contain 0.39 gram of citric acid to maintain a quality score of 7 and above.")

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_citric_acid, x='quality', y='citric acid')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='Citric Acid (g)')

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    #------------------------------------------------------------------------------------------
    #chlorides by quality

    # Calculate the mean chlorides by quality
    mean_chlorides = clean_data.groupby('quality')['chlorides'].mean().reset_index()

    # Streamlit app
    st.subheader("Mean Chlorides by Quality")
    st.write("Based on the visualisation, the “quality” of 3 has the highest “chlorides” among all classes. However, starting from “quality” 5, a pattern can be observed. The lower the “chlorides” content, the higher the “quality” becomes. To maintain the quality score of 8, the chlorides content should fall on 0.068 gram or below. Therefore, the winemaker should take note that one’s should not have too much chlorides in the wine or else the wine will fall under the low-quality category of 3. Because the quality of 4, 5 and 6 have similar average “chlorides”, it is not wise to maintain the chlorides content around 0.7 gram. Thus, the winemaker should ensure the chlorides content falls on or under 0.68 gram.")

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_chlorides, x='quality', y='chlorides')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='Chlorides (g)')

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    #----------------------------------------------------------------------------------------------
    #free sulfur dioxide by quality 

    # Calculate the mean free sulfur dioxide by quality
    mean_free_sulfur_dioxide = clean_data.groupby('quality')['free sulfur dioxide'].mean().reset_index()

    # Streamlit app
    st.subheader("Mean Free Sulfur Dioxide by Quality")
    st.write("Feature variable “free sulfur dioxide” should be avoided to fall in 8.7 milligram. This is because the wine quality will only score 3. On the other hand, if the wine wants the ideal “free sulfur dioxide” content to produce good wine, maintaining around 10.5 is not a good idea because both quality of 4 and 8 have a very close “free sulfur dioxide” content. Therefore, the winemaker can consider to maintain the content in 12.75 milligram to have a solid quality score of 7.")

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_free_sulfur_dioxide, x='quality', y='free sulfur dioxide')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='Free Sulfur Dioxide (mg)')

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    #----------------------------------------------------------------------------------------------
    #total sulfur dioxide by quality 

    # Calculate the mean free sulfur dioxide by quality
    mean_total_sulfur_dioxide = clean_data.groupby('quality')['total sulfur dioxide'].mean().reset_index()

    # Streamlit app
    st.subheader("Mean Total Sulfur Dioxide by Quality")
    st.write("Based on the visualisation, the data is quite uncertain. Some of the available insights is that the “total sulfur dioxide” should not contained 24.9 milligram or below as the wine quality will only score 3 points. To maintain a stable wine quality, the winemaker should restrict the total sulfur dioxide in between 27.438 to 29.217 milligram content. ")

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_total_sulfur_dioxide, x='quality', y='total sulfur dioxide')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='Total Sulfur Dioxide (mg)')

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    #----------------------------------------------------------------------------------------------------
    #density by quality
    # Calculate the mean density by quality
    mean_density = clean_data.groupby('quality')['density'].mean().reset_index()

    # Streamlit app
    st.subheader("Mean Density by Quality")
    st.write("Based on the visualisation, all quality categories have similar density. Therefore, density is not a very important feature variables to be considered.")

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_density, x='quality', y='density')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='Density (g/cm³)')

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    #----------------------------------------------------------------------------------------------------
    #pH by quality
    # Calculate the mean pH by quality
    mean_pH = clean_data.groupby('quality')['pH'].mean().reset_index()

    # Streamlit app
    st.subheader("pH by Quality")
    st.write("Based on the visualisation, a pattern can be seen that the lower the “pH”, the higher the “quality”. In that case, the higher the “pH”, the lower the “quality”. It can be summarised that even though the range of mean “pH” for each of the quality categories has not significance different, but a very small difference can highly affect the wine quality. To maintain a good wine quality, the winemaker should restrict the pH value to 3.28 and below. ")

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_pH, x='quality', y='pH')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='pH')

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    #-------------------------------------------------------------------------------------
    #sulphates by quality
    # Calculate the mean sulfate levels by quality
    mean_sulfates = clean_data.groupby('quality')['sulphates'].mean().reset_index()

    # Streamlit app
    st.subheader("Sulfates by Quality")
    st.write("The visualisation shown that as the mean “sulphates” decrease, the “quality” decrease. On the other hand, as the mean “sulphates” increase, the “quality” also increased. To maintain a good wine quality, the winemaker should ensure that the sulphates content of the wine is at least 0.73 gram and above to maintain the quality score of 7 to 8.")

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_sulfates, x='quality', y='sulphates')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='Sulfates (g)')

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    #-------------------------------------------------------------------------------------------------
    #alcohol by quality 
    # Calculate the mean alcohol content by quality
    mean_alcohol = clean_data.groupby('quality')['alcohol'].mean().reset_index()

    # Streamlit app
    st.subheader("Alcohol Content by Quality")
    st.write("Based on the visualisation, the quality score of 3 to 6 has the alcohol content ranging from 9.8% to 10.6%. On the other hand, quality score of 7 and above has alcohol content of 11% and above. The quality score of 8 has the highest alcohol content of among all the classes. Therefore, to produce a wine with a score of 7 and above, the winemaker should ensure that their wine alcohol content is above 11% content. Not only that, the winemaker could also produce the wine up to 12% alcohol content to give a shot in getting quality 8.")

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_alcohol, x='quality', y='alcohol')

    # Customize the axis labels
    fig.update_xaxes(title_text='Quality')
    fig.update_yaxes(title_text='Alcohol (%)')

    # Display the plot in Streamlit
    st.plotly_chart(fig)









