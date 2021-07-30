import re
from ftplib import FTP


def check_dict_path(d, *indices):
    """
    检查*indices中的层级键名是否在嵌套字典d中
    :param d:需要查询的嵌套字典
    :param indices:键名，例如'cvrfdoc', 'Vulnerability'查询了是否有d['cvrfdoc']['Vulnerability']这个键
    :return:
    """
    sentinel = object()
    for index in indices:
        if d is None:
            return False
        d = d.get(index, sentinel)
        if d is sentinel:
            return False
    return True


def replace_with_dict(original: str, pair: dict) -> str:
    """
    将来源String中匹配pair中的key的值替换为value
    :param original: 原始string
    :param pair: 替换对
    :return: new_string: 结果string
    """
    new_string = original
    for p in pair:
        new_string = new_string.replace(p, str(pair[p]))
    return new_string


def replace_with_re_dict(original: str, pair: dict) -> str:
    """
    将original字符串中，符合re_string正则表达式部分的字符串改为replace_to的内容
    :param pair:
    :param original: 原始string
    :param pair: 正则表达式为key，替换的内容为value的键值对
    :return:
    """
    new_string = original
    for p in pair:
        new_string = re.sub(p, pair[p], new_string)
    return new_string


class FTPConnection(object):

    def __init__(self, host='', port=21, username='', pwd=''):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.ftp = FTP()

    def connect(self):
        self.ftp.connect(self.host, self.port)
        self.ftp.login(self.username, self.pwd)

    def close(self):
        self.ftp.close()

    def upload(self, local_path, target_path):
        # 连接，上传
        with open(local_path, 'rb') as fp:
            self.ftp.storbinary('STOR ' + target_path, fp)

    def download(self, remote_path, local_path):
        bufsize = 1024
        with open(local_path, 'wb') as fp:
            self.ftp.retrbinary('RETR ' + remote_path, fp.write, bufsize)

