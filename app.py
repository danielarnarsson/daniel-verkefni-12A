import bottle

@bottle.route('/')
def helloWorld():
    return 'Daníel er kominn á Heroku.'

bottle.run(host='0.0.0.0', port=argv[1])