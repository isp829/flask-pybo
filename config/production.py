from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'j\xfdA\x07=\xfb\x06\xc1\xf7\x87@\xb1\xed\x99\xc6\x8b'