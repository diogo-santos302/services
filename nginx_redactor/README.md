# nginx_redactor
Network service that takes NGINX logs, passes them through a privacy quantifier (current implementation randomly assigns a severity level of LOW, MEDIUM or HIGH to every log) which classifies them and sends them to an ELK stack, which uses Logstash for anonymizing IPs of logs with a high severity level, replacing them with a redacted string. These logs are then available in Elasticsearch and observable through Kibana.

Privacy characteristics
- 3 severity levels for logs (LOW, MEDIUM and HIGH)
- Anonymization of client IP addresses
