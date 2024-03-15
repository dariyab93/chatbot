
# after that, go to bot_code directory and implement a test for existing handler

#checking whether api.py and test.py exist in github directory 
import requests

def check_files_exist(owner, repo, path_to_directory):
    # GitHub API endpoint to get the contents of a repository
    api_url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path_to_directory}'

    # Make a request to the GitHub API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        content_list = response.json()

        # Check if the required files are present
        files_to_check = ['api.py', 'test.py']
        for file in files_to_check:
            if any(entry['name'] == file for entry in content_list):
                print(f"{file} exists in the directory.")
            else:
                print(f"{file} does not exist in the directory.")
    #Second test for a negative case
    elif response.status_code == 404: 
        print(f"The directory '{path_to_directory}' does not exist in the repository")
    else:
        print(f"Failed to fetch directory contents. Status code: {response.status_code}")

# Example usage
owner = 'dariyab93'
repo = 'chatbot'
path_to_directory = 'github'

check_files_exist(owner, repo, path_to_directory)


