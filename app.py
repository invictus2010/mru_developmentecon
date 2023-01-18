from googleapiclient.discovery import build
import re
import csv
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Set up the YouTube Data API client
api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

alphabets = "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"
digits = "([0-9])"
def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    text = re.sub(digits + "[.]" + digits, "\\1<prd>\\2", text)
    if "..." in text:
        text = text.replace("...", "<prd><prd><prd>")
    if "Ph.D" in text:
        text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms+" "+starters, "\\1<stop> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" +
                  alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(alphabets + "[.]" + alphabets +
                  "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" "+suffixes+"[.] "+starters, " \\1<stop> \\2", text)
    text = re.sub(" "+suffixes+"[.]", " \\1<prd>", text)
    text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

# Make a request to the YouTube Data API's playlistItems.list method
playlist_id = 'PL-uRhZ_p-BM4pQXFm4hCmMR7LhTXje61m'
pageTokens = ['','EAAaBlBUOkNESQ', 'EAAaBlBUOkNHUQ', 'EAAaB1BUOkNKWUI','EAAaB1BUOkNNZ0I','EAAaB1BUOkNQb0I']
for i in pageTokens:
    request = youtube.playlistItems().list(
        part='snippet',
        pageToken= '',
        playlistId=playlist_id,
        maxResults=50)

    response = request.execute()

    videos = []
    for item in response['items']:
        video_id = item['snippet']['resourceId']['videoId']
        title = item['snippet']['title']
        videos.append({'video_id': video_id, 'title': title})
    print(videos)
    for video in videos:
        try:
            video_id = video['video_id']
            title = video['title']
            result = {'text': ''}
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            for obj in transcript:
                text = obj['text']
                result['text'] += text + ' '
            sentences = split_into_sentences(result['text'])
            for i in range(0, len(sentences), 1):
                block = sentences[i:i+1]
                s = ' '.join([str(elem) for elem in block])
                data = [title, s, f'https://www.youtube.com/watch?v={video_id}']
                with open('transcripts_1sentences.csv', 'a', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                    f.close()
        except Exception as e:
            f = open('error.txt', 'a')
            f.write(video['video_id'])
            f.close()

            # Log exception to error_log txt file
            with open('error_log.txt', 'a') as f:
                f.write(video['video_id'] + ' ' + str(e))
                f.write('\n')
                f.close()
            continue
    print(response['nextPageToken'])
        