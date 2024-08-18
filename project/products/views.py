from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductsListView(APIView):

    @swagger_auto_schema(
        operation_description="Получить список всех продуктов",
        responses={
            status.HTTP_200_OK: ProductSerializer(many=True)
        }
    )
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
