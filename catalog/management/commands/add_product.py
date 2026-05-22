from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Сбрасывает базу данных и заполняет из фикстур'

    def handle(self, *args, **kwargs):

        # Удаление старой базы
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Заполнение из фикстур
        call_command('loaddata', 'category_fixture.json')
        call_command('loaddata', 'product_fixture.json')

        self.stdout.write(self.style.SUCCESS('База успешно пересоздана из фикстур!'))
