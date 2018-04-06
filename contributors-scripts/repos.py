import requests
#repos = requests.get('https://api.github.com/orgs/edgexfoundry/repos',auth=('jpwhitemn','9e396978ef8f2cbbb6613cf1676351742bf672ae'))

repos = requests.get('https://api.github.com/orgs/edgexfoundry/repos?per_page=100',auth=('jpwhitemn','9e396978ef8f2cbbb6613cf1676351742bf672ae'))

j=0
for repo in repos.json():
	print(repo['name'])
	j=j+1
print(j)
