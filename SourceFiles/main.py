from instagram.client import InstagramAPI


def auth(access_token, client_secret):
    api = InstagramAPI(access_token=access_token, client_secret=client_secret)
    print('Succesfully Authenticated your app!')

def main():
    auth('2613384557.4b4891d.0e84980f87b74955bd65b27d3fc21c62', '6425a96b56e64e2aa4e96cca976b2fea')





if __name__ == '__main__':
    main()
