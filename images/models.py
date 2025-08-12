from django.db import models
from wagtail.images.models import AbstractImage, AbstractRendition, Image

class CustomImage(AbstractImage):
    # Primer dodatnega polja (po želji):
    # source = models.CharField(max_length=255, blank=True)

    # Če dodaš polja, jih vključi v Wagtail admin:
    admin_form_fields = Image.admin_form_fields  # + ("source",)

class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        "images.CustomImage",
        on_delete=models.CASCADE,
        related_name="renditions",
    )
    file = models.ImageField(
        upload_to="images/renditions/",
        width_field="width",
        height_field="height",
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)