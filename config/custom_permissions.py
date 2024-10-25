from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class OnlyLoggedSuperUser(LoginRequiredMixin, UserPassesTestMixin):

  def test_func(self) -> bool | None:
    return self.request.user.is_superuser