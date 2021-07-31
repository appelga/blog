from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):        
        base_user = User.objects.create_user(
                'USUARIO PARA TESTES UNITARIOS',
                email=None,
                password=None
            )       
        Post.objects.create(
            author = base_user,
            title = 'post para teste unitario',
            subtitle = 'estamos fazendo testes unitarios',
            text = 'testes unitarios sao legais'
        )

    def test_post_can_be_published(self):
        post = Post.objects.get(title='post para teste unitario')
        self.assertEqual(post.published_date, None)
        post.publish()
        self.assertNotEqual(post.published_date, None)