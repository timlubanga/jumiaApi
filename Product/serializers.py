from Product.models import Product, Review, Category
from rest_framework import serializers
from Partners.serializers import CustomerSerializer


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]





class reviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["title", "description", "rating",
                  "customer", "product"]
        read_only_fields = ["customer", "product"]

    def validate(self, data):
        product = self.context.get("product", None)
        customer = self.context.get("customer", None)
        review = Review.objects.filter(
            product=product, customer=customer).exists()
        if review:
            raise serializers.ValidationError({"message":
                                               "you have already reviewed this item"})
        return data


class productSerializer(serializers.ModelSerializer):
    productreviews=reviewSerializer(read_only=True, many=True)
    averageRating=serializers.ReadOnlyField()
    class Meta:
        productcategory = serializers.ReadOnlyField()
        model = Product
        fields = ["id", "price", "name", "brand",
                  "supplier", "image", "productcategory", "productreviews", "averageRating"]
