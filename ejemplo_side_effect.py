import requests


def main():
    try:
        response = requests.get('http://localhost/fake-url/')
        print(response.json())
    except RuntimeError:
        print('This was a mistake')
        raise


if __name__ == '__main__':
    main()
