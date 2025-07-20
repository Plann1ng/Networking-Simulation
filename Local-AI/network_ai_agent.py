# network_ai_agent.py

from netmiko import ConnectHandler
from flask import Flask, request, jsonify
import subprocess

# === DEVICE CONFIG ===
DEVICE = {
    'device_type': 'cisco_ios',
    'host': '10.10.10.2',  # Example SW1 IP
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco'
}

# === BASIC COMMAND WRAPPER ===
def run_command(command):
    try:
        conn = ConnectHandler(**DEVICE)
        conn.enable()
        output = conn.send_command(command)
        conn.disconnect()
        return output
    except Exception as e:
        return f"Error: {e}"

# === LLM LOGIC ===
OLLAMA_API_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are a Cisco network engineer assistant.
You can solve network issues by suggesting or running commands like:
- show ip int brief
- show ip route
- interface <int> + no shutdown
You have access to a run_command(cmd) function.
Never ask the user for help — diagnose and fix.
"""

def query_llm(user_input):
    prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAI:"
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=data)
    return response.json().get("response", "No response")

# === FLASK API TO TALK TO LLM ===
app = Flask(__name__)

@app.route("/interact", methods=["POST"])
def interact():
    data = request.json
    user_input = data.get("input", "")
    llm_response = query_llm(user_input)
    return jsonify({"response": llm_response})

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    cmd = data.get("command")
    output = run_command(cmd)
    return jsonify({"output": output})

# === LOCAL START ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
