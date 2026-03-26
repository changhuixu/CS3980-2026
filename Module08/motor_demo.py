from motor.motor_asyncio import AsyncIOMotorClient
import asyncio


async def main():
    client = AsyncIOMotorClient("mongodb://localhost:27017/")

    a = client.address
    print(a)

    b = client.get_default_database
    print(b)

    databases = await client.list_database_names()
    print(databases)

    server_info = await client.server_info()
    print(server_info)


asyncio.run(main())
