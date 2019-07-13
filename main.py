from flask import Flask
from flask import request
app = Flask(__name__)
import subprocess
 
@app.route("/ping")
def ping():
    cmd = request.args.get("ip")
    if cmd is None:
        return "Invalid input.."

    try:
        output = subprocess.check_output("echo "+cmd, shell=True)
    except:
        return "Error!"

    return output
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
