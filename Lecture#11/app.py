import os
import uuid

import catday
import utils
from flask import Flask, Response, abort, send_file, render_template, request
import PIL.Image
import io
import logging
import random

from time import perf_counter

from utils import input_text_lines, check_for_decompression_bomb, allowed_file

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base_page.html.jinja')



# Note:
#   If a rule ends with a slash and is requested without a slash by the user,
#   the user is automatically redirected to the same page with a trailing 
#   slash attached.
#   If a rule does not end with a trailing slash and the user requests
#   the page with a trailing slash, a 404 not found is raised.
# So we try to always define rules with trailing slashes '/'

@app.route('/cats/')
def list_cats():
    msg = 'There are {num} cats in our collection'
    return msg.format(num=len(catday.CATS))


def get_cat(numext, try_random=False):
    try:
        ret = catday.find_cat_file(numext=numext,
                                   try_random=try_random)
    except ValueError:      # integer unconvertable or wrong range
        abort(404, 'Wrong image number')
    else:
        app.logger.debug('Retrieve image "%s" for '
                        'base %s with ext "%s"',
                        *ret)
        return ret


@app.route('/cats/cat<int:num>.<string:ext>')
def cat_original(num, ext):
    t_start = perf_counter()    # measure request time

    file, base, ext = get_cat(f'{num}.{ext}', try_random=False)

    name = f'cat{base}{ext}'   # the filename passed to browser
    
    app.logger.debug('Original extension is %s', file.suffix)
    
    # if the extension is different, perform conversion with PIL
    if ext.lower() != file.suffix.lower():
        
        try:
            img = PIL.Image.open(file)
            # Save to buffer in memory and serve with Flask
            buf = utils.ImageIO(img, ext=ext)
        except utils.ImageIOError as err:
            abort(400, str(err))
        else:
            # now our file gets mocked by conversion result
            file = buf
    
    # if the file has the same extension,
    # don't convert at all and return directly

    took = perf_counter() - t_start

    if app.logger.isEnabledFor(logging.DEBUG):
        msg = f'Request took {took * 1000:.2f} ms'
        app.logger.debug(msg)

    return send_file(file, as_attachment=False, download_name=name)


@app.route('/cats/catoftheday<name>')
def cat_modified(name):
    file, base, ext = get_cat(name, try_random=True)

    date = utils.DateTriple()       # try UADateTriple() here
    date_suffix = date.tostr(fmt='{day}_{month:.3}').lower()

    text = date.tostr(fmt='{weekday:.3},\n{day}\n{month:.3}')

    try:
        img = PIL.Image.open(file)
        bgcolor = (255, 255, 255, int(255 * 0.4))
        cut = catday.cutter.text_cutout(img, text, bgcolor=bgcolor)
        if ext in ['.jpg', '.jpeg', '.jfif']:
            # eliminate alpha-channel as JPEG has no alpha
            cut = cut.convert('RGB')
        file = utils.ImageIO(cut, ext=ext)
    except utils.ImageIOError as err:
        abort(400, str(err))

    # passed to browser
    name = f'catoftheday{base}-{date_suffix}{ext}'
    return send_file(file, as_attachment=False, download_name=name)


@app.route('/cats/cat', methods=['GET', 'POST'])
def cat_chosen_modified(ext='png'):
    if request.method == 'POST':
        num = request.form['number']
        text = request.form['text']
        text = input_text_lines(text)

        file, base, ext = get_cat(f'{num}.{ext}', try_random=False)

        name = f'cat{base}{ext}'

        try:
            img = PIL.Image.open(file)
            bgcolor = (255, 255, 255, int(255 * 0.4))
            cut = catday.cutter.text_cutout(img, text, bgcolor=bgcolor)
            if ext in ['.jpg', '.jpeg', '.jfif']:
                # eliminate alpha-channel as JPEG has no alpha
                cut = cut.convert('RGB')
            file = utils.ImageIO(cut, ext=ext)
        except utils.ImageIOError as err:
            abort(400, str(err))

        return send_file(file, as_attachment=False, download_name=name)
    else:
        return render_template('choose_cats.html.jinja')


@app.route('/cats/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if check_for_decompression_bomb(request.files['file'].read()):
            abort(400, 'File has decompression bomb!')

        if not allowed_file(request.files['file'].filename):
            abort(400, 'Invalid file type.')

        file = request.files['file']
        img = PIL.Image.open(file)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        file_path = os.path.join(dir_path, 'uploaded', filename)
        img.save(file_path)
        return 'File uploaded successfully.'
    return render_template('upload_image.html')


if __name__ == '__main__':
    import logging
    app.logger.setLevel(logging.DEBUG)
    app.run(host='127.0.0.1', port=5000, debug=True)