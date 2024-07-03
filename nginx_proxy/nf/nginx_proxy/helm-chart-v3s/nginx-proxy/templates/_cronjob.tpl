{{- define "nginx_proxy.cronjob" -}}
*/{{ $.Values.interval }} * * * * root python /app/main.py && /usr/sbin/service nginx reload >> /var/log/cron.log 2>&1
{{- end }}
