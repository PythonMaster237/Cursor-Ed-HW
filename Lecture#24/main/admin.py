from django.contrib import admin
from .models import MenuItem, SliderItem, OrderItems, Order, Coupon

admin.site.register(MenuItem)
admin.site.register(SliderItem)


class OrderAdmin(admin.ModelAdmin):
    list_display = fields = ['id', 'first_name', "last_name", "address", "email"]

    def queryset(self,request):
        qs = super(Order, self).queryset(request)
        return qs.all()


admin.site.register(Order, OrderAdmin)


class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'discount_percent', 'valid_from', 'valid_to', 'used')
    ordering = ('valid_from', 'valid_to', 'used', 'discount_percent',)

admin.site.register(Coupon, CouponAdmin)
