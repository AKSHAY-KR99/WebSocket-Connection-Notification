# In admin case
admin_objects = models.User.objects.filter(user_role=settings.ADMIN['number_value'])
for admin_object in admin_objects:
	push_notification(admin_object.slug_value, notification_serializer.data)


# In other user case
push_notification(user_object.slug_value, notification_serializer.data)


# Function for sending notification to the user

# push_notification(slug_value_of_user, notification_data)
