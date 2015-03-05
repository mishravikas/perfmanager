from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
import hashlib

@receiver([post_save], sender=User)
def init_newuser_data(sender, instance, created, **kwargs):
	'''
	Whenever a new user is created, we need to create
	UserProfile with default values
	'''
	if created:
		UserProfile.objects.create(user=instance)

def profile(request):
	if request.user.is_authenticated():
		current_profile = UserProfile.objects.get(user=request.user)
		img_url = 'http://www.gravatar.com/avatar/' + hashlib.md5(request.user.email).hexdigest()

		if request.method == 'GET':
			form = UserProfileForm(instance=current_profile)
		else:
			# A POST request: Handle Form Upload
			# Bind data from request.POST into a PostForm
			form = UserProfileForm(request.POST)
			# If data is valid, proceeds to create a new post and redirect the user
			if form.is_valid():
				print "FORM IS VALID"
				current_profile.first_name = form.cleaned_data['first_name']
				current_profile.last_name = form.cleaned_data['last_name']
				current_profile.irc_nick = form.cleaned_data['irc_nick']
				current_profile.receive_notifications = form.cleaned_data['receive_notifications']
				current_profile.save(update_fields=['first_name', 'last_name', 'irc_nick', 'receive_notifications'])
				return HttpResponseRedirect('/accounts/profile/')
		return render(request, 'accounts/profile.html', {'img_url': img_url, 'form': form})
	return HttpResponse("404 Not authorized")
