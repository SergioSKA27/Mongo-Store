import streamlit as st
import pymongo as pm
import requests
import random
import asyncio
import uuid
import json


st.set_page_config(page_title='E-commerce App', page_icon='🛒',layout='wide')

@st.cache_resource
def connect_to_mongo(uri):
    client = pm.MongoClient(uri)
    return client

if 'uri' not in st.session_state:
    st.session_state.uri = ''

if 'database' not in st.session_state:
    st.session_state.database = ''


try:
    client = connect_to_mongo(st.session_state.uri)

    st.write(':green[Connected to MongoDB: '+ str(client.server_info()['version']) + ']')

    st.title('DB Conection')

    database = st.selectbox('Select database', client.list_database_names())

    config = {
    'uri': st.session_state.uri,
    'database': database,
    }
    c1, c2 = st.columns([1,1])
    c1.download_button('Download config', data=json.dumps(config), file_name='config.json', mime='application/json')
    c2.button('Conectar', key=uuid.uuid4())

except Exception as e:
    if  len(st.session_state.uri) > 0:
        st.toast('Failed to connect to MongoDB', icon='❌')
    uri = st.text_input('Enter MongoDB connection string',value='mongodb://localhost:27017',placeholder='mongodb://localhost:<port>')
    if st.button('Connect'):
        st.session_state.uri = uri
        st.rerun()






