import re

# Define a list of known malicious patterns (signatures)
malicious_patterns = [
    r'select\s+\*',       # Matches "SELECT *"
    r'exec\s+\(',         # Matches "exec("
    r'\bdrop\b',          # Matches "drop" as a whole word
    r'\bdelete\b',        # Matches "delete" as a whole word
    # Add more patterns as needed
]

def detect_intrusion(log_entry):
    """
    Detects intrusion attempts in a log entry using signature-based detection.

    Args:
        log_entry (str): The log entry to analyze.

    Returns:
        bool: True if intrusion detected, False otherwise.
    """
    for pattern in malicious_patterns:
        if re.search(pattern, log_entry, re.IGNORECASE):
            return True
    return False

# Example log entries (replace with actual log data)
log_entries = [
    "User 'admin' logged in successfully.",
    "SQL query: SELECT * FROM users;",
    "Received HTTP request: DELETE /delete-user?id=123",
    "Potential SQL injection attempt: exec('DROP TABLE users')",
]

# Process log entries and detect intrusions
for log_entry in log_entries:
    if detect_intrusion(log_entry):
        print(f"Intrusion detected: {log_entry}")
    else:
        print("No intrusion detected.")
