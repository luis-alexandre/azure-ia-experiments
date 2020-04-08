import requests
import sys


def main():
    subscription_key = sys.argv[1]  # your subscription key. ex: 1230sd80912312
    assert subscription_key

    text_analytics_base_url = "https://text-analytics-faas.cognitiveservices.azure.com"
    sentiment_api_url = text_analytics_base_url + "/text/analytics/v2.1/sentiment"

    documents = {
        'documents': [
            {'id': '1',
             'text': 'Eu estou muito feliz por aprender coisa nova com a Microsoft.'}
        ]
    }

    # Get sentiment text
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    response = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()

    print(response.status_code)
    print(sentiments)
    print()

    # Detect language
    language_api_url = text_analytics_base_url + "/text/analytics/v2.1/languages"
    response = requests.post(language_api_url, headers=headers, json=documents)
    languages = response.json()

    print(response.status_code)
    print(languages['documents'][0]['detectedLanguages'][0]['name'])
    print()

    # Get key phrases from text
    key_phrase_url_api = text_analytics_base_url + "/text/analytics/v2.1/keyPhrases"
    response = requests.post(key_phrase_url_api, headers=headers, json=documents)
    key_phrases = response.json()

    print(response.status_code)
    print(key_phrases)
    print()


if __name__ == "__main__":
    main()