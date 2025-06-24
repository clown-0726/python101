import boto3
from enum import Enum
from threading import Lock


class SSMParameterEnumLoader:
    _instance = None
    _lock = Lock()

    def __new__(cls, path, region_name='us-west-2', with_decryption=True):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self, path, region_name='us-west-2', with_decryption=True):
        if self._initialized:
            return  # 避免重复初始化

        self.path = path
        self.region_name = region_name
        self.with_decryption = with_decryption
        self.ssm = boto3.client('ssm', region_name=self.region_name)
        self.parameter_cache = {}
        self.enum_class = None

        self._load_parameters()
        self._initialized = True

    def _load_parameters(self):
        parameters = []
        next_token = None

        while True:
            kwargs = {
                'Path': self.path,
                'Recursive': True,
                'WithDecryption': self.with_decryption,
                'MaxResults': 10
            }
            if next_token:
                kwargs['NextToken'] = next_token

            response = self.ssm.get_parameters_by_path(**kwargs)
            parameters.extend(response['Parameters'])

            next_token = response.get('NextToken')
            if not next_token:
                break

        enum_dict = {}
        for param in parameters:
            key = self._normalize_key(param['Name'])
            value = param['Value']
            self.parameter_cache[key] = value
            enum_dict[key] = key  # 枚举值为 key 名

        self.enum_class = Enum('AppConfig', enum_dict)

    def _normalize_key(self, name):
        """将参数名转换为枚举名"""
        key = name.replace(self.path, '').replace('/', '_').upper()
        return key

    def get_enum(self):
        return self.enum_class

    def get_value(self, enum_member):
        return self.parameter_cache.get(enum_member.name)

    def reload(self):
        """手动刷新参数缓存"""
        self.parameter_cache.clear()
        self._load_parameters()


if __name__ == "__main__":
    # 初始化一次（路径指定）
    loader = SSMParameterEnumLoader('/orbit/')
    AppConfig = loader.get_enum()

    # 使用枚举
    print(AppConfig.LANG_EN.name)  # 输出：EN

    # 获取值（缓存中）
    value = loader.get_value(AppConfig.LANG_EN)
    print("EN =", value)
