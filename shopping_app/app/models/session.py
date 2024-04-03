class Session:
    def __init__(self, session_id, user_id, timestamp, is_active, logout_time=None):
        self.session_id = session_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.is_active = is_active
        self.logout_time = logout_time

    def __json__(self):
        return {
            'session_id': self.session_id,
            'user_id': self.user_id,
            'timestamp': self.timestamp,
            'is_active': self.is_active,
            'logout_time': self.logout_time
        }
    
    def __str__(self):
        return f"Session {self.session_id}: User {self.user_id} - Active: {self.is_active}"
    
