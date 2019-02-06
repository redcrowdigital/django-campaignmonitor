from createsend import CreateSend, Client as CSClient, List as CSList
from django.core.management.base import BaseCommand, CommandError

from ... import settings
from ...models.lists import List
from ...models.subscribers import Subscriber, STATE_ACTIVE


class Command(BaseCommand):
    help = 'Get the current subscriber lists from CampaignMonitor'
    
    def handle(self, **options):
        client = CSClient(auth=settings.CREDENTIALS, client_id=settings.CLIENT_ID)
        lists = client.lists()
        for data in lists:
            # get or create the list
            list_obj, created = List.objects.get_or_create(
                cm_id=data.ListID,
                title=data.Name,
            )
            cs_list = CSList(auth=settings.CREDENTIALS, list_id=data.ListID)

            # get all the active subscribers in this list
            for active_sub in cs_list.active().Results:
                subscriber, created = Subscriber.objects.get_or_create(
                    list=list_obj,
                    email_address=active_sub.EmailAddress,
                    defaults={'state': STATE_ACTIVE}
                )
                subscriber.name = active_sub.Name
                subscriber.date = active_sub.Date
                subscriber.state = STATE_ACTIVE
                subscriber.save()
