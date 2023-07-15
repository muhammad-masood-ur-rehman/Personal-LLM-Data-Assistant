import streamlit as st 
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt
import seaborn as sns

heading = '<h1 style="font-family:Courier; color:Orange; font-size: 30px;">Prompt Driven Data Analysis Dashboard</h1>'
st.markdown(heading, unsafe_allow_html=True)


uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

# create an LLM by instantiating OpenAI object, and passing API token
llm = OpenAI(api_token=st.secrets["secret"])


# create PandasAI object, passing the LLM
pandas_ai = PandasAI(llm)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    heading2 = '<h2 style="font-family:Courier; color:Cyan; font-size: 20px;">Data Overview</h2>'
    st.markdown(heading2, unsafe_allow_html=True)
    st.write(df.head(10))

    heading3 = '<h2 style="font-family:Courier; color:Cyan; font-size: 20px;">Prompt Driven Insight</h2>'
    st.markdown(heading3, unsafe_allow_html=True)
    prompt = st.text_area("Enter your prompt:")

    # Generate output
    if st.button("Generate"):
        if prompt:
            # call pandas_ai.run(), passing dataframe and prompt
            with st.spinner("Generating response..."):
                st.write(pandas_ai.run(df, prompt))
        else:
            st.warning("Please enter a prompt.")

    heading4 = '<h2 style="font-family:Courier; color:Cyan; font-size: 20px;">Graphhical Visualization</h2>'
    st.markdown(heading4, unsafe_allow_html=True)

    st.sidebar.header("Visualizations")
    plot_options = ["Bar plot", "Scatter plot", "Histogram", "Box plot"]
    selected_plot = st.sidebar.selectbox("Choose a plot type", plot_options)

    if selected_plot == "Bar plot":
        x_axis = st.sidebar.selectbox("Select x-axis", df.columns)
        y_axis = st.sidebar.selectbox("Select y-axis", df.columns)
        #st.write("Bar plot:")
        fig, ax = plt.subplots()
        sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        st.pyplot(fig)

    elif selected_plot == "Scatter plot":
        x_axis = st.sidebar.selectbox("Select x-axis", df.columns)
        y_axis = st.sidebar.selectbox("Select y-axis", df.columns)
        #st.write("Scatter plot:")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        st.pyplot(fig)

    elif selected_plot == "Histogram":
        column = st.sidebar.selectbox("Select a column", df.columns)
        bins = st.sidebar.slider("Number of bins", 5, 100, 20)
        #st.write("Histogram:")
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=bins, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        st.pyplot(fig)

    elif selected_plot == "Box plot":
        column = st.sidebar.selectbox("Select a column", df.columns)
        #st.write("Box plot:")
        fig, ax = plt.subplots()
        sns.boxplot(df[column], ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        st.pyplot(fig)