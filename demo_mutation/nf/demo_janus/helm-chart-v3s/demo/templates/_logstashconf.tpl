{{- define "demo.logstashConf" -}}
input {
    file {
        path => "/var/log/janus/janus.log"
    }
}

filter {
    grok {
        match => { "message" => "\[%{DAY:day} +%{MONTH:month} +%{MONTHDAY:monthday} %{TIME:time} %{YEAR:year}\](?: \[(?<severity>[A-Z]+)\])?(?: \[(?<session>WSS-0x%{BASE16NUM})\]| \[(?<handle>[0-9]+)\])?(?: \[(?<plugin>janus\.plugin\.[^\]]+)\])? %{GREEDYDATA:message}" }
    }

    mutate {
        replace => { "session" => "REDACTED" }
        replace => { "plugin" => "REDACTED" }
        replace => { "handle" => "REDACTED" }
    }

    mutate {
        gsub => [
            "message", "\b\d{5,}\b", "[REDACTED]",
            "message", "0x[a-fA-F0-9]+\b", "[REDACTED]"
        ]
    }
}

output {
    stdout { codec => rubydebug }
}
{{- end }}
