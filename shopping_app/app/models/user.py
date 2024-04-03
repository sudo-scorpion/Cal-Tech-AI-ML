class User:
    def __init__(self, user_id, username, password, email, user_role, session_id=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.user_role = user_role
        self.session_id = session_id

    def __json__(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'user_role': self.user_role,
            'session_id': self.session_id
            # Omit password for security reasons
        }
    
    def __str__(self):
        return f"User {self.user_id}: {self.username} ({self.email}) - {self.user_role}"