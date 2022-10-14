from bs4 import BeautifulSoup
import requests
import time

print('Enter the skill you are unfamiliar with')
unfamiliar_skill = input('>')
print('filtering out unfamiliar skills')
print('')


def find_jobs():
    html_texts = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_texts, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        time_posted = job.find('span', class_='sim-posted').text
        if 'few' in time_posted:

            company_name = job.find(
                'h3', class_='joblist-comp-name').text

            skills = job.find('span', class_='srp-skills').text
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"Time Posted: {time_posted.strip()}")
                print(f"Job Link: {more_info}")

                print('')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 2
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait * 60)

print('')
