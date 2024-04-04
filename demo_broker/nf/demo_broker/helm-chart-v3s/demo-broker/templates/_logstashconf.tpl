{{- define "demo_broker.logstashConf" -}}
input {
    file {
        path => "/var/log/{{ .Values.broker.name }}/{{ .Values.broker.name }}.log.1"
    }
}

filter {
    grok {
        match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} \[%{WORD:severity}\] msg: %{WORD:message}, mfa: %{GREEDYDATA:mfa}, peername: %{HOSTPORT:peername}?(, clientid: %{GREEDYDATA:client_id})?(, topic: %{GREEDYDATA:topic}, action: %{GREEDYDATA:action}, source: %{GREEDYDATA:source}|, reason: %{GREEDYDATA:reason})" }
    }

    mutate {
        replace => { "clientid" => "[REDACTED]" }
        replace => { "peername" => "[REDACTED]" }
        replace => { "username" => "[REDACTED]" }
    }
}

output {
    stdout { codec => rubydebug }
}
{{- end }}
