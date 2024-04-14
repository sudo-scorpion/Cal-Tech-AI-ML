class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, username, session_id, role):
        self.sessions[username] = {
            'session_id': session_id,
            'role': role
        }

    def get_session(self, username):
        return self.sessions.get(username)

    def delete_session(self, username):
        if username in self.sessions:
            del self.sessions[username]