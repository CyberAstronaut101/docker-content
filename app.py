import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

agent = os.getenv('AGENT_NAME', 'no-agent-name-set')


def get_agent_name():
    """Returns the name of the agent"""
    return agent


@app.route('/')
def get_current_time():
    """Returns the current time"""
    return {
        'time': datetime.now().isoformat(),
        'days_since_y2k': days_since_y2k(),
        'agent': get_agent_name()
    }


def days_since_y2k():
    """Returns the number of days since the year 2000"""
    return (datetime.now() - datetime(2000, 1, 1)).days


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
