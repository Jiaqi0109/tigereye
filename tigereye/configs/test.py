from tigereye.configs.default import DafalutConfig


class TestConfig(DafalutConfig):
    TESTING = True
    JSON_SORT_KEYS = False
    SQLALCHEMY_ECHO = False
    # 不写路径，保存在内存中
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
