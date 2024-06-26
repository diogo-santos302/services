# cipher_proxy
NGINX proxy for ciphering traffic. A time interval can be specified after which the ciphers used will be changed.

## Security characteristics:
- SSL protocols
    - TLSv1
    - TLSv1.1
    - TLSv1.2 
    - TLSv1.3
- SSL ciphers (HIGH:!aNULL:!MD5)
- Cipher change interval

## Possible mutated fields
- NGINX port
- Certificates
- SSL protocols
- SSL ciphers
- Session timeout
- Cipher change interval
- File locations
- NGINX configuration
- VM image
