import asyncio
import requests

# Type aliases for JSON data handling
JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
"""Type alias for JSON data, supporting nested structures."""
JSONObject = dict[str, JSON]
"""Type alias for a JSON object, representing key-value pairs."""
JSONList = list[JSON]
"""Type alias for a list of JSON data."""


def http_get_sync(url: str) -> JSONObject:
    """
    Performs a synchronous HTTP GET request to a specified URL.

    This function uses the requests library to make a synchronous HTTP GET request
    and returns the response in JSON format.

    Parameters:
    - url (str): The URL to which the HTTP GET request is to be made.

    Returns:
    - JSONObject: The JSON response from the HTTP GET request as a dictionary.
    """
    response = requests.get(url)
    return response.json()


async def http_get(url: str) -> JSONObject:
    """
    Performs an asynchronous HTTP GET request to a specified URL.

    This function wraps the synchronous http_get_sync function in an asynchronous
    call, allowing it to be called in asynchronous code. It uses asyncio.to_thread
    to run the synchronous function in a separate thread, thereby not blocking the
    event loop.

    Parameters:
    - url (str): The URL to which the HTTP GET request is to be made.

    Returns:
    - JSONObject: The JSON response from the HTTP GET request as a dictionary.
    """
    return await asyncio.to_thread(http_get_sync, url)
