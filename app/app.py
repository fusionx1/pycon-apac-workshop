from flask import Flask
import os
import socket
import redis

app = Flask(__name__)

@app.route("/")
def hello():
    connection = "Redis is not connecting"
    try:
        # Connecto to Redis
        conn = redis.StrictRedis(
            host='35.227.164.30',
            port=6379,
            password='daloh31r8hisn2')
        print conn
        conn.ping()
        connection = 'Redis is connected'
        print 'Set Record:', conn.set("best_car_ever", "Tesla Model S")
        print 'Get Record:', conn.get("best_car_ever")
        #print 'Delete Record:', conn.delete("best_car_ever")
        #print 'Get Deleted Record:', conn.get("best_car_ever")
    except Exception as ex:
        print 'Error:', ex
        exit('Failed to connect, terminating.')

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname: <b/> {hostname}<br/>" \
           "<b>Status: <b/> {connection}<br/>"
    return html.format(name=os.getenv("Name", "world"), hostname=socket.gethostname(), connection=connection)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)



































