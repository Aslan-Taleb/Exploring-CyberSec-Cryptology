import requests

def UsernameGenerator():
    try:
        result = requests.get("https://api.namefake.com/")
        result.raise_for_status()
        result = result.json()
        result = result["maiden_name"]
        return result
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        return None
    except KeyError as e:
        # Handle the case where the JSON response does not have a "maiden_name" key
        print(f"KeyError: {e}")
        return None
