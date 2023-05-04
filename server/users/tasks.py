from celery import shared_task

@shared_task
def send_email_confirmation(user_id,uuid):
    return {f'127.0.0.1/verification/{user_id}/{uuid}'}

# разгружаем ну очень тяжелый запрос
@shared_task
def account_activate(user_id):
    from users.models.users import User

    user = User.objects.get(id=user_id)
    user.is_active=True
    user.save()