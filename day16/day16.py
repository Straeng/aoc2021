#!/usr/bin/env python
import operator
from functools import reduce


"""
|ver | type id | literal/operator |
 3b    3b

type id:

4: literal value 1nnnn, 1nnnn, ..., 0nnnn
x: operator
    T
   |0|<length in bits of subpackets>|<subpkts>
       15 bits
   |1|<nbr of subpkts>|<subpkts>
       11 bits
    

"""


class BinData:

    def __init__(self, hexstr):
        self.bin = bin(int(hexstr, 16))[2:].zfill(len(hexstr)*4)

    def _consume(self, n):
        self.bin = self.bin[n:]

    def number(self, n):
        nbr = int(f'0b{self.bin[:n]}', 2) 
        self._consume(n)
        return nbr

    def hexstr(self, n):
        return hex(self.number(n))

    def literal(self):
        v = 0
        while True:
            more = self.number(1) == 1
            v <<= 4
            v += self.number(4)
            if not more:
                break
        return v

    def len(self):
        return len(self.bin)


def perform_op(type_id, values):
    if type_id == 0:
        return sum(values)
    elif type_id == 1:
        return int(reduce(operator.mul, values))
    elif type_id == 2:
        return min(values)
    elif type_id == 3:
        return max(values)
    elif type_id == 5:
        return 1 if values[0] > values[1] else 0
    elif type_id == 6:
        return 1 if values[0] < values[1] else 0
    elif type_id == 7:
        return 1 if values[0] == values[1] else 0


def parse_packet(bd, versions):
    ver = bd.number(3)
    versions.append(ver)
    type_id = bd.number(3)

    if type_id == 4:
        value = bd.literal()
    else:
        values = []
        if bd.number(1) == 0:
            len_bits = bd.number(15)
            start_len = bd.len()
            while True:
                values.append(parse_packet(bd, versions))
                if start_len - bd.len() == len_bits:
                    break
        else:
            len_pkts = bd.number(11)
            for _ in range(len_pkts):
                values.append(parse_packet(bd, versions))
        value = perform_op(type_id, values)
    return value


test = {
    "C200B40A82": 3,
    "04005AC33890": 54,
    "880086C3E88112": 7,
    "CE00C43D881120": 9,
    "D8005AC2A8F0": 1,
    "F600BC2D8F": 0,
    "9C005AC2F8F0": 0, 
    "9C0141080250320F1802104A08": 1
}

for d, v in test.items():
    bd = BinData(d)
    assert parse_packet(bd, []) == v

with open('input', 'r') as f:
    data = f.read().strip()

bd = BinData(data)
versions = []
value = parse_packet(bd, versions)
print(f'Part 1: {sum(versions)}')
print(f'Part 2: {value}')
