#coding=utf-8
from flask import Blueprint, render_template, request, jsonify, session
ytx_blueprint = Blueprint('ytx_blueprint', __name__)


@ytx_blueprint.route('/')
def index():
    return render_template('ytx/index.html')

from ytx_sdk import ytx_send
import random


@ytx_blueprint.route('/sendSMS',methods=['POST'])
def sendSMS():
    sjh=request.form.get('sjh')
    yzm=random.randint(1000,9999)
    result=ytx_send.sendTemplateSMS(sjh,[yzm,'5'],1)
    session['yzm']=yzm
    if result=='000000':
        return jsonify({'ok':1})
    else:
        return jsonify({'ok':2})


@ytx_blueprint.route('/yz',methods=['POST'])
def yz():
    yzm1=session.get('yzm')
    yzm2=int(request.form.get('yzm'))
    if yzm1==yzm2:
        return 'ok'
    else:
        return 'no'