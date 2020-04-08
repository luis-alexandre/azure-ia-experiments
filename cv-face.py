import requests
import sys


def main():
    subscription_key = sys.argv[1]  # your subscription key. ex: 1230sd80912312
    assert subscription_key

    face_base_url = "https://face-faas.cognitiveservices.azure.com"
    face_analyze_url = face_base_url + "/face/v1.0/detect"

    image_url = "https://www.oliberal.com/image/contentid/policy:1.64688:1549677714/Carmen-Miranda.JPG?f=2x1&$p$f=086acb8&w=750&$w=a1569b8"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    data = {'url': image_url}

    response = requests.post(face_analyze_url, headers=headers, json=data)
    print(response.status_code)
    print(response.text)

    analysis = response.json()
    print(analysis)
    print()


if __name__ == "__main__":
    main()
