class S(object):
    def __init__(self):
        print('ctor')

    def __new__(cls):
        print('new')
        if not hasattr(cls, 'instance'):
            print('creating new')
            cls.instance = super(S, cls).__new__(cls)
        print('returning cucc')
        return cls.instance