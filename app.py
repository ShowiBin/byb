from datetime import timedelta

from flask import Flask, render_template, request

import server

import model.USER_DBOP as user_OP
import model.BLOS_DBOP as blogs_OP
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/home')
def p_home():
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

@app.route('/submit_blogs',methods=['post','get'])
def submit_blogs():
    title = eval(request.args.get('title'))
    con = eval(request.args.get('con'))

    return blogs_OP.insert_blogs(title,con)

@app.route('/sorry',methods=['post','get'])
def sorry():
    return '''
        <h1>对不起，我还没实现，好累，唉</h1>
    '''
@app.route('/about',methods=['post','get'])
def about():
    return '''
        <h1>本网站由Showi小冰建设...技术也不高，做着玩玩，。。想要源码直接拿，不想要就..好。</h1><br>
        <h1>但是请遵守互联网协议,</h1><br>
        <h1>还有，，不要把我的小服务器搞过载了</h1><br>
        <h1>blogsd登录和可使用,但有bug，可以登录注册,不想修了，一个人做太难了，</h1><br>
        <h1>有许多数据是从网上爬到的，如果侵权了，联系我删除，/😁/</h1><br>
        <h1 style="position:absolute;buttom:10px;">copyright@机客公会@Showi小冰</h1>
    '''

if __name__ == '__main__':
    app.run()
