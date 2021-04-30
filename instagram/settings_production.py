import dj_database_url
from decouple import config


DATABASES = {
    'default': dj_database_url.config(
        default=config('postgres://lckpwgeahycdul:41df89bc3184750963b3ab53acf5f403358657c96ef63e8e1b51bce1fad7085a@ec2-52-21-252-142.compute-1.amazonaws.com:5432/dqtej0v8j4ole')
    )
}
