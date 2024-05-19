import requests
from bs4 import BeautifulSoup

BLOG_URL = "https://rangyi.tistory.com"

response = requests.get(BLOG_URL)
soup = BeautifulSoup(response.text, 'html.parser')

# 티스토리 최신 글 추출 (티스토리 블로그 HTML 구조에 맞게 수정 필요)
latest_posts = soup.select('div.post-item a')  # 이 부분은 블로그 HTML 구조에 맞게 조정 필요

with open('latest_posts.md', 'w', encoding='utf-8') as file:
    file.write("## Latest Tistory Posts\n")
    for post in latest_posts[:5]:  # 최신글 5개 가져오기
        title = post.get_text(strip=True)
        link = post['href']
        if not link.startswith('http'):
            link = f"{BLOG_URL}{link}"
        file.write(f"* [{title}]({link})\n")
