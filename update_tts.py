import os
from retell import Retell
from retell.errors import APIError

# --- CONFIGURATION ---
# IMPORTANT: The actual secret key must be placed inside the quotation marks.
RETELL_API_KEY = "key_1928abb828325b516005dee51e7f"
AGENT_ID = "ag_0ea0a1d1176ac160d90908d4bd" # Use the correct 'ag_' prefix for the Agent ID

# Your live server URL from Render
CUSTOM_TTS_URL = "https://shivai1978-tts-server.onrender.com/synthesize"

# Data to update the agent with
UPDATE_DATA = {
    "tts_provider": "external_tts",
    "tts_url": CUSTOM_TTS_URL,
}

# --- API CALL ---
try:
    # 1. Initialize the client using the variable name (RETELL_API_KEY)
    client = Retell(api_key=RETELL_API_KEY)
    
    # 2. Make the API call using the SDK method
    # Use the variable AGENT_ID for printing
    print(f"Attempting to update agent: {AGENT_ID}...")
    agent_response = client.agent.update(
        agent_id=AGENT_ID,
        **UPDATE_DATA
    )
    
    # 3. Print success message
    print("\n--- ✅ SUCCESS ---")
    print(f"Agent ID {agent_response.agent_id} successfully updated!")
    print(f"TTS Provider set to: {agent_response.tts_provider}")
    print("Your voice is now connected! Test in the Retell dashboard.")

except APIError as e:
    # 4. Handle errors (like invalid ID, invalid API key, etc.)
    print("\n--- 🛑 FAILURE ---")
    print(f"Retell API Error: Status {e.status_code}")
    print(e.message)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
