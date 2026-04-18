import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Poll Results Visualizer", page_icon="📊", layout="wide")

# Custom CSS for aesthetics
st.markdown("""
    <style>
    h1 { text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stMetric { 
        background-color: rgba(255, 255, 255, 0.05); 
        padding: 15px; 
        border-radius: 10px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.3); 
        border: 1px solid rgba(255,255,255,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Poll Results Visualizer")
st.markdown("### Interactive Dashboard for Survey & Poll Data Analysis")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv('data/customer_feedback.csv')
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Dataset not found! Please ensure 'data/customer_feedback.csv' exists.")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🎯 Filter Poll Data")
selected_country = st.sidebar.multiselect("Select Country", df['Country'].unique(), default=df['Country'].unique())
selected_gender = st.sidebar.multiselect("Select Gender", df['Gender'].unique(), default=df['Gender'].unique())
selected_loyalty = st.sidebar.multiselect("Select Loyalty Level", df['LoyaltyLevel'].unique(), default=df['LoyaltyLevel'].unique())

filtered_df = df[(df['Country'].isin(selected_country)) & 
                 (df['Gender'].isin(selected_gender)) & 
                 (df['LoyaltyLevel'].isin(selected_loyalty))]

if filtered_df.empty:
    st.warning("No data matches the selected filters. Please adjust your selection.")
    st.stop()

# --- METRICS ---
st.markdown("#### 📈 Key Poll Insights")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Poll Responses", f"{len(filtered_df):,}")
col2.metric("Avg Satisfaction", f"{filtered_df['SatisfactionScore'].mean():.1f}/100")
col3.metric("Avg Product Quality", f"{filtered_df['ProductQuality'].mean():.1f}/10")
col4.metric("Avg Service Quality", f"{filtered_df['ServiceQuality'].mean():.1f}/10")

st.divider()

# --- CHARTS ---
colA, colB = st.columns(2)

with colA:
    st.markdown("#### Respondent Loyalty Distribution")
    fig_pie = px.pie(filtered_df, names='LoyaltyLevel', hole=0.4, 
                     color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig_pie, use_container_width=True)

with colB:
    st.markdown("#### Satisfaction Score by Country")
    country_avg = filtered_df.groupby('Country')['SatisfactionScore'].mean().reset_index()
    country_avg = country_avg.sort_values(by='SatisfactionScore', ascending=False)
    fig_bar = px.bar(country_avg, x='Country', y='SatisfactionScore', text_auto='.1f',
                     color='SatisfactionScore', color_continuous_scale='Blues')
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

colC, colD = st.columns(2)

with colC:
    st.markdown("#### Product vs Service Quality Ratings")
    rating_melt = filtered_df.melt(id_vars=['CustomerID'], value_vars=['ProductQuality', 'ServiceQuality'], 
                                   var_name='Category', value_name='Rating')
    fig_hist = px.histogram(rating_melt, x='Rating', color='Category', barmode='group', nbins=10,
                            color_discrete_sequence=['#4C72B0', '#55A868'])
    st.plotly_chart(fig_hist, use_container_width=True)

with colD:
    st.markdown("#### Feedback Score Distribution")
    fig_feedback = px.histogram(filtered_df, x='FeedbackScore', color='FeedbackScore', 
                                category_orders={"FeedbackScore": ["Low", "Medium", "High"]},
                                color_discrete_map={"Low":"#C44E52", "Medium":"#DD8452", "High":"#55A868"})
    st.plotly_chart(fig_feedback, use_container_width=True)

# --- RAW DATA EXPANDER ---
with st.expander("🔍 View Raw Poll Data"):
    st.dataframe(filtered_df.head(500), use_container_width=True)
