from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
    ("Andaman & Nicobar Islands", "Andaman & Nicobar Islands"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chandigarh", "Chandigarh"),
    ("chhattisgarh", "Chhattisgarh"),
    ("Dadra & Nagar Haveli", "Dadra & Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu & Kashmir", "Jammu & Kashmir"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Lakshadweep", "Lakshadweep"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Puducherry", "Puducherry"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttarakhand", "Uttarakhand"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("West Bengal", "West Bengal"),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def _str_(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ("M", "Mobile"),
    ("L", "Laptop"),
    ("TW", "Top Wear"),
    ("BW", "Bottom Wear"),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to="productimg")

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_COICES = (
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("On the Way", "On the Way"),
    ("Delivered", "Delivered"),
    ("Cancel", "Cancel"),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=50, choices=STATUS_COICES, default="Pending")
    ordered_date = models.DateTimeField(auto_now_add=True)