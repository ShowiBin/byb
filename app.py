from datetime import timedelta
import datetime
from flask import Flask, render_template, request

import server

import model.USER_DBOP as user_OP
import model.BLOS_DBOP as blogs_OP
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

timer = 0
@app.route('/')
def hello_world():
    global timer
    with open('log.txt', 'a') as f:
        f.write(datetime.datetime.now())
    timer+=1
    return render_template('index.html')


@app.route('/home')
def p_home():
    global timer
    with open('log.txt', 'a') as f:
        f.write(str(timer)+'\n')
        f.write(str(datetime.datetime.now()))
        f.write('\n')
    timer += 1

    return render_template('home.html')


@app.route('/login', methods=['post', 'get'])
def p_login():
    return render_template('login.html')


@app.route('/signup')
def p_signup():
    return render_template('signup.html')


@app.route('/server', methods=['post', 'get'])
def s_data():
    data_name = eval(request.args.get('dataName'))
    data = server.DataGet()
    res = data.getData(data_name)
    print('res', res)
    return str(res)

@app.route('/serverLogin',methods=['post','get'])
def s_login():
    username = eval(request.args.get('username'))
    pwd = eval(request.args.get('pwd'))
    return user_OP.login(username,pwd)

@app.route('/serverSignUp',methods=['post','get'])
def s_signup():
    username = eval(request.args.get('username'))
    pwd = eval(request.args.get('pwd'))
    name = eval(request.args.get('name'))
    age = eval(request.args.get('age'))
    return user_OP.signup(username,pwd,name,age)

@app.route('/blogs',methods=['post','get'])
def blogs():

    return render_template('blogs.html')

@app.route('/events',methods=['post','get'])
def events():

    return render_template('events.html')

@app.route('/submit_blogs',methods=['post','get'])
def submit_blogs():
    title = eval(request.args.get('title'))
    con = eval(request.args.get('con'))

    return blogs_OP.insert_blogs(title,con)
@app.route('/submit_events',methods=['post','get'])
def submit_events():
    title = eval(request.args.get('title'))
    con = eval(request.args.get('con'))

    return blogs_OP.insert_events(title,con)

@app.route('/sorry',methods=['post','get'])
def sorry():
    return '''
        <h1>对不起，此功能还没实现呢</h1>
    '''
@app.route('/about',methods=['post','get'])
def about():
    return '''
        <h1>本网站由Showi小冰建设...技术也不高，做着玩玩，。。想要源码直接拿，不想要就..好。</h1><br>
        <h1>但是请遵守互联网协议,</h1><br>
        <h1>还有，，不要把我的小服务器搞过载了</h1><br>
        <h1>如果侵权了，联系我删除，/😁/</h1><br>
        <h1>时间:2020/2/29,  重庆交通大学大学生艺术团表演部网站:version 1.0</h1><br>
        <h1 style="position:absolute;buttom:10px;">copyright 重庆交通大学大学生艺术团表演部@Showi小冰</h1>
    '''

@app.route('/learn_more',methods=['post','get'])
def learn_more():

    return '''
    <style>
        background-color:gray;
    </style>
    <h1>LEARN MORE</h1>
        <a href='http://www.cqjtu.edu.cn/' style="text-decoration:none;color:gold;">重庆交通大学</a><br>
        <a href='/sorry' style="text-decoration:none;color:gold;">重庆交通大学校团委</a><br>
        <a href='/sorry' style="text-decoration:none;color:gold;">重庆交通大学大学生艺术团</a><br>
        <a href='/sorry' style="text-decoration:none;color:gold;">重庆交通大学大学生学生会</a><br>
        <a href='/sorry' style="text-decoration:none;color:gold;">重庆交通大学大学生校社联</a><br>
    '''

@app.route('/showus',methods=['post','get'])
def showus():
    '''
    show showus html page
    :return:
    '''
    return render_template('showus.html')

@app.route('/DM',methods=['post','get'])
def DM():
    '''
    show showus html page
    :return:
    '''
    return render_template('DM.html')

@app.route('/products',methods=['post','get'])
def products():
    '''
    show showus html page
    :return:
    '''
    return render_template('products.html')

@app.route('/welcome',methods=['post','get'])
def welcome():
    '''
    show welcome html page
    :return:
    '''
    return render_template('welcome.html')

@app.route('/showi',methods=['post','get'])
def showi():
    '''
    show showi html page
    :return:
    '''
    return '<h1>Showi 的个人主页还在完善</h1>'

if __name__ == '__main__':
    app.run()
