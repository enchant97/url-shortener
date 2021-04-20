import base64
import hashlib


def make_short_url(url: str) -> str:
    hashed = hashlib.sha256(url.encode()).digest()
    safe_hashed = base64.urlsafe_b64encode(hashed).decode()
    short_id = safe_hashed[:8]
    return short_id
