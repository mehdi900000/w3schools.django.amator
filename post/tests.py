from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse
class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user=get_user_model().objects.create_user(
            username="testuser",email="test@email.com",password="secret"
        )
        cls.post=Post.objects.create(subject="fruit",text="apple",author=cls.user,body="lorem test body")

    def test_post_model(self):
        self.assertEqual(self.post.subject,"fruit")
        self.assertEqual(self.post.text,"apple")
        self.assertEqual(self.post.author.username,"testuser")
        self.assertEqual(self.post.body,"lorem test body")
        self.assertEqual(str(self.post),"fruit")
        self.assertEqual(self.post.get_absolute_url(),"/post/1/")

    def test_url_exist_at_correct_location_listview(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_url_exist_at_correct_location_detailview(self):
        response=self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
    def test_post_listview (self):
        response=self.client.get(reverse('home'))    
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"fruit")
        self.assertTemplateUsed(response,"home.html")
    def test_post_detailview (self):
        response=self.client.get(reverse('detail', kwargs={"pk":self.post.pk}))
        no_response=self.client.get('/post/100000/')
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'fruit')
        self.assertTemplateUsed(response, 'post/post_detail.html')
    def test_post_creatview (self):
        response=self.client.post(reverse('create'),{'subject':'new subject',
        'text':'new text',
        'author':self.user.id,
        'body':'new body',})    
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().subject, 'new subject')
        self.assertEqual(Post.objects.last().text,'new text')




