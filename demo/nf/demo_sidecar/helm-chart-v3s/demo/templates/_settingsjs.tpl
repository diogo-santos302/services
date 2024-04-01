{{- define "demo.settingsJs" -}}
var server = "ws://{{ .Values.webrtc.name }}.{{ .Values.namespace | default "default" }}.svc.cluster.local:8188";
var iceServers = null;
{{- end }}
