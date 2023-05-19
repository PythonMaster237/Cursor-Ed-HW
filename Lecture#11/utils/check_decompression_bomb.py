import io

from PIL import Image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def check_for_decompression_bomb(file):
    max_size = 10*(1024**2) # 10 MB
    if len(file) > max_size:
        return True
    try:
        Image.open(io.BytesIO(file)).verify()
    except (ValueError, IOError):
        return True
    return False


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS