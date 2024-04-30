import streamlit as st


st.set_page_config(page_title='E-commerce App', page_icon='🛒',layout='wide')








def main_hero():
    """
    Renders the main hero section of the landing page.

    Returns:
        None
    """

    st.html("""
        <style>
        #MainMenu, header, footer {visibility: hidden;}
        .appview-container .main .block-container
        {
            padding-top: 0.1px;
            padding-left: 0rem;
            padding-right: 0rem;
            padding-bottom: 0.1rem;
        }

        .hero-body {
            background-color: #FD3636;
        }
        .main-hero {
            background-color: #F0F0F052;
            border-radius: 10px;
            padding: 20px;
            margin: 3.5rem;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            gap: 2.5rem;
        }

        @media (max-width: 768px) {
            .main-hero {
                flex-direction: column;
                align-items: center;
            }
        }

        .cta {
            display: flex;
            flex-direction: column;
            margin: 2rem;
            justify-content: center;
            gap: 1rem;
        }


        .hero-button {
            font-size: 1.5rem;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: white;
            width: 200px;
            }
        .hero-button2 {
            font-size: 1.5rem;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: white;
            width: 200px;
            }


        </style>
        <div class="hero-body">
            <div class="main-hero">
                <div class="cta">
                    <h1 style="font-size: 3rem;">¡Bienvenido a nuestra tienda!</h1>
                    <p style="font-size: 1.5rem;">
                    Descubre una amplia selección de productos de alta calidad, especialmente seleccionados para ti.
                    ¡A precios inigualables!
                    </p>
                    <div style="display: flex; flex-direction: row; gap: 1rem;">
                        <button class="hero-button">
                        Comprar Ahora
                        </button>
                        <button class="hero-button2">
                            Ver Productos
                        </button>
                    </div>
                </div>
                <div>
                    <img src="https://source.unsplash.com/600x900/?shopping" style="width: 400px; height: 400px; border-radius: 10px;">
                </div>
            </div>
        </div>
    """)



main_hero()
