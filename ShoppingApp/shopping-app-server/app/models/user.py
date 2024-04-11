class User:
    def __init__(self, id, username, email, password, role, session_id):
        self.id = id
        self.username = username
        self.email = email
        self.password = password 
        self.role = role
        self.session_id = session_id
