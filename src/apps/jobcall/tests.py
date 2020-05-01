
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import JobCall,AnonymousInscription
from apps.accounts.models import AspiringUser as User
User = get_user_model()

# pruebas automatizadas
class DisableCategoryTestCase(TestCase):
    fixtures = ['test_fixtures/user_apply_jobcall.json']

    def setUp(self):
        # Usuario
        # author = User.objects.create_user(username='testuser',
        #   email='user@test.com', password='abc123')
        # Categoría
        # self.category = Category.objects.create(name='Test category',
        #   description='Test category description')
        # posts
        # self.category.post_set.create(title='Test post 1',
        #   text='Test post content', author=author)
        # self.category.post_set.create(title='Test post 2',
        #   text='Test post content', author=author)
        self.closed_jobcall = JobCall.objects.get(pk=2)
        self.open_jobcall =  JobCall.objects.first()
        self.aspirant = User.objects.first()
        return super().setUp()
    def test_user_apply_jobcall_signal(self):
        try:
            self.closed_jobcall.aspirant.add(self.aspirant)
        except:
            pass
        try:
            self.open_jobcall.aspirant.add(self.aspirant)
        except:
            pass
        self.assertNotIn(self.aspirant,self.closed_jobcall.aspirants.all())
        self.assertNotIn(self.aspirant,self.open_jobcall.aspirants.all())

    def test_anonymouns_inscription_jobcall_signal(self):
        inscription = None
        try:
            inscription =  AnonymousInscription.objects.create(
                full_name="anonymouns inscripcion",
                jobcall=self.closed_jobcall,
                curriculum="static/jobcall/curriculim.pdf")
        except:
            pass
        try:
            inscription =  AnonymousInscription.objects.create(
                full_name="anonymouns inscripcion",
                jobcall=self.open_jobcall,
                curriculum="static/jobcall/curriculim.pdf")
        except:
            pass
        self.assertNotIn(inscription,self.closed_jobcall.anonymousinscription_set.all())
        self.assertIn(inscription,self.open_jobcall.anonymousinscription_set.all())

