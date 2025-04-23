from django.shortcuts import render
from django.views.generic import DetailView
from django.http import JsonResponse
from .models import Watch, Author

def base(request):
    watches = Watch.objects.all().order_by('-created_at')
    return render(request, 'base.html', {'carousel_items': watches})

from rest_framework import viewsets
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Watch.objects.all()
    serializer_class = ProductSerializer

def carousel_view(request):
    watches = Watch.objects.all().order_by('-created_at')
    return render(request, 'carousel_section1.html', {'carousel_items': watches})

class WatchDetailView(DetailView):
    model = Watch
    template_name = 'watch_detail.html'
    context_object_name = 'watch'
    
    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            try:
                watch = self.get_object()
                data = {
                    'title': watch.title,
                    'brand': watch.get_brand_display(),
                    'price': f"{watch.price:.2f}",
                    'material': watch.get_material_display(),
                    'water_resistance': watch.get_water_resistance_display(),
                    'movement': watch.get_movement_display(),
                    'image': watch.image.url if watch.image else '',
                    'description': watch.description
                }
                return JsonResponse(data)
            except Watch.DoesNotExist:
                return JsonResponse({'error': 'Watch not found'}, status=404)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_works'] = self.object.author.watches.exclude(pk=self.object.pk)
        context['watch_images'] = self.object.images.all()
        return context