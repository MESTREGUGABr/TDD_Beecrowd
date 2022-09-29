import unittest

from beecrowd1117 import nota_correta

class verificacao_notas(unittest.TestCase):
    def verificacao(self):
        self.assertEqual(nota_correta(8,9),8,5)
        self.assertEqual(nota_correta(8,7),7,5)
        self.assertEqual(nota_correta(5,9),7)
        self.assertEqual(nota_correta(3,2),2,5)
        self.assertEqual(nota_correta(8,-1),"alguma nota invalida")
        
if __name__ == '__main__':
    unittest.main()