rule MalwarePayload {
    strings:
        $malicious = "Your computer is infected..."
    condition:
        $malicious
}
