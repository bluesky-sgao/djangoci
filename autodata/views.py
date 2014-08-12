# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from autodata.models import AutoData

def autodata(request):
    auto_datas = AutoData.objects.all()
    t = loader.get_template("auto_data.html")
    c = Context({'auto_datas':auto_datas})
    return HttpResponse(t.render(c))
