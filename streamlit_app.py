import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header( 'Breakfast Favorites')

streamlit.text('Omega 3 & Blueberry Oatmeal') 
streamlit.text ('03 Kale, Spinach & Rocket Smoothie')
streamlit.text ('4 Hard-Boiled Free-Range Egg')
streamlit.text ('Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)) #display the table on the page
streamlit.dataframe (my_fruit_list)


# adding new code here

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit macros.txt")
my fruit list = my fruit list.set index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe (my fruit list)
