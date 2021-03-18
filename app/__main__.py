from tortoise import Tortoise

if __name__ == '__main__':
    from config import TORTOISE_ORM

    await Tortoise.init(TORTOISE_ORM)
