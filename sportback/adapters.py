from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        user_field(user, 'name', request.data.get('name', ''))
        user_field(user, 'username', request.data.get('email', ''))
        user_field(user, 'refused_newsletters', request.data.get('refused_newsletters', ''))
        user.save()
        return user
