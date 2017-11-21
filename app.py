import bottle
from sys import argv

#test comment

@bottle.route('/')
def helloWorld():
    return 'Daníel er kominn á Heroku.'


if __name__ == "__main__":
    bottle.run(host='0.0.0.0', port=argv[1])
