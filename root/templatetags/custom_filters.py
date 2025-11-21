import jdatetime
from django import template
from django.utils import timezone

register = template.Library()

@register.filter("mul")
def mul(value, arg):
    return int(value) * int(arg)


def to_persian_numbers(value):
    numbers = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }
    return str(value).translate(str.maketrans(numbers))


# Helper: Month names list
PERSIAN_MONTHS = [
    "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
]


@register.filter(name='jalali_human')
def jalali_human(value):
    if not value:
        return ""

    # 1. Ensure timezone awareness
    if timezone.is_naive(value):
        value = timezone.make_aware(value, timezone.get_current_timezone())

    now = timezone.now()
    diff = now - value

    seconds = diff.total_seconds()
    minutes = int(seconds // 60)
    hours = int(minutes // 60)
    days = diff.days

    # 2. Logic for "Time Ago"
    if seconds < 60:
        return "لحظاتی پیش"

    if minutes < 60:
        return to_persian_numbers(f"{minutes} دقیقه پیش")

    if hours < 24:
        return to_persian_numbers(f"{hours} ساعت پیش")

    if days == 1:
        return "دیروز"

    # 3. Logic for Full Date (The Fix)

    # Convert to Jalali
    j_date = jdatetime.date.fromgregorian(date=value)

    # Get Persian Month Name from our list (index starts at 0, month starts at 1)
    month_name = PERSIAN_MONTHS[j_date.month - 1]

    # Manually build the string: "Day Month Year"
    full_date_str = f"{j_date.day} {month_name} {j_date.year}"

    return to_persian_numbers(full_date_str)