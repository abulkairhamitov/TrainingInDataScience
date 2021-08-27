from matplotlib import pyplot as plt
import requests, json
from collections import Counter
from dateutil.parser import parse

github_user = "abulkairhamitov"
endpoint = f"https://api.github.com/users/{github_user}/repos"

repos = json.loads(requests.get(endpoint).text)

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)
plt.plot(month_counts.keys(), month_counts.values(), "bx")
plt.ylabel("В какие месяцы")
plt.show()
plt.ylabel("В какие дни недели")
plt.plot(weekday_counts.keys(), weekday_counts.values(), "ro")
plt.show()

last_5_repositories = sorted(repos, # последние 5 хранилищ
                            key=lambda r: r["created_at"], 
                            reverse=True) [:5] 
last_5_languages = [repo["language"] # последние 5 языков 
                    for repo in last_5_repositories] 
