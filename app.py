def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

def get_data(url):
    """
    Simulates making a request. 
    This function requires the 'requests' package.
    """
    import requests
    # Use the requests package to simulate a real-world dependency
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        return f"Successfully fetched status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
