#!/usr/bin/python3
"""基于 aes文件 基础加密功能 封装 openapi签名算法"""

import orjson

from .aes import aes_encrypt, md5_encrypt


class SignBase:

    @classmethod
    def generate_sign(cls, encrypt_key: str, request_params: dict) -> str:
        """
        生成签名
        """
        canonical_querystring = cls.format_params(request_params)
        md5_str = md5_encrypt(canonical_querystring).upper()
        return aes_encrypt(encrypt_key, md5_str)

    @classmethod
    def format_params(cls, request_params: None | dict = None) -> str:
        """
        格式化 params
        """
        if not request_params or not isinstance(request_params, dict):
            return ''

        canonical_strs = []
        sort_keys = sorted(request_params.keys())
        for k in sort_keys:
            v = request_params[k]
            if v == "":
                continue
            if isinstance(v, (dict, list)):
                canonical_strs.append(f"{k}={orjson.dumps(v, option=orjson.OPT_SORT_KEYS).decode()}")
            elif isinstance(v, bool):
                canonical_strs.append(f"{k}={str(v).lower()}")
            else:
                canonical_strs.append(f"{k}={v}")
        return "&".join(canonical_strs)
