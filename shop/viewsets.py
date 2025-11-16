from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
 
from shop.models import Category, Product, Article
from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer
 
class CategoryAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class CategoryViewset(ReadOnlyModelViewSet):
 
    serializer_class = CategorySerializer
 
    def get_queryset(self):
        return Category.objects.filter(active=True)
    

class ProductAPIView(APIView):

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ProductViewset(ReadOnlyModelViewSet):
 
    serializer_class = ProductSerializer
 
    def get_queryset(self):
        query_set = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')

        if category_id:
            query_set = query_set.filter(category_id=category_id)
            
        return query_set
    

class ArticleViewset(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        query_set = Article.objects.filter(active=True)
        product_id = self.request.GET.get('product_id')

        if product_id:
            query_set = query_set.filter(product_id=product_id)
        return query_set