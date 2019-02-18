from flask import Flask
from flask import render_template
from flask import request
import qrcode,time

app = Flask(__name__)

def code(form):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,#容错范围25 H30
        box_size=10,#每个点像素的大小
        border=4,#框
    )#创建qrcode对象
    qr.add_data(
        '''BEGIN:VCARD\n
        version:3.0\n
        FN:{}\n
        ORG:{}\n
        TITLE:{}\n
        ADR;WORK:{}\n
        TEL;WORK:{}\n
        EMAIL;WORK:{}\n
        URL:{}\n
        NOTE:{}\n
        END:VCARD'''.format(form.get('name'),form.get('company'),form.get('title'),form.get('address'),form.get('mobile'),form.get('email'),form.get('url'),form.get('desc'))

    )
    img = qr.make_image()
    path = 'static/CardImg/{}.png' % time.time()
    img.save(path)
#pil模块
@app.route('/',methods = ['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    #request.args#获取get
    form = request.form
    path = code(form)
    return path

@app.route('/ryo')
def ryo():
    return '<h1>hello ryo</h1>'

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000,debug = True)
