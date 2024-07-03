import datetime

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

with open("/etc/nginx/ssl/localhost.key", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "PT"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Aveiro"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Aveiro"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "ITAV"),
    x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
])

cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.now(datetime.timezone.utc)
).not_valid_after(
    datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName("localhost")]),
    critical=False,
).sign(key, hashes.SHA256(), default_backend())

with open("/etc/nginx/ssl/localhost.crt", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Generated new key and certificate")
