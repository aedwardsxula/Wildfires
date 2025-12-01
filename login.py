from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional, Tuple
import os
import hashlib
import hmac

class Role(str, Enum):
    ADVISOR = "Advisor"
    TEACHER = "Teacher"
    STUDENT = "Student"

@dataclass
class User:
    username: str
    password_salt: bytes
    password_hash: bytes
    role: Role

class LoginManager:
    """
    Simple in-memory login/auth manager.
    - add_user(username, password, role)
    - authenticate(username, password) -> User | None
    - get_role(username) -> Role | None
    - is_advisor/teacher/student(username) -> bool
    """
    def __init__(self) -> None:
        self._users: Dict[str, User] = {}

    def _hash_password(self, password: str, salt: Optional[bytes] = None) -> Tuple[bytes, bytes]:
        if salt is None:
            salt = os.urandom(16)
        # PBKDF2-HMAC-SHA256 (secure & stdlib-only)
        pwd_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
        return salt, pwd_hash

    def _check_password(self, password: str, salt: bytes, expected_hash: bytes) -> bool:
        test_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
        return hmac.compare_digest(test_hash, expected_hash)
    
    def add_user(self, username: str, password: str, role: Role) -> None:
        username_key = username.strip().lower()
        if username_key in self._users:
            raise ValueError(f"User '{username}' already exists.")
        salt, pwd_hash = self._hash_password(password)
        self._users[username_key] = User(username=username, password_salt=salt, password_hash=pwd_hash, role=role)

    def authenticate(self, username: str, password: str) -> Optional[User]:
        username_key = username.strip().lower()
        user = self._users.get(username_key)
        if not user:
            return None
        if not self._check_password(password, user.password_salt, user.password_hash):
            return None
        return user
    
    def get_role(self, username: str) -> Optional[Role]:
        user = self._users.get(username.strip().lower())
        return user.role if user else None

    def is_advisor(self, username: str) -> bool:
        return self.get_role(username) == Role.ADVISOR

    def is_teacher(self, username: str) -> bool:
        return self.get_role(username) == Role.TEACHER

    def is_student(self, username: str) -> bool:
        return self.get_role(username) == Role.STUDENT

  
    def list_users(self) -> Dict[str, Role]:
        return {u.username: u.role for u in self._users.values()}