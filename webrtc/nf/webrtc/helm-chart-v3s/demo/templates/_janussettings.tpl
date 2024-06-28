{{- define "demo.janusSettings" -}}
var server = [
    "ws://webrtc:8188",
    "wss://localhost:8188",
    "wss://webrtc:8188",
    "ws://webrtc.default.svc.cluster.local:8188",
    "wss://webrtc.default.svc.cluster.local:8188",
];
var iceServers = null;
{{- end }}
