import unittest

from beecrowd1132 import multiplo

class verificacao_notas(unittest.TestCase):
    def verificacao(self):
       self.assertEqual(multiplo(13),0)
       self.assertEqual(multiplo(14),'Não é multiplo')
       self.assertEqual(multiplo(26),0)
       self.assertEqual(multiplo(39),0)
       self.assertEqual(multiplo(52),0)

        
if __name__ == '__main__':
    unittest.main()