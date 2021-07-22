#3. 在全拼基础上改进打字编码方案，新旧方案对比

# !/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from xpinyin import Pinyin
py=Pinyin()
# 统计字符出现频率，生成映射表
def count_frequency(text):
    chars = []
    ret = []

    for char in text:
        if char in chars:
            continue
        else:
            chars.append(char)
            ret.append((char, text.count(char)))

    return ret


# 节点类
class Node:
    def __init__(self, frequency):
        self.left = None
        self.right = None
        self.father = None
        self.frequency = frequency

    def is_left(self):
        return self.father.left == self


# 创建叶子节点
def create_nodes(frequency_list):
    return [Node(frequency) for frequency in frequency_list]


# 创建Huffman树
def create_huffman_tree(nodes):
    queue = nodes[:]

    while len(queue) > 1:
        queue.sort(key=lambda item: item.frequency)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.frequency + node_right.frequency)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)

    queue[0].father = None
    return queue[0]


# Huffman编码
def huffman_encoding(nodes, root):
    huffman_code = [''] * len(nodes)

    for i in range(len(nodes)):
        node = nodes[i]
        while node != root:
            if node.is_left():
                huffman_code[i] = '0' + huffman_code[i]
            else:
                huffman_code[i] = '1' + huffman_code[i]
            node = node.father

    return huffman_code


# 编码整个字符串
def encode_str(text, char_frequency, codes):
    ret = ''
    for char in text:
        i = 0
        for item in char_frequency:
            if char == item[0]:
                ret += codes[i]
            i += 1

    return ret


# 解码整个字符串
def decode_str(huffman_str, char_frequency, codes):
    ret = ''
    while huffman_str != '':
        i = 0
        for item in codes:
            if item in huffman_str and huffman_str.index(item) == 0:
                ret += char_frequency[i][0]
                huffman_str = huffman_str[len(item):]
            i += 1

    return ret


if __name__ == '__main__':
    #text = input('The text to encode:')

    text=py.get_pinyin("u一个幽灵，共产主义的幽灵，在欧洲游荡。"
                                  u"为了对这个幽灵进行神圣的围剿，旧欧洲"
                                  u"的一切势力，教皇和沙皇、梅特涅和基佐、"
                                  u"法国的激进派和德国的警察，都联合起来了。"
                                  u"有哪一个反对党不被它的当政的敌人骂为共产党呢？又",' ')

    char_frequency = count_frequency(text)
    nodes = create_nodes([item[1] for item in char_frequency])
    root = create_huffman_tree(nodes)
    codes = huffman_encoding(nodes, root)

    huffman_str = encode_str(text, char_frequency, codes)
    #origin_str = decode_str(huffman_str, char_frequency, codes)

    print('Encode result:' + huffman_str)
    #print('Decode result:' + origin_str)


