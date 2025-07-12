from fastmcp import FastMCP
import requests
import os

# The official GitHub MCP server is missing some tools that are necessary for the security agent.
# This MCP server adds those tools.

mcp = FastMCP("Extra GitHub Tools")


@mcp.tool
async def add_reviewer_to_pr(
    repo_owner: str, repo_name: str, pr_number: int, reviewer_username: str
):
    """Add a reviewer to a GitHub pull request"""
    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.post(
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/requested_reviewers",
        headers=headers,
        json={"reviewers": [reviewer_username]},
    )
    return response.json()


@mcp.tool
async def get_dependabot_alerts(repo_owner: str, repo_name: str):
    """Get all dependabot alerts for a repository"""
    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.get(
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/dependabot/alerts",
        headers=headers,
    )
    return response.json()


@mcp.tool
async def get_dependabot_alert(repo_owner: str, repo_name: str, alert_id: str):
    """Get a dependabot alert for a repository"""
    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.get(
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/dependabot/alerts/{alert_id}",
        headers=headers,
    )
    return response.json()


if __name__ == "__main__":
    mcp.run()
