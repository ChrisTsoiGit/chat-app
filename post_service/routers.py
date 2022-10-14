from fastapi import APIRouter
from model import BlogComment, BlogPost


router = APIRouter()

# get all blogs
@router.get("/blogs", response_model = BlogPost)
def get_blogs(blogs:BlogPost):
    return blogs

# get a blog
@router.get("/blog/{id}", response_model = BlogPost)
def get_blog(blog:BlogPost):
    return blog

#deleat a blog
@router.delete("/blog/{id}", response_model = BlogPost)
def delete_blog(blog:BlogPost):
    return blog

# post blog
@router.post('/create-blog', response_model = BlogPost)
def create_blogpost(blog: BlogPost):
    return blog

# @router.post("/create-blog", response_model=BlogPost)
# async def post_todo(blog: BlogPost):
#     response = await create_todo(todo.dict())
#     if response:
#         return response
#     raise HTTPException(400, "Something went wrong" )

# #update post description
# @router.update("/blog/{id}", response_model = BlogPost)
# def get_blog(blog:BlogPost, data:BlogPost):
#     return blog

# get all comments
@router.get("/blog-comments", response_model = BlogComment)
def get_comments(blog_comments:BlogComment):
    return blog_comments

#post comment
@router.post('/create-comment', response_model = BlogPost)
def create_blogcomment(comment: BlogComment):
    return comment

#deleat a comment
@router.delete("/blog-comment/{id}", response_model = BlogPost)
def delete_comment(comment:BlogPost):
    return comment
