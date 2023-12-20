import requests

def download_audio_from_github(username, repository, filename, destination):
    url = f'https://raw.githubusercontent.com/{username}/{repository}/main/{filename}'
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print("Download successful!")
    else:
        print(f"Failed to download. Status code: {response.status_code}")

# Call the function with specific values
download_audio_from_github('Avzzzzz', 'Sih-', 'test1.wav', 'local_test1.wav')
