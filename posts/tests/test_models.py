from django.test import TestCase
from django.contrib.auth.models import User

from posts.models import Post, Tag, Author


class TestAuthorModel(TestCase):
    
    def test_string_representation(self):
        user = User.objects.create_user(username='Inno', password='90reoifhdskj97e')
        author = Author.objects.create(user=user)

        self.assertEquals(str(author), 'Inno')

    


class TestTagModel(TestCase):

    def test_tag_string_representation(self):
        tag = Tag.objects.create(name='Django')

        self.assertEqual(str(tag), 'Django')


class TestPostsSaveRetrieve(TestCase):

    def test_can_save_and_retrieve_posts(self):
        post1 = Post(
            title='First Post',
            content='Hello ifrst psfodh'
        )
        post1.save()
        post2 = Post(
            title='second post',
            content='Hleo ofdsago fdsoah odsf ha'
        )
        post2.save()

        saved_posts = Post.objects.all()

        self.assertEquals(len(saved_posts), 2)

        first_post = Post.objects.get(id=1)
        second_post = Post.objects.get(id=2)
        
        self.assertEquals(first_post.title, 'First Post')
        self.assertEquals(second_post.title, 'second post')


class TestPostsModels(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Awesome Post',
            content='Hleo ofdsago fdsoah odsf ha'
        )

    
    def test_can_update_post(self):
        initial_content = self.post.content
        self.post.content = 'Hello, this is updated post'
        self.post.save()

        current_content = self.post.content

        self.assertNotEquals(current_content, initial_content)


    def test_post_string_representation(self):
        self.assertEquals('Awesome Post', str(self.post.title))


    def test_get_absolute_url(self):
        self.assertEquals(self.post.get_absolute_url(), '/blog/awesome-post/')

    
    def test_get_update_url(self):
        self.assertEqual(self.post.get_update_url(), '/blog/awesome-post/update/')


    def test_get_delete_url(self):
        self.assertEqual(self.post.get_delete_url(), '/blog/awesome-post/delete/')


    def test_can_delete_post(self):
        self.post.delete()
        posts = Post.objects.all()

        self.assertEquals(len(posts), 0)




