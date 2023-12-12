# This code contains solutions to exercises given by ALX(Holberton) on Async comprehensions.
# Async comprehensions are a feature in Python that allow for the creation of asynchronous generators.
# They are used to simplify the process of writing asynchronous code by allowing for the iteration over asynchronous data sources.
# This directory contains solutions to exercises that demonstrate the use of async comprehensions in Python.
# FILEPATH: async_comprehensions.py

"""
This Directory contains an example of using async comprehensions in Python.

Async comprehensions allow you to asynchronously iterate over a collection of items,
yielding each item as it becomes available. This can be useful for working with
asynchronous data sources, such as web APIs or databases.

In this example, we use an async comprehension to fetch data from a web API in parallel,
using the `aiohttp` library. The `fetch_data` function sends a GET request to the API
for each item in the `urls` list, and returns a list of the responses.

To use this module, simply import the `fetch_data` function and call it with a list of
URLs to fetch data from. The function returns a coroutine object, which you can await
to get the list of responses.

Example usage:

    import asyncio
    from async_comprehensions import fetch_data

    urls = ['https://jsonplaceholder.typicode.com/posts/1', 'https://jsonplaceholder.typicode.com/posts/2']
    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(fetch_data(urls))
    print(responses)

Output:

    [<ClientResponse(https://jsonplaceholder.typicode.com/posts/1) [200 OK]>, <ClientResponse(https://jsonplaceholder.typicode.com/posts/2) [200 OK]>]
"""
