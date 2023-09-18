def data_visualisation():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    
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

    st.title("Data Visualisation")

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