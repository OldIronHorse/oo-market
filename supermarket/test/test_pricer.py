from unittest import TestCase
from supermarket import Pricer, Item

class TestPricer(TestCase):
  def setUp(self):
    self.pricer = Pricer({'soap':150,
                          'shampoo':200,
                          'conditioner':190})

  def test_empty_basket(self):
    self.assertEqual([], self.pricer.price([]))
    
  def test_valid_basket(self):
    self.assertEqual([Item('soap', 150),
                      Item('shampoo', 200),
                      Item('shampoo', 200),
                      Item('soap', 150),
                      Item('conditioner', 190),
                      Item('shampoo', 200)],
                     self.pricer.price(['soap',
                                        'shampoo',
                                        'shampoo',
                                        'soap',
                                        'conditioner',
                                        'shampoo']))
    
  def test_unknown_item_basket(self):
    with self.assertRaises(KeyError):
       self.pricer.price(['soap',
                          'shampoo',
                          'shampoo',
                          'unobtainium',
                          'soap',
                          'conditioner',
                          'shampoo'])
    
