import streamlit
streamlit.title('my parents new healthy dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 🥑🍞 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacado toaste')
streamlit.header('BUILD YOUR OWN FRUIT SMOOTHIE')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
