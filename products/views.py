"""takes a Web request and returns a Web response."""
import logging

from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Product, Category

logger = logging.getLogger(__name__)


class ProductDetailView(DetailView):
    """Display an individual product.

    **Context**
    ''product''
        An instance of :model:`products.Product`.

    **Template:**
        'products/detail.html'
    """
    logger.info('Product detail', exc_info=True, extra={
        # Optionally pass a request and we'll grab any information we can
        # 'request': request,
    })
    model = Product
    context_object_name = 'product'
    template_name = 'products/detail.html'


class SubstitutesListView(ListView):
    """Display list substitutes from a product.

    **Context**
        'substitutes', get by Product.objects.get_substitutes,
        'selected_product', an instance of :model:`products.Product`.
    **Template:**
        'products/substitutes.html'
    """
    template_name = 'products/substitutes.html'
    context_object_name = 'substitutes'

    def get_queryset(self):
        """return substitutes from a product."""
        product = Product.objects.get(pk=self.kwargs['pk'])
        substitutes = Product.objects.get_substitutes(product)
        self.paginate_by = 6

        return substitutes

    def get_context_data(self, **kwargs):
        """add selected_product in global context."""
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        context['selected_product'] = product

        return context


class SearchListView(ListView):
    """displays the list of products corresponding to the search.

    **Context**
        'products', get by Product.objects.search(),
        'search', term.
    **Template:**
        'products/search.html'
    """
    template_name = 'products/search.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        """return products from search term."""
        query = self.request.GET['search']
        products = Product.objects.search(query)

        return products

    def get_context_data(self, **kwargs):
        """add search in global context."""
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET['search']

        return context


# for v2
class CategoryListView(ListView):
    """Display list products from a category.

    **Context**
        'products', get by Product.objects.get_substitutes,
        'category', an instance of :model:'products.Category'.
    **Template:**
        'products/search.html'
    """
    template_name = 'products/search.html'
    context_object_name = 'products'

    def get_queryset(self):
        """return substitutes from a product."""
        category = Category.objects.get(pk=self.kwargs['pk'])
        print("Catégorie:", category)
        products = category.product_set.all()
        self.paginate_by = 6

        return products

    def get_context_data(self, **kwargs):
        """add selected_product in global context."""
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])

        return context


# for v2
class CategoriesListView(ListView):
    """Display list categories.
        **Context**
        'categories', get by Categories.all,
    **Template:**
        'products/categories.html'
    """
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    paginate_by = 6


class FavoritesListView(ListView):
    """Display list favorites for a logged user.

    **Context**
        'favorites', get by Product.objects.filter,
    **Template:**
        'products/favorites.html'
    """
    template_name = 'products/favorites.html'
    context_object_name = 'favorites'
    paginate_by = 6

    def get_queryset(self):
        """return favorite products for a user."""
        favorites = Product.objects.filter(
            favorites=self.request.user
        ).order_by('-products_favorite.date_favorite')
        return favorites


def admin_favorite(request, pk, action='add'):
    """Save substitute in favorites."""
    logger.info('favorites', exc_info=True, extra={
        # Optionally pass a request and we'll grab any information we can
        'request': request,
        'action': action,
    })
    if request.user.is_authenticated:

        substitute = get_object_or_404(
            Product,
            pk=pk
        )

        if action == 'add':
            substitute.favorites.add(request.user)
        elif action == 'del':
            substitute.favorites.remove(request.user)

        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('sign_up')
