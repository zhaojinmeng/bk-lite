import base64

from cryptography.fernet import Fernet
from django.conf import settings


class EncryptMixin:
    @staticmethod
    def get_cipher_suite():
        key = base64.urlsafe_b64encode(settings.SECRET_KEY.encode()[:32])
        return Fernet(key)

    @classmethod
    def encrypt_field(cls, field_name, field_dict=None):
        cipher_suite = cls.get_cipher_suite()
        field_dict = field_dict if field_dict is not None else {}
        field_value = field_dict.get(field_name)
        if field_value:
            try:
                cipher_suite.decrypt(field_value.encode())
            except Exception:
                encrypted_value = cipher_suite.encrypt(field_value.encode())
                field_dict[field_name] = encrypted_value.decode()

    @classmethod
    def decrypt_field(cls, field_name, field_dict=None):
        cipher_suite = cls.get_cipher_suite()
        field_dict = field_dict if field_dict is not None else {}
        field_value = field_dict.get(field_name)
        if field_value:
            try:
                decrypted_value = cipher_suite.decrypt(field_value.encode())
                field_dict[field_name] = decrypted_value.decode()
            except Exception:
                pass
