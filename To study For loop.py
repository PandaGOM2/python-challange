from requests import get

websites = ("https://daum.net",
            "https://httpstat.us/502",
            "https://httpstat.us/404",
            "https://httpstat.us/301",
            "https://httpstat.us/200",
            "https://httpstat.us/101")

results = {}

for website in websites:
    if not website.startswith("https://"):
     website = f"https://{website}"
    response = get(website)
    if response.status_code >= 100 and response.status_code < 200:
      results[website] = "Information"
    elif response.status_code >=200 and response.status_code < 300:
      results[website] = "Ok"
    elif response.status_code >=300 and response.status_code < 400:
      results[website] = "Redirection"
    elif response.status_code >=400 and response.status_code < 500:
      results[website] = "Client Error"
    elif response.status_code >=500 and response.status_code < 600:
      results[website] = "Error"

print(results)
