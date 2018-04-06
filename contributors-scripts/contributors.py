import requests
repos = requests.get('https://api.github.com/orgs/edgexfoundry/repos?per_page=100',auth=('jpwhitemn','<token>'))

for repo in repos.json():
	if not (repo['name'].startswith('docker')):
		print('---------------')
		print(repo['name'])
		contrib_data = requests.get('https://api.github.com/repos/edgexfoundry/' + str(repo['name']) + '/stats/contributors?per_page=100', auth=('jpwhitemn','<token>'))
		for contrib in contrib_data.json():
			print(contrib['author']['login'])

