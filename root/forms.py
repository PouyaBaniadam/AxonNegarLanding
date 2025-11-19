from django import forms

from root.models import ContactMessage

def convert_persian_digits_to_english(text):
    if text is None:
        return None

    persian_to_english_map = {
        '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4',
        '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9',
        '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
        '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
    }

    translation_table = str.maketrans(persian_to_english_map)
    return text.translate(translation_table)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'website', 'message']

        labels = {
            'name': 'نام',
            'email': 'ایمیل',
            'phone': 'تلفن',
            'website': 'وب‌سایت',
            'message': 'پیام شما',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام*'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل*'}),
            'phone': forms.TextInput(attrs={'placeholder': 'تلفن*', 'type': 'tel', 'dir': 'rtl'}),
            'website': forms.URLInput(attrs={'placeholder': 'وب‌سایت'}),
            'message': forms.Textarea(attrs={'placeholder': 'پیام شما*', 'rows': 4}),
        }

        error_messages = {
            'name': {
                'required': 'لطفاً نام خود را وارد کنید.',
            },
            'email': {
                'required': 'لطفاً ایمیل خود را وارد کنید.',
                'invalid': 'یک آدرس ایمیل معتبر وارد کنید.',
            },
            'phone': {
                'required': 'لطفاً شماره تلفن خود را وارد کنید.',
            },
            'message': {
                'required': 'لطفاً پیام خود را بنویسید.',
            },
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone:
            return phone

        phone = convert_persian_digits_to_english(phone)

        if not phone.isdigit():
            raise forms.ValidationError("شماره تلفن باید فقط شامل عدد باشد.")

        if len(phone) != 11:
            raise forms.ValidationError("شماره تلفن باید ۱۱ رقم باشد (مثال: ۰۹۱۲۳۴۵۶۷۸۹).")

        if not phone.startswith('09'):
            raise forms.ValidationError("شماره تلفن باید با ۰۹ شروع شود.")

        return phone