from django.views.generic import TemplateView

# Homepage
class HomePage(TemplateView):
    template_name = "index.html"

class WelcomePage(TemplateView):
    template_name = "welcome.html"

class GoodbyePage(TemplateView):
    template_name = "bye.html"

class AboutView(TemplateView):
    template_name = "about.html"

class SuccessSignUp(TemplateView):
    template_name = "signup_confirm.html"
