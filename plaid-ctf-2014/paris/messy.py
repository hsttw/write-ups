# super-messy solution for plaidctf2014/paris, too lazy to clean it up, please don't judge too harshly


xor_keys = 'a92df26d2e34aa557ac394cca211d8b9a5f0e28c54cb5d18d8795f3a159edaeafc772b914f2129261f608fc4be6387d8811e3f76e861eb94f6fa7447fb52ba537c596f513ec8ee2f3a69801acf7460cd0fc972c7f945ad9145954514cff5576f395ad83cdf96f0ce90be298efe67d77b8d4f22d97a764798504af7474c92634498d9342df8c295cad4bc89c6986416bcade20efdd0586d75c910d65b0f2abbcf323db44aff36b5d2274a91b8a60c333a35f266397f7afb4b35411ec250e14fd560b41e7de435dcfc3ba978f566ada05e9317db995961862f6f63f8f6effb94479b17d85d082640e91c73f51a4db48502e9cfcf1465ca74e7f99db61ac1a7f294'.decode('hex')
mem_200h = [0xaef2, 0x4f8b, 0xc349, 0xa3e5, 0x1aa3, 0xa52d, 0x7a90, 0x88e, 0xfe5, 0x6141, 0xd752, 0xc040, 0xa978, 0x2b5d, 0xc48b, 0xc233, 0xcb42, 0x8122, 0x3e77, 0xef09, 0x6ccb, 0xb0cf, 0xc4f4, 0x1075, 0x93c1, 0xd9ae, 0xec1d, 0x11e8, 0xdc16, 0x3b2d, 0x6c25, 0xc5b8, 0xc1c3, 0xa91c, 0x8518, 0xabe1, 0xd01d, 0xa00c, 0x43b9, 0xe397, 0xb585, 0x20db, 0xfc48, 0xcd1e, 0x5b79, 0xbdbb, 0xe302, 0xe432, 0xc063, 0x951d, 0x48ca, 0x9d63, 0x2287, 0xe9aa, 0x267e, 0xa26, 0x379b, 0x5450, 0x61cc, 0x7e13, 0xf85a, 0xf7bf, 0x4545, 0xab82, 0x6f1c, 0xe8ab, 0x4827, 0x2507, 0xab71, 0x2942, 0xc373, 0xe455, 0xf654, 0xd60b, 0x3917, 0xaeb5, 0x5ce8, 0x585, 0x2ce5, 0x3cdd, 0xda3b, 0x7d09, 0x42c4, 0x1286, 0x2b8b, 0x9972, 0x86f8, 0xc39d, 0x65f1, 0x2e85, 0x5305, 0x486f, 0x13ed, 0xab9c, 0x4468, 0x357, 0xa66a, 0x9ed7, 0xe6b9, 0xa316, 0xf627, 0x5acc, 0xcbc6, 0x6ea, 0xca05, 0x954f, 0x9390, 0x4272, 0xa3ce, 0x1a08, 0x2a47, 0xd0b8, 0x2976, 0x2486, 0xe562, 0xd032, 0xb27d, 0xc70d, 0xa7ad, 0x98ee, 0xb926, 0x9ddd, 0xa657, 0xe98b, 0x3e13, 0xe42, 0xaf3d, 0x19e4, 0x7d2b, 0x9017, 0x52c4, 0x5b9e, 0x96d4, 0x6d5f, 0xe7dc, 0x9908, 0xb2a, 0xe554, 0xe0a4, 0x7ca1, 0x5681, 0x2f2, 0x4676, 0xb64c, 0xe3da, 0x4af6, 0x7c0, 0x6b1b, 0x8a16, 0x6a0f, 0x180d, 0x8cf6, 0xb3cc, 0x6ac2, 0xe9bd, 0xe3d, 0x15f6, 0x4c7c, 0x6157, 0xa9f2, 0x5b08, 0x7206, 0x9b97, 0xf6fb, 0x7db0, 0x6989, 0x3daf, 0x93fd, 0xa0bd, 0x24c5, 0xe3d1, 0x8720, 0xbce9, 0x8d56, 0x7a2d, 0x66b3, 0xe95c, 0xc9da, 0x4bae, 0x53b0, 0x8f15, 0xf1f2, 0xa399, 0x283b, 0x5bcb, 0x319c, 0x7beb, 0xf1c2, 0x8c5b, 0xdcbf, 0x66c5, 0xb2b9, 0xdca6, 0x5226, 0x3039, 0x5564, 0x4b9b, 0xe100, 0xe041, 0x2b1, 0xde55, 0xeac9, 0x2d27, 0xd945, 0xd227, 0x3e17, 0xb488, 0xbd3e, 0xe4b0, 0x6825, 0x9b65, 0xdab, 0xa3fb, 0xdc2c, 0x58cf, 0x5898, 0xeaeb, 0x571, 0x60e1, 0x5695, 0xe6f0, 0x3b34, 0x287d, 0x4565, 0x270, 0xad37, 0x702a, 0x46b0, 0x9cef, 0xc0f8, 0x2d56, 0x3a49, 0x19c9, 0xb1f7, 0x2846, 0x64ef, 0x701, 0xbe58, 0xe7ec, 0x8db4, 0xb1d6, 0x9eac, 0x12f4, 0xbb9e, 0x337a, 0x9339, 0x3882, 0x3482, 0xc38c, 0x8800, 0x128e, 0xc39c, 0x624d, 0xdc2f, 0x5a7c, 0xa5aa]
desired_stack = [0x2e0b, 0x6d02, 0x7492, 0x870c, 0x93b9, 0xedb3, 0x312c, 0x7107, 0x7d10, 0x2007, 0xe7c6, 0x3a1b, 0xbad8, 0x9417, 0xfa6b, 0xbe6c, 0x621d, 0x4d3b, 0x47ad, 0x7a7a, 0x3e9d, 0x53a2, 0xf22f, 0xd1a9, 0xf574, 0x8173, 0x11bc, 0xae15, 0x6179, 0x5a4d]
desired_stack.reverse()


def xor_200h(k):
    k = (ord(xor_keys[k]) << 8) | ord(xor_keys[k])
    for i in xrange(len(mem_200h)):
        mem_200h[i] ^= k


def bruteforce(val):
    '''bruteforce candidate values to produce the desired index'''
    res = []
    printable = range(0x20, 0x80)
    for x in xrange(0x10000):
        c = (x - 0x3332) & 0xffff
        hi = c >> 8
        lo = c & 0xff
        if hi ^ lo == val and (x >> 8) in printable and (x & 0xff) in printable:
            res.append(x)
    return res


# generate lists of lists of possible first/second character for each stack value
first_chars_lists = []
second_chars_lists = []
for i in xrange(0, len(desired_stack)-1):
    val = mem_200h.index(desired_stack[i+1] ^ desired_stack[i])
    first, second = zip(*map(lambda x: (x >> 8, x & 0xff), bruteforce(val)))
    first_chars_lists.append(map(chr, first))
    second_chars_lists.append(map(chr, second))
    xor_200h(i)


# backtrack and generate the solution based on the lists
def recursive(c, first_chars_lists, second_chars_lists):
    if len(first_chars_lists) == 1:
        if c in first_chars_lists[0]:
            return c, second_chars_lists[first_chars_lists[0].index(c)]
        else:
            return None
    else:
        if c in first_chars_lists[0]:
            return c, recursive(second_chars_lists[0][first_chars_lists[0].index(c)], first_chars_lists[1:], second_chars_lists[1:])
        else:
            return None


for c in first_chars_lists[0]:
    print recursive(c, first_chars_lists, second_chars_lists)
