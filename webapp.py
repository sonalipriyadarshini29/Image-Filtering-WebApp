import pandas as pd
import streamlit as st

dresses = pd.read_csv("dress.csv")
dresses.drop("category:confidence", inplace=True, axis=1)
dress_categories = dresses.category.unique()

st.write("""
Simple Web App to filter dresses through category
""")

def user_input_features():
    options = st.multiselect(
        'Which category would you like to view?',
        ['ikat', 'plain', 'polka dot', 'geometry', 'floral', 'squares',
        'scales', 'animal', 'OTHER', 'stripes', 'tribal', 'houndstooth',
        'cartoon', 'chevron', 'stars', 'letter_numb', 'skull'])
    return options

selected_categories = user_input_features()

product_image = []
for i in selected_categories:
    product_image = dresses[dresses['category'].isin(selected_categories)].image_url
for i in product_image:
    st.image(i)
    
# in command line, run -> streamlit run webapp.py