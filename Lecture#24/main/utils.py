from django.utils import timezone


def is_coupon_expired(coupon):
    current_datetime = timezone.now()
    return coupon.valid_to < current_datetime
