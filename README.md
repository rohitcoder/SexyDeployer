
# SexyDeployer - A simple and sexy continous deployment tool

While working on one of project, i was in a situation where i was in need of updating dev/prod server very frequently and that was frutrsated, i started looking at Jenkins, but it was taking a lot of time and you need to look at lot of youtube videos to get it working. SexyDeployer works on concept of webhooks and that webhook triggers all internal scripts to get your work done!




## Installation
Deploy this tool on same server, where you are hosting your source code and enable used Port number in your firewall. This will allow github to send commit push alerts to SexyDeployer.

```bash
  $ git clone https://github.com/rohitcoder/SexyDeployer
  $ cd SexyDeployer
  $ source bin/activate
  $ python3 -m ensurepip --default-pip
  $ pip3 install -r requirements.txt
  $ flask run --host=0.0.0.0
```

After running above commands you'll get a URL in output something like this.

![Preview](https://i.imgur.com/8rA5RdN.png)

Copy this URL and visit, https://github.com/<Username>/<REPO_NAME>/settings/hooks/new

paste above URL, and in section "Which events would you like to trigger this webhook?
", select "Just the push event."

Now click on Add webhook.

Now configure, ``config.yaml`` file

```YAML
PROJECT_PATH: This is path of project, where you want to host your source code of application.

SLACK_WEBHOOK`: This is SLACK_WEBOOK url for logging purpose
```

#### Want to do something more Precisely?
Use `scripts/build.sh` and `scripts/deploy.sh` to add your custom exec commands
## Features

- Connect webhook with your github Repo
- Works with multiple branches simultaneously
- Supports ``build.sh`` and ``deploy.sh`` scripts which helps you running custom commands.
- Sends status reports in a slack workspace.


## FAQ

#### Is this the best tool available, should i used it?

You can look into Jenkins, this tool is for those who just want to deploy continously without doing much efforts. This tool is still in early phase of development. You should first test it then implement on prod servers.

#### Is this Secure?

Well, you have full access to source code, you can also do a code review. We're just using webhook from git and triggering some scripts internally, if you find any security issue please create an issue report.


## Authors

- [@rohitcoder - Rohit Kumar](https://github.com/rohitcoder)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Tech Stack

Python Flask Server, YAML, Linux

