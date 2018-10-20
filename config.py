import redis
import flask_session


class BaseConfig:

    SECRET_KEY = "secret_key"

    DEBUG = True

    #
    LOGGING_DEBUG = "ERROR"

    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/tour"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = "127.0.0.1"

    REDIS_PORT = 6379

    SESSION_TYPE = "redis"

    SESSION_USE_SIGNER = True

    SESSION_REDIS = redis.StrictRedis(REDIS_HOST, REDIS_PORT)

    SESSION_PERMANENT = 24 * 60 * 60


class DevConfig(BaseConfig):
    pass


configs = {
    "dev": DevConfig,
}
