from mongoengine import connect
#alias_core = 'core'
#db = 'snakes'

#data = dict(
#    username = 'chandramgc',
#    password = 'tJRT9XLLNabvHS5J',
#    host = 'girish-cluster.rwcoi.mongodb.net',
#    port = 27016
#)

def global_init():
    #connect.register_connection(alias=alias_core, name=db,**data)
    connect(
        alias='core',
        db='snakes',
        username='chandramgc',
        password='tJRT9XLLNabvHS5J',
        host='girish-cluster.rwcoi.mongodb.net'
    )