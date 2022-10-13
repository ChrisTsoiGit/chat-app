# from model import BlogPost, BlogComment
# #mango db driver
# import motor.motor_asyncio
# #connectoin between database.py and mango db
# client = motor.motor_asyncio.AsyncIOMotorClient('mangodb://localhoast:27017')
# database = client.Blog
# collection = database.blog

# async def fetch_a_blog_post(user):
#     document = await collection.find_one("user":user)
#     return document

# async def fetch_all_blogs():
#     blogs = []
#     cursor = collection.find({})
#     async for document in cursor:
#         blogs.append(BlogPost(**document))
#     return blogs

# async def create_a_blog(blog):
#     document = blog
#     result = await collection.insert_one(document)
#     return document

# async def update_blog(id, desc):
#     await collection.update_one({'desc':desc},)
