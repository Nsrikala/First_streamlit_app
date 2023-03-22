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
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show =my_fruit_list.loc[fruit_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
streamlit.header('Fruityvice fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice )
#streamlit.text(fruityvice_response.json()) #just writes the data to screen

#take the Json version of responce and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output the screan as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("the fruit load list contains:")

streamlit.text(my_data_row)
