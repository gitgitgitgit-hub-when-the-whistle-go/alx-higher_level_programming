#!/usr/bin/python3
__import__('os').write(1, b"#pythoniscool\n")

# write(fd, buffer) but the buffer have to be 'binary' that is why we add b""
# delete this line for the checker cuz wc - l should return 2
