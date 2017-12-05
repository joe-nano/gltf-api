# Run test API
import requests

PORT = '5018'

# Upload an unsupported file
print("Upload unsupported file")
url = 'http://127.0.0.1:'+PORT+'/v1/models'  # API endpoint
filename = 'test.png'
file = open(filename, 'rb')  # File to upload
try:
    r = requests.post(url=url, data={'uploaded_file': filename}, files={'file': file})
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Upload a supported file
print("Upload supported file")
url = 'http://127.0.0.1:'+PORT+'/v1/models'  # API endpoint
filename = 'test.FBX'
file = open(filename, 'rb')  # File to upload
try:
    r = requests.post(url=url, data={'uploaded_file': filename}, files={'file': file})
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Upload a supported file by sending the url
print("Post source_path to supported file")
url = 'http://127.0.0.1:'+PORT+'/v1/models'  # API endpoint
source_path = 'https://purplepill.io/wp-includes/3d/test.FBX'
try:
    r = requests.post(url=url, data={'source_path': source_path})
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Upload a supported file by sending the url + arguments for converter
print("Post source_path to supported file + arguments")
url = 'http://127.0.0.1:'+PORT+'/v1/models'  # API endpoint
source_path = 'https://purplepill.io/wp-includes/3d/test.FBX'
try:
    r = requests.post(url=url, data={'source_path': source_path, 'compress': True, 'binary': True})
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Upload a file that is too large
print("Upload a file that is too large")
url = 'http://127.0.0.1:'+PORT+'/v1/models'  # API endpoint
source_path = 'https://purplepill.io/wp-includes/3d/large.zip'
try:
    r = requests.post(url=url, data={'source_path': source_path})
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)


# Retrieve list of uploaded files
print("Retrieve list of models")
url = 'http://127.0.0.1:'+PORT+'/v1/models'  # API endpoint
# r = requests.get('https://api.github.com/user', auth=('user', 'pass')), because we need authentication for this one
try:
    r = requests.get(url=url)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print(r.status_code)
print(r.text)