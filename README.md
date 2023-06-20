```bash
# Build python flask docker image
docker build -t flask-agent:latest .

# Run the flask agent
docker run -p 5000:5000 -e AGENT_NAME='demo_agent' flask-agent
# detached with env var for flask set
docker run -d -p 5000:5000 -e AGENT_NAME='demo_agent' flask-agent
```


## Second Part: Multiple Agents

```bash
# NOTE: Assumes previous flask-agent image is built and present on system