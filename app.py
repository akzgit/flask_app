from flask import Flask,request,redirect, url_for #flask -is the package, Flask -is the module,this lines allows up to access the flask server

app=Flask(__name__) #app is an object, __name__ variable/argument,constructor-flask

@app.route("/") #route will call the python function,/->index or default page,it will heip you route map what ever you are typing in the browser(the  url) to a python function
def display(): #view function
    return "First Flask application"

@app.route("/nsti")
def show():
    return "new page named NSTI "


@app.route("/nsti/<value>") #what ever we type in the url will be displayed in the web page
def show1(value):
    return "new page named %s "%value


@app.route('/python/<name>/<place>')
def showtime(name,place):
    return 'Hooray!! %s executed the code successfully %s'%(name,place)


@app.route("/login",methods=['POST','GET'])
def loginform():
    if request.method=='POST':
        username=request.form['uname']
        userplace=request.form['uplace']
        return redirect(url_for('showtime',name=username, place=userplace))
    else:
        username=request.args.get['uname']
        userplace=request.args.get['uplace']
        return redirect(url_for('showtime',name=username,place=username))

if __name__ =='__main__':
   app.run()
   
   