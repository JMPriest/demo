# demo
Several useful methods.
# CLASSES
    builtins.object
        FTPConnection
    
    class FTPConnection(builtins.object)
     |  FTPConnection(host='', port=21, username='', pwd='')
     |  
     |  Methods defined here:
     |  
     |  __init__(self, host='', port=21, username='', pwd='')
     |  
     |  close(self)
     |  
     |  connect(self)
     |  
     |  download(self, remote_path, local_path)
     |  
     |  upload(self, local_path, target_path)
     |  
     |  ----------------------------------------------------------------------

# FUNCTIONS
    check_dict_path(d, *indices)
        检查*indices中的层级键名是否在嵌套字典d中
        :param d:需要查询的嵌套字典
        :param indices:键名，例如'cvrfdoc', 'Vulnerability'查询了是否有d['cvrfdoc']['Vulnerability']这个键
        :return:boolean值
    
    replace_with_dict(original: str, pair: dict) -> str
        将来源String中匹配pair中的key的值替换为value
        :param original: 原始string
        :param pair: 替换对
        :return: 结果string
    
    replace_with_re_dict(original: str, pair: dict) -> str
        将original字符串中，符合re_string正则表达式部分的字符串改为replace_to的内容
        :param pair:
        :param original: 原始string
        :param pair: 正则表达式为key，替换的内容为value的键值对
        :return: 结果string
