import requests
import json
import os
import django

"""# Django環境を読み込む（必要に応じて設定）
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()"""
API_KEY = os.environ.get('ONE_SIGNAL_API_KEY')

def send_notification():
    url = "https://onesignal.com/api/v1/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": API_KEY,
    }

    payload = {
        "app_id": "91af5053-eb7e-4a58-b2e5-dc1328868ba5",
        "included_segments": ["Subscribed Users"],
        "headings": {"en": "Reminder",
                     "ja": "今日のはみがきはもうお済みですか？"},
        "contents": {"en": "Have you done your tasks today? Check them out!",
                     "ja": "今日の分の色塗りをしましょう。"},
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # ステータスコードが4xx/5xxの場合に例外を発生
        print("Notification sent successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print("Failed to send notification:", e)

if __name__ == "__main__":
    send_notification()
