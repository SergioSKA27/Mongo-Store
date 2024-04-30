import requests
import random
import asyncio


async def get_random_image(topics=['swimsuit'], size='600x900'):
    """
    Retrieves a random image from the Unsplash API based on the given topics and size.

    Args:
        topics (list): A list of topics to search for images. Default is ['swimsuit'].
        size (str): The size of the image to retrieve. Default is '600x900'.

    Returns:
        bytes or str: The content of the image as bytes if the request is successful and the status code is 200,
                      or a URL string to a default image if the request fails.

    """
    try:
        response = await asyncio.to_thread(requests.get, f'https://source.unsplash.com/{size}/?{",".join(topics)}',timeout=1)
        return response.content if response.status_code == 200 else f'https://source.unsplash.com/600x900/?{",".join(topics)}'
    except Exception as e:
        return f'https://source.unsplash.com/{size}/?{random.choice(topics)}'

