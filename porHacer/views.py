from porHacer.models import *
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def marcar_como_hecho(request, pk):
    item = Item.objects.get(pk=pk)
    item.hecho = True
    item.save()
    return HttpResponseRedirect(reverse("admin:porHacer_item_changelist"))
