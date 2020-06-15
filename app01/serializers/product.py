from app01 import models
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    post_date = serializers.DateField(format="%Y-%m-%d", required=False, read_only=True)
    product_type = serializers.CharField(source="get_product_type_display")
    status = serializers.CharField(source="get_status_display")
    params = serializers.SerializerMethodField()

    class Meta:
        model = models.Products
        fields = ['id', 'name', 'product_img', 'product_type', 'price', 'sale_num', 'store_num',
                  'post_date', "status", "params"]

    def get_params(self, obj):
        queryset = obj.productsparams_set.all()
        return [
            {
                'meta_key': row.meta_key,
                'meta_value': row.meta_value,
            } for row in queryset]

class ProductDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name")
    product_img = serializers.CharField(source="product.product_img")
    price = serializers.CharField(source="product.price")
    sale_num = serializers.CharField(source="product.sale_num")
    store_num = serializers.CharField(source="product.store_num")
    post_date = serializers.CharField(source="product.post_date")
    params = serializers.SerializerMethodField()
    product_type = serializers.CharField(source="product.get_product_type_display")
    status = serializers.CharField(source="product.get_status_display")

    class Meta:
        model = models.ProductsDetail
        fields = ['id', 'name', 'product_img', 'product_type', 'price', 'sale_num', 'store_num',
                  'post_date', "status", "params", "content"]

    def get_params(self, obj):
        queryset = obj.product.productsparams_set.all()
        return [
            {
                'meta_key': row.meta_key,
                'meta_value': row.meta_value,
            } for row in queryset]