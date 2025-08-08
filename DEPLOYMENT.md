# Deployment Guide

Easy Agents is designed as a flexible template that you can customize and deploy to fit your environment. Here are several deployment options for productionizing Easy Agents:

## 1. Local Deployment

Easy Agents can run locally out of the box. The downside is that it requires some manual trigger to initiate the agent. You can do so by making HTTP requests to the endpoints defined in `main.py`. 

It'd also be very easy to build a custom frontend to interact with Easy Agents if you'd prefer a UI.

![Example Local Web UI](https://static.kpolley.com/easyagents/example_web_ui.png)

## 2. Remote Server Deployment

Deploy Easy Agents to a cloud server (e.g., AWS EC2) and expose it through a load balancer for production use. 

**Steps:**
1. Launch an EC2 instance with appropriate security groups
2. Install dependencies and deploy Easy Agents
3. Set up 3rd party tools (ex. SIEM) to send alerts to the relevant Easy Agent endpoint. 

![Example Remote Server Deployment](https://static.kpolley.com/easyagents/example_remote_server.png)

## 3. Kubernetes Deployment

Kubernetes deployment requires special consideration for MCP servers that depend on Docker. There are a few ways to do this, but I'd suggest running each MCP server as its own Kubernetes deployment.

**Steps:**
1. Create Kubernetes manifests for Easy Agents and MCP servers
2. Set up ingress controllers for external access
3. Set up 3rd party tools (ex. SIEM) to send alerts to the relevant Easy Agent endpoint. 

![Example Kubernetes Deployment](https://static.kpolley.com/easyagents/example_k8s_deployment.png)