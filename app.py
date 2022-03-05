from flask import Flask, jsonify, request
import os, yaml, requests, time

app = Flask(__name__)
                  
with open(os.path.join(os.path.dirname(__file__), 'config.yaml'), 'r') as ymlfile:
    try:
        config = yaml.safe_load(ymlfile)
    except yaml.YAMLError as exc:
        raise Exception("Error parsing config file: {}".format(exc))

VERBOSE = config['VERBOSE']
PROJECT_PATH = config['PROJECT_PATH']
ROOT_PATH = os.getcwd()

def ExecuteBashScript(script, branch):
    os.system("chmod u+x " + ROOT_PATH + '/scripts/'+script)
    ## Pass ROOT_PATH and PROJECT_PATH to the script
    os.system('cd ' + PROJECT_PATH + ' && ' + ROOT_PATH + '/scripts/'+script + ' "' + ROOT_PATH + '" "' + PROJECT_PATH + '"' + ' "' + branch + '"')

def SlackAlert(msg):
    """
    SlackAlert(msg)
    Send a message to a Slack channel.
    """
    if VERBOSE == "enabled":
      msg = msg + " [" + time.strftime("%Y-%m-%d %H:%M:%S") + "]"
      requests.post(config['SLACK_WEBHOOK'], data={"text": msg})

@app.route("/webhook", methods=['POST'])
def webhook():
    payload = request.get_json()
    branch = payload['ref'].split('/')[-1]
    ## parse github webhook payload response and get event type and branch name
    SlackAlert("👀 A new commit has been detected to the {} branch, working on updating source code.".format(branch))
    os.system('cd ' + PROJECT_PATH + ' && git pull origin ' + branch)
    SlackAlert("🎉 The {} branch has been updated successfully.".format(branch))
    SlackAlert("🛠 Executing the build script.")
    ExecuteBashScript('build.sh', branch)
    SlackAlert("🎉 The build script has been executed successfully.")
    SlackAlert("🛠 Executing the deploy script.")
    ExecuteBashScript('deploy.sh', branch)
    SlackAlert("🎉 The deploy script has been executed successfully.")
    return jsonify(payload)
    

if __name__ == "__main__":
  app.run(host='0.0.0.0')