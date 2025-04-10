import random
import string


def generate_random_email(length=12, domain="example.com"):
    allowed_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    username = ''.join(random.choices(allowed_chars, k=length))
    return f"{username}@{domain}"


def generate_random_strong_password(length=12):
    if length < 4:
        raise ValueError("Пароль должен быть длиной хотя бы 4 символа")

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()-_=+[]{};:,.<>?")
    ]

    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)


def generate_random_emails(email_count=1, email_length=12, email_domain="example.com"):
    emails = [generate_random_email(length=email_length, domain=email_domain) for _ in range(email_count)]
    return emails


def generate_random_strong_passwords(password_count=1, password_length=12):
    passwords = [generate_random_strong_password(password_length) for _ in range(password_count)]
    return passwords
