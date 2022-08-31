import requests

headers = {
"x-csrftoken": "a",
"x-requested-with": "XMLHttpRequest",
"Cookie": "scratchcsrftoken=a;scratchlanguage=en;",
"referer": "https://scratch.mit.edu",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
}


def get_unread_msg_cnt(user):
    headers["referer"] = "https://scratch.mit.edu"
    return requests.get("https://api.scratch.mit.edu/users/" + str(user) + "/messages/count", headers=headers).json()['count']


print(get_unread_msg_cnt(input("username: ")))
