import streamlit as st
import pymongo as pm
import requests
import random
import asyncio


from modules import get_random_image




@st.experimental_fragment
async def render_product_card(product: dict):
    """
    Renders a product card with the given product information.

    Args:
        product (dict): A dictionary containing the product information.

    Returns:
        None
    """
    with st.container(border=True):
        st.write(f'##### {product["name"]}')
        with st.container(border=True):

            if 'image' in product:
                st.image(product['image'], width=200)
            else:
                st.image(await get_random_image(product['topics'] if 'topics' in product else ['swimsuit']),
                          width=200)

            for key, value in product.items():
                if key not in ['_id', '$name', 'image']:
                    st.write(f'**{key}**: {value}')

        st.button('Add to cart', key=product['_id']+ 'add')
        st.button('Buy now', key=product['_id']+ 'buy')


