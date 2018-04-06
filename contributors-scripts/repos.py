import requests
#repos = requests.get('https://api.github.com/orgs/edgexfoundry/repos',auth=('jpwhitemn','<token>'))

repos = requests.get('https://api.github.com/orgs/edgexfoundry/repos?per_page=100',auth=('jpwhitemn','<token>'))

j=0
for repo in repos.json():
	print(repo['name'])
	j=j+1
print(j)
