"""Posts Tests"""
from django.test import TestCase
from posts.models import Post, Comment
from users.models import Profile, User, Contact
import tempfile

# Create your tests here.


class TestComments(TestCase):
	
	@classmethod
	def setUpTestData(cls):
		""" 
		Creates 2 users and 2 profiles.
		@classmethod allows the creation of initial and persisting data at the class level
		"""
		cls.user_1 = User.objects.create_user(username='Carlanga', password='passwordforuser1')
		cls.user_2 = User.objects.create_user(username='Carlango', password='passwordforuser2')
		cls.profile_1= Profile.objects.create(user=cls.user_1)
		cls.profile_2= Profile.objects.create(user=cls.user_2)
  
	def test_contact_system(self):
		profile_1 = self.profile_1
		profile_2= self.profile_2
		Contact.objects.create(profile=profile_1)
		Contact.objects.create(profile= profile_2)
		Contact.follow(profile= profile_1, another_profile= profile_2)
		self.assertEqual(1, profile_1.contact.following_count())
		print(f" Profile {profile_1} follows {profile_1.contact.following_count()} profiles")
		Contact.unfollow(profile_1, profile_2)
		self.assertEqual(0, profile_1.contact.following_count())
	
	def test_create_post(self):
		user_1= self.user_1
		profile_1= self.profile_1

		post_1= Post.objects.create(
			user=user_1, 
			profile=profile_1, 
			photo= tempfile.NamedTemporaryFile(suffix=".jpg").name	
			)
	
	def test_posts_likes_and_likes_removal(self):
		user_1 = self.user_1
		profile_1 = self.profile_1
		user_2 = self.user_2
		profile_2= self.profile_2
		post_1= Post.objects.create(
			user=user_1, 
			profile=profile_1, 
			photo= tempfile.NamedTemporaryFile(suffix=".jpg").name	
			)
		post_1.likes.add(user_1)
		post_1.likes.add(user_2)
		self.assertEqual(2, post_1.likes_count())
		post_1.likes.remove(user_1)
		post_1.likes.remove(user_2)
		self.assertEqual(0, post_1.likes_count())
  
	def test_comments_creation(self):
		user_1= self.user_1
		profile_1 = self.profile_1
		profile_2= self.profile_2
		user_2= self.user_2
		post_1= Post.objects.create(
			user=user_1, 
			profile=profile_1, 
			photo= tempfile.NamedTemporaryFile(suffix=".jpg").name	
			)
		comment_1 = Comment.objects.create(
			post = post_1,
			user = user_1,
			profile = profile_1,
			text = 'KDMSLDMAS"DKMASDLSM DLSM DKMDSAKDNASDNAJDNASKDMASKJDNAD Mdldmsakdmaslkdas dasmdlasmdkasm',
			)
	
	def test_comments_likes_and_likes_removal(self):
		user_1= self.user_1
		profile_1 = self.profile_1
		profile_2= self.profile_2
		user_2= self.user_2
		post_1= Post.objects.create(
			user=user_1, 
			profile=profile_1, 
			photo= tempfile.NamedTemporaryFile(suffix=".jpg").name	
			)
		comment_1 = Comment.objects.create(
			post = post_1,
			user = user_1,
			profile = profile_1,
			text = 'KDMSLDMAS"DKMASDLSM DLSM DKMDSAKDNASDNAJDNASKDMASKJDNAD Mdldmsakdmaslkdas dasmdlasmdkasm',
			)
		comment_1.likes.add(user_1)
		comment_1.likes.add(user_2)
		self.assertEqual(2, comment_1.likes.count())
		comment_1 = Comment.objects.get(pk=1)
		comment_1.likes.remove(user_1)	
		comment_1.likes.remove(user_2)
		self.assertEqual(0, comment_1.likes.count())
		self.assertEqual(1, Comment.objects.filter(post=post_1.pk).count())
		self.assertEqual(1, Comment.comments_count(post_1))