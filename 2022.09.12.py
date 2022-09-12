# 다운로드한 library 불러오기
from requests import get  #http를 불러오기 위한 lib
from bs4 import BeautifulSoup  #parsing을 위한 lib
# 요청 사이트의 url
main_url = "https://weworkremotely.com/remote-jobs/search?term="

search_term = "python"  #검색한 내용 ""안의 내용에 따라 달라짐

#응답받기
response = get(f"{main_url}{search_term}")

# 응답이 성공적인가에 대한 분기문
if not response.status_code == 200:
    print("Can't request the website!")
else:
    #Save the result and renew
    results = []
    #Parcing the result of html code and receiving it
    soup = BeautifulSoup(response.text, "html.parser")
    # bring the All data in section > jobs
    jobs = soup.find_all('section', class_="jobs")
    # bring the All data in jobs > li
    for jobs_section in jobs:
        job_post = jobs_section.find_all("li")
        job_post.pop(-1)  # remove the viewer-list
        #bring the All data in job_post > a
        for post in job_post:
            anchors = post.find_all("a")
            anchor = anchors[1]  #remove the first company
            link = anchor['href']  #태그의 요소를 가져올 수 있다.
            #duplication the 'company' so made the position argument
            company, position, region = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_="title")
            #HTML tag --> string
            job_data = {
                'company': company.string,
                'region': region.string,
                'position': title.string
            }
            #job을 추출할 때마다 result에 저장
            results.append(job_data)
    for result in results:
        print(result)
        print("///////")
