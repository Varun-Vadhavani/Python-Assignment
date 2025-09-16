import base64

msg = "Hello$World"
msg_bytes = msg.encode("utf-8")
base64_bytes = base64.b64encode(msg_bytes)
base64_string = base64_bytes.decode("utf-8")

print("Original:", msg)
print("Base64: ", base64_string)