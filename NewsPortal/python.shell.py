cd NewsPortal
python manage.py makemigrations
python manage.py shell
from django.contrib.auth.models import User
user_ivan = User.objects.create_user(username=’Ivan’)
user_sasha = User.objects.create_user(username=’Sasha’)
author_ivan = Author.objects.create(content_creator=user_ivan, rating_content=100)
author_sasha = Author.objects.create(content_creator=user_sasha, rating_content=56)
sport = Category.objects.create(type_name=’sport’)
education = Category.objects.create(type_name=’education’)
politics = Category.objects.create(type_name=’ politics’)
info = Category.objects.create(type_name=’information’)
content1 = Post.objects.create(creator=author_ivan,  type_choice=’content’,  title=’woolworth’, content_text=’открылся новый магазин’,rating=1261)
news1 = Post.objects.create(creator=author_ivan,  type_choice=’news’,  title=’iphone 26’, content_text=’добавили 12 камер и наконец-то 120 герц экран’,rating=1261)
content2 = Post.objects.create(creator=author_sasha,  type_choice=’content’,  title=’elon Musk’, content_text=’elon musk сказал, что создал электрокар для жены’,rating=12633)

Post.objects.get(id=1).post_category.add(Category.objects.get(id=2))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=2))
Post.objects.get(id=2).post_category.add(Category.objects.get(id=4))
Post.objects.get(id=3).post_category.add(Category.objects.get(id=2))

Comment.objects.create(comment_to_post=Post.objects.get(id=1), comment_to_user=Author.objects.get(id=1).content_creator, comment_text='привет круто сделано')
Comment.objects.create(comment_to_post=Post.objects.get(id=1), comment_to_user=Author.objects.get(id=1).content_creator, comment_text='хорощая статья')
Comment.objects.create(comment_to_post=Post.objects.get(id=2), comment_to_user=Author.objects.get(id=1).content_creator, comment_text='замечательная новость')
Comment.objects.create(comment_to_post=Post.objects.get(id=3), comment_to_user=Author.objects.get(id=2).content_creator, comment_text='интересно')
Post.objects.get(id=1).like()
Post.objects.get(id=1).dislike()
Post.objects.get(id=2).like()
Post.objects.get(id=2).dislike()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).dislike()
Comment.objects.get(id=3).comment_rating

a =Author.objects.get(id=1)
a.update_rating()

a1.rating_content
Author.objects.all().order_by('-rating_content')[0]

Post.objects.all().order_by('-rating')[0]

P = Post.objects.all().order_by('-rating')[0]
Comment.objects.all().filter(comment_to_post=p)
