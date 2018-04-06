import requests
repos = requests.get('https://api.github.com/orgs/edgexfoundry/repos?per_page=100',auth=('jpwhitemn','<token>'))

for repo in repos.json():
	if not (repo['name'].startswith('docker')):
		print('---------------')
		print(repo['name'])
		commits = requests.get('https://api.github.com/repos/edgexfoundry/' + str(repo['name']) + '/stats/participation?per_page=1000',auth=('jpwhitemn','<token>'))
		weeks=commits.json()['all']
		for i in weeks:
			print(i)

