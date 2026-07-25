#!/usr/bin/python3
"""提供 基于 AES 的基础加密功能"""

import base64
import hashlib

from Crypto.Cipher import AES

BLOCK_SIZE = 16  # Bytes


def do_pad(text: str) -> str:
    return text + (BLOCK_SIZE - len(text) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(text) % BLOCK_SIZE)


def aes_encrypt(key: str, data: str) -> str:
    """
    AES的ECB模式加密方法
    :param key: 密钥
    :param data:被加密字符串（明文）
    :return:密文
    """
    key_bytes = key.encode("utf-8")
    # 确保 key 长度是16的倍数 (AES ECB 模式要求)
    # 如果key长度超过32字节，截取前32字节
    # 如果key长度不足16字节，补位到16字节
    # 如果key长度在16-32之间且不是16的倍数，补位到下一个16的倍数
    if len(key_bytes) > 32:
        key_bytes = key_bytes[:32]
    elif len(key_bytes) < 16:
        key_bytes = key_bytes.ljust(16, b"\0")
    else:
        # 补位到16的倍数
        padding_len = (16 - len(key_bytes) % 16) % 16
        if padding_len:
            key_bytes = key_bytes + b"\0" * padding_len

    # 字符串补位
    data = do_pad(data)
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    result = cipher.encrypt(data.encode())
    encode_str = base64.b64encode(result)
    return encode_str.decode("utf-8")


def md5_encrypt(text: str) -> str:
    md = hashlib.md5()
    md.update(text.encode("utf-8"))
    return md.hexdigest()
