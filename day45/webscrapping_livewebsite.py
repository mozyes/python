from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

content = response.text

soup = BeautifulSoup(content, 'html.parser')

titleline_spans = soup.find_all('span', class_='titleline')
subline_spans = soup.find_all('span', class_='subline')

for titleline_span, subline_span in zip(titleline_spans, subline_spans):
    article_tag = titleline_span.find('a')
    if article_tag:
        article_text = article_tag.getText()
        article_link = article_tag.get('href')

        upvote_score_tag = subline_span.find('span', class_='score')
        if upvote_score_tag:
            upvote_score_text = upvote_score_tag.getText()

            print("Article Title:", article_text)
            print("Article Link:", article_link)
            print("Upvote Score:", upvote_score_text)
            print("-" * 50)  # Separator
