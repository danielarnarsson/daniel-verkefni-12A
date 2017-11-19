import bottle, os

@bottle.route('/')
def helloWorld():
    return 'Daníel er kominn á Heroku.'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    bottle.run(host='0.0.0.0', port=port)