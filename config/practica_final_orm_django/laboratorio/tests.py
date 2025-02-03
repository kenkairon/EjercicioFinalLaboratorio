from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre="LabTest", ciudad="CiudadTest", pais="PaisTest")

    def test_reverse_url_laboratorio(self):
        """ Verifica que reverse() funcione correctamente con la URL de detalle """
        url = reverse('laboratorio:laboratorio', args=[self.laboratorio.id])  # Usando app_name
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "laboratorio/laboratorio.html")
        self.assertContains(response, "LabTest")  # Ajusta según el contenido esperado


