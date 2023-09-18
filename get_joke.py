import requests

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
    data = response.json()
    return data["joke"]

if __name__ == "__main__":
    joke = get_joke()
    print(joke)
