import requests
import datetime


def get_trending_repositories(top_size):
    params = {'q': 'created:>='+
                   '{:%Y-%m-%d}'.format(datetime.date.today() - datetime.timedelta(days=7)),
              'sort': 'stars',
              'order': 'desc'
              }
    res = requests.get(url='https://api.github.com/search/repositories', params=params)

    repos = res.json()['items']

    return repos[:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    pass


if __name__ == '__main__':

    top_repos = get_trending_repositories(20)

    for repository in top_repos:
        print(repository['html_url'], repository['open_issues'])
