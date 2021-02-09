from django.shortcuts import render

# Create your views here.
def pricing_view(request):
    template_name = "pricing.html"
    return render(request, template_name)