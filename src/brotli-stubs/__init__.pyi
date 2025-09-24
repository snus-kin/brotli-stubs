class BrotliError(Exception): ...

def compress(
    string: bytes,
    *,
    mode: int = ...,
    quality: int = ...,
    lgwin: int = ...,
    lgblock: int = ...,
    dictionary: bytes = ...,
) -> bytes: ...
def decompress(string: bytes, *, dictionary: bytes = ...) -> bytes: ...
