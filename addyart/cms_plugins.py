from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Catalog, Category, Product

@plugin_pool.register_plugin
class HelloPlugin(CMSPluginBase):
    model = Catalog
    name = _("Catalog")
    render_template = "catalog.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(HelloPlugin, self).render(context, instance, placeholder)
        products = Product.objects.all()
        categories = Category.objects.all()
        context.update({
            'products': products,
            'categories': categories,
        })
        return context
