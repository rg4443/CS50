import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r".+(https?://(?:www\.)?youtube\.com/embed/\w+).+$", s)
    if matches:
        youtube_url = matches.group(1)
        youtube_url = youtube_url.replace("http://", "https://")
        youtube_url = youtube_url.replace("youtube.com", "youtu.be")
        youtube_url = youtube_url.replace("embed/", "")
        youtube_url = youtube_url.replace("www.", "")

        return youtube_url
    else:
        return None

if __name__ == "__main__":
    main()
