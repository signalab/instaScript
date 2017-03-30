import requests

access_token = '2613384557.e029fea.3eeef32d7a0d4502b0bf3b87655d1927'
client_secret = '6425a96b56e64e2aa4e96cca976b2fea'
location_id = '213351762' #Location ID ITESO

#Precise Lat and long for ITESO:
#20.607558877936, -103.4148257093

#Obtained from google maps:
latitude = '20.606686'
longitude = '-103.415787'


def auth(access_token, client_secret):
    api = InstagramAPI(access_token=access_token, client_secret=client_secret)
    print('Succesfully authenticated!\n' + str(api.user('2613384557')) + '\n')
    return api

def main():
    #InstagramAPI(access_token=access_token, client_secret=client_secret)
    api = auth(access_token, client_secret)

    #Test Querys on Location Endpoint

    #Get information about a location
    data = requests.get('https://api.instagram.com/v1/locations/{}?access_token={}'.format(location_id, access_token))
    jsonData = data.json()

    print('--------------------------------------------------------------------------------------------------')
    print('Data obtained for location_id = \"{}\":\n{}'.format(location_id,str(jsonData)))
    print('--------------------------------------------------------------------------------------------------')

    #Search for a location by geographic coordinate
    data = requests.get('https://api.instagram.com/v1/locations/search?lat={}&lng={}&access_token={}'.format(latitude, longitude, access_token))
    jsonData = data.json()

    print('--------------------------------------------------------------------------------------------------')
    print('Data obtained for lat = \"{}\", lng = \"{}\"\n{}'.format(latitude, longitude, str(jsonData)))
    print('--------------------------------------------------------------------------------------------------')

    #Get a list of recent media objects from a given location.
    data = requests.get('https://api.instagram.com/v1/locations/{}/media/recent?access_token={}'.format(location_id, access_token))
    jsonData = data.json()

    print('--------------------------------------------------------------------------------------------------')
    print('Recent media objects on location_id = \"{}\":\n{}'.format(location_id,str(jsonData)))
    print('--------------------------------------------------------------------------------------------------')








if __name__ == '__main__':
    main()
