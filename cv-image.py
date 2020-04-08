import requests
import sys


def main():
    subscription_key = sys.argv[1]  # your subscription key. ex: 1230sd80912312
    assert subscription_key

    vision_base_url = "https://computerfaas.cognitiveservices.azure.com/"
    vision_analyze_url = vision_base_url + "/vision/v2.0/analyze"

    image_url = "https://i0.statig.com.br/bancodeimagens/0a/ve/mm/0avemmbd8e03snftfdrdjnoe8.jpg"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key }
    params = {'visualFeatures': 'Categories,Description,Color'}
    data = {'url': image_url}

    response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
    response.raise_for_status()

    analysis = response.json()
    print(analysis)
    print()

    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    print(image_caption)


if __name__ == "__main__":
    main()