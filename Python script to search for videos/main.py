from googleapiclient.discovery import build

# Initialize the YouTube Data API
API_KEY = "YOUR_YOUTUBE_API_KEY"
youtube = build("youtube", "v3", developerKey=API_KEY)

# Search for Python tutorials in the Education category
request = youtube.search().list(
    part="snippet",
    q="Python tutorial",
    type="video",
    videoCategoryId="27"  # Education category ID
)

response = request.execute()

# Print out the titles and video IDs of the results
for item in response.get("items", []):
    print(f"Title: {item['snippet']['title']}")
    print(f"Video ID: {item['id']['videoId']}\n")
