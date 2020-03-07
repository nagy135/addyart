from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class CatalogApphook(CMSApp):
    app_name = "catalog"  # must match the application namespace
    name = "Catalog Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["catalog.urls"]
