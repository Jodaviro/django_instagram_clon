"""Posts Tests"""

from django.test import TestCase
from posts.models import Post
from users.models import Profile, User, Contact
import tempfile

# Create your tests here.


class TestPost(TestCase):
	
	def setUp(self):
		""" Creates 2 users and 2 profiles"""

		user_1 = User.objects.create_user(username='Carlanga', password='passwordforuser1')
		user_2 = User.objects.create_user(username='Carlango', password='passwordforuser2')
		profile_1= Profile.objects.create(user=user_1)
		profile_2= Profile.objects.create(user=user_2)

	
	def test_create_post(self):
		user_1= User.objects.get(username='Carlanga')
		profile_1= Profile.objects.get(pk=user_1.pk)

		post1= Post.objects.create(
			user=user_1, 
			profile=profile_1, 
			photo= tempfile.NamedTemporaryFile(suffix=".jpg").name	
			)
		
		post1.save()
  
	def test_contact_system(self):
		profile_1 = Profile.objects.get(pk=1)
		profile_2= Profile.objects.get(pk=2)
		Contact.objects.create(profile=profile_1)
		Contact.objects.create(profile= profile_2)
		Contact.follow(profile= profile_1, another_profile= profile_2)
		#test following
		self.assertEqual(1, profile_1.contact.following_count())
		print(f" Profile {profile_1} follows {profile_1.contact.following_count()} profiles")
		#test followers
		self.assertEqual(1, profile_2.followers.count())
		print(f" Profile {profile_2} has {profile_2.followers.count()} followers")
		for profile in profile_2.followers.all():
			print (profile.profile)
		Contact.unfollow(profile_1, profile_2)
		self.assertEqual(0, profile_1.contact.following_count())
	
  
	def test_delete_post(self):
		posts = Post.objects.all()
		for post in posts:
			post.delete()
		
