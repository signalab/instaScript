from instagram.client import InstagramAPI
import requests

access_token = '2613384557.4b4891d.0e84980f87b74955bd65b27d3fc21c62'
client_secret = '6425a96b56e64e2aa4e96cca976b2fea'


def auth(access_token, client_secret):
    api = InstagramAPI(access_token=access_token, client_secret=client_secret)
    print('Succesfully authenticated!\n' + str(api.user('2613384557')) + '\n')
    return api

def main():
    #InstagramAPI(access_token=access_token, client_secret=client_secret)
    api = auth(access_token, client_secret)

    #api.media_search(q, count, lat, lng, min_timestamp, max_timestamp)
    #print(api.location('2593354')) #Uses the Eiffel Tower Location ID

    data = requests.get('https://api.instagram.com/v1/locations/{}?access_token={}'.format('2593354', access_token))
    # API response:
    # {
    #     u'meta':
    #     {
    #         u'code': 200
    #     },
    #     u'data':
    #     {
    #         u'latitude': 48.858212502088, u'id': u'2593354', u'longitude': 2.2945895631526, u'name': u'Tour Eiffel'
    #     }
    # }

    print('Data obtained:')
    print(data.json())






if __name__ == '__main__':
    main()
