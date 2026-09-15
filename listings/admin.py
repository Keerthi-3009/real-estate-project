from django.contrib import admin
from .models import (
    Property,
    PropertyType,
    PropertyImage,
    Amenity,
    Inquiry,
    Favorite,
    SellerSubmission,
    SellerSubmissionImage,
)
from .models import BuyerInquiry


admin.site.register(Property)
admin.site.register(PropertyType)
admin.site.register(PropertyImage)
admin.site.register(Amenity)
admin.site.register(Inquiry)
admin.site.register(Favorite)
admin.site.register(SellerSubmission)
admin.site.register(SellerSubmissionImage)
admin.site.register(BuyerInquiry)