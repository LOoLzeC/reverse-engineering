import zlib, base64
print zlib.decompress(base64.b64decode('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'))
