from django.db import models
from wagtail.documents.models import AbstractDocument, Document

class CustomDocument(AbstractDocument):
    # primer dodatnega polja (po želji):
    # category = models.CharField(max_length=100, blank=True)

    # omogoči prikaz dodatnih polj v Wagtail adminu
    admin_form_fields = Document.admin_form_fields  # + ("category",)