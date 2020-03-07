from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Catalog, Category, Product, Detail

@plugin_pool.register_plugin
class CatalogPlugin(CMSPluginBase):
    model = Catalog
    name = _("Catalog")
    render_template = "catalog.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(CatalogPlugin, self).render(context, instance, placeholder)
        products = Product.objects.all()
        categories = Category.objects.all()
        context.update({
            'products': products,
            'categories': categories,
        })
        return context

@plugin_pool.register_plugin
class DetailPlugin(CMSPluginBase):
    model = Detail
    name = _("Detail")
    render_template = "detail_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(DetailPlugin, self).render(context, instance, placeholder)
        slug = context['request'].GET.get('slug')
        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            return context
        context.update({
            'product': product,
        })
        return context
