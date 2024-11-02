import os
import random
import django
from dateutil import tz
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE","chat_app.settings")
django.setup()

from main.models import Talk,User

fakegen = Faker(["ja_JP"])


def create_users(n):

    users = [
        User(username=fakegen.user.name(),email=fakegen.ascii_safe_email())
        for _ in range(n)
    ]

    User.objects.bulk_create(users, ignore_conflicts=True)

    my_id = User.objects.get(username="<自分のユーザ名>").id

    user_ids = User.objects.exclude(id=my_id).value_list("id",flat=True)

    talks = []
    for _ in range(len(user_ids)):
        sent_talk = Talk(
            sender_id=my_id,
            receiver_id=random.choice(user_ids),
            message=fakegen.text(),
        )
        received_talk = Talk(
            sender_id=random.choice(user_ids),
            receiver_id=my_id,
            message=fakegen.text(),
        )
        talks.extend([sent_talk,received_talk])
    Talk.objects.bulk_create(users, ignore_conflict=True)