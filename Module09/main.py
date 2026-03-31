import asyncio

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.product import Product
from models.student import Student
from beanie.operators import Set


async def init():
    client = AsyncIOMotorClient("mongodb://localhost:27017/")
    db = client["test_db"]
    await init_beanie(database=db, document_models=[Student, Product])

    s = await Student.insert_one(Student(univ_id="00123456", name="Hawk Eye"))
    print(s)

    s = await Student.find_one(Student.univ_id == "00123456").update_one(
        Set({Student.name: "Hawkeye"})
    )
    print(s)

    s = await Student.find_one(Student.univ_id == "00123456")
    print(s)

    p = await Product.insert_one(Product(name="projector", category="Office Staples"))
    print(p)


asyncio.run(init())
