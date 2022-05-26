from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

id = input('Вставте id видео:')
transcript = YouTubeTranscriptApi.get_transcript(id, languages=['ru'])
formatter = TextFormatter()


json_formatted = formatter.format_transcript(transcript)
json_formatted = json_formatted.replace("\r"," ")
json_formatted = json_formatted.replace("\n"," ")
with open("input.txt", "w") as file:
            file.write(json_formatted)
