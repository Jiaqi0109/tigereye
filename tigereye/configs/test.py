from tigereye.configs.default import DefalutConfig


class TestConfig(DefalutConfig):
    TESTING = True
    JSON_SORT_KEYS = False
    SQLALCHEMY_ECHO = False
    # 不写路径，保存在内存中
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
