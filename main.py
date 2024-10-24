import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Excel Data Visualizer", layout="wide")

st.title("Excel Data Visualization Tool")

# File uploader
uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls'])

if uploaded_file is not None:
    # Load the data
    df = pd.read_excel(uploaded_file)
    
    # Show raw data
    st.subheader("Raw Data Preview")
    st.dataframe(df.head())
    
    # Column selection
    st.subheader("Create Visualization")
    
    # Select chart type
    chart_type = st.selectbox(
        "Select Chart Type",
        ["Line Plot", "Bar Chart", "Scatter Plot", "Box Plot"]
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        x_axis = st.selectbox("Select X-axis", df.columns)
    with col2:
        y_axis = st.selectbox("Select Y-axis", df.columns)
    
    # Create visualization based on selection
    if st.button("Generate Plot"):
        st.subheader("Visualization")
        
        if chart_type == "Line Plot":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
            
        elif chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
            
        elif chart_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
            
        elif chart_type == "Box Plot":
            fig = px.box(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
        
        # Update layout
        fig.update_layout(
            xaxis_title=x_axis,
            yaxis_title=y_axis,
            template="plotly_white",
            height=600
        )
        
        # Display the plot
        st.plotly_chart(fig, use_container_width=True)
        
        # Display basic statistics
        st.subheader("Basic Statistics")
        st.write(df[[x_axis, y_axis]].describe())

# Add sidebar with instructions
with st.sidebar:
    st.header("Instructions")
    st.write("""
    1. Upload your Excel file using the file uploader
    2. Preview your data in the raw data section
    3. Select the type of chart you want to create
    4. Choose columns for X and Y axes
    5. Click 'Generate Plot' to create the visualization
    """)
    
    st.header("About")
    st.write("""
    This app allows you to quickly visualize data from Excel files.
    You can create various types of plots and view basic statistics.
    """)
