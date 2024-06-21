from werkzeug.utils import secure_filename as _secure_filename

def secure_filename(*args, **kwargs):
    return _secure_filename(*args, **kwargs)