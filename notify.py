import os

import requests
from dotenv import load_dotenv


def main():
    load_dotenv(override=True)
    access_token = os.getenv("ACCESS_TOKEN")

    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"message": "message"}
    files = {"imageFile": open("./images/sample.jpg", "rb")}

    requests.post(url=url, headers=headers, data=data, files=files)


if __name__ == "__main__":
    main()
