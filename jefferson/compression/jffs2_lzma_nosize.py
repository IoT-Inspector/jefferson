import lzma


def decompress(data, outlen):
    # LZMA stream with stripped 'uncompressed_size' field, so we inject one
    fake_size = outlen.to_bytes(8, "little")
    decompressed = lzma.decompress(data[0:5] + fake_size + data[5:])
    return decompressed
