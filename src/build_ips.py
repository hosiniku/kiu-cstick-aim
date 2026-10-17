"""Build code.ips from src/<region>.tsv (no ROM needed).

    python3 src/build_ips.py jpn code.ips
    python3 src/build_ips.py usa code.ips
    python3 src/build_ips.py eur code.ips

Each row is one 32-bit ARM word written at a virtual address. code.ips offsets are
relative to the start of .text (0x00100000), which is what Luma3DS and Azahar expect.
"""
import os
import struct
import sys

BASE = 0x00100000


def main(region, out):
    here = os.path.dirname(os.path.abspath(__file__))
    rows = []
    with open(os.path.join(here, region + '.tsv'), encoding='utf-8') as f:
        next(f)
        for line in f:
            addr, word = line.split('\t')[:2]
            rows.append((int(addr, 16) - BASE, int(word, 16)))
    rows.sort()
    recs = []
    for off, w in rows:                      # merge consecutive words into one record
        if recs and recs[-1][0] + len(recs[-1][1]) == off:
            recs[-1][1].extend(struct.pack('<I', w))
        else:
            recs.append([off, bytearray(struct.pack('<I', w))])
    b = bytearray(b'PATCH')
    for off, data in recs:
        assert off < 0x1000000 and off != 0x454f46 and len(data) < 0x10000
        b += off.to_bytes(3, 'big') + len(data).to_bytes(2, 'big') + data
    b += b'EOF'
    with open(out, 'wb') as f:
        f.write(b)
    print('%s: %d bytes, %d words' % (out, len(b), len(rows)))


if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] not in ('jpn', 'usa', 'eur'):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
