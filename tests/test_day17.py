import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from Day17_Chronospatial_Computer import Processor


def test_Processor_example1():

    processor = Processor(0, 0, 9)
    processor.run([2, 6])
    assert processor.register_b == 1


def test_Processor_example2():

    processor = Processor(10, 0, 0)
    assert processor.run([5, 0, 5, 1, 5, 4]) == "0,1,2"


def test_Processor_example3():

    processor = Processor(2024, 0, 0)
    result = processor.run([0, 1, 5, 4, 3, 0])
    assert (result, processor.register_a) == ("4,2,5,6,7,7,7,7,3,1,0", 0)


def test_Processor_example4():

    processor = Processor(0, 29, 0)
    processor.run([1, 7])
    assert processor.register_b == 26


def test_Processor_example5():

    processor = Processor(0, 2024, 43690)
    processor.run([4, 0])
    assert processor.register_b == 44354


def test_Processor_example6():

    processor = Processor(729, 0, 0)
    assert processor.run([0, 1, 5, 4, 3, 0]) == "4,6,3,5,6,3,5,2,1,0"
