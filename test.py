import requests

BASE_URL =  "http://127.0.0.1:5000/api/"

get_r = requests.get(BASE_URL + "2")

print(get_r.status_code)
res = get_r.json()
print(f"hello {res['name']}")
# print(get_r.headers)

# post_r = requests.post(BASE_URL, {'name':'narendra', 'pin':123, 'country':
# 	'India'})
# print(post_r.status_code)
# print(post_r.text)

# put_r = requests.put(BASE_URL+ '20', {'name':'mukesh', 'pin':123, 'country':
# 	'India'})
# print(put_r.status_code)
# print(put_r.text)
# delete_r = requests.delete(BASE_URL+ '1')
# print(delete_r.status_code)
# print(delete_r.text)

