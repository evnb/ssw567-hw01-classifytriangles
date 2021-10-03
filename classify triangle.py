#!/usr/bin/env python3

import pytest

def classify_triangle(a, b, c):
	#check input
	for x in (a,b,c):
		if not isinstance(x, (int, float)):
			raise TypeError('all sides must be int or float')
		if x<=0:
			raise ValueError('all sides must have length greater than zero')
	
	if a + b < c or a + c < b or b + c < a:
		return ["invalid triangle"]
	
	#actual classification
	classifications = []
	if a == b and b == c:
		classifications.append("equilateral")
	elif a == b or b == c or a == c:
		classifications.append("isosceles")
	else:
		classifications.append("scalene")
	
	if ("equilateral" not in classifications) and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2):
		classifications.append("right")
	
	return classifications

def test_classify_triangles():
	assert classify_triangle(1, 1, 1) == ["equilateral"]
	assert classify_triangle(.7, 0.7, 7/10) == ["equilateral"]
	
	assert classify_triangle(1, 2, 1) == ["isosceles"]
	assert classify_triangle(2, 2, 2.1) == ["isosceles"]
	assert classify_triangle(27.001, 27.002, 27.002) == ["isosceles"]
	
	#How to test irrational numbers with a tolerance?
	#assert classify_triangle(1, 1, 2**0.5) == ["isosceles", "right"]
	
	assert classify_triangle(5, 7, 12) == ["scalene"]
	assert classify_triangle(5.5, 7, 12) == ["scalene"]
	assert classify_triangle(5.1, 7.1, 12.1) == ["scalene"]
	
	assert classify_triangle(3,4,5) == ["scalene", "right"]
	assert classify_triangle(4,7.5,8.5) == ["scalene", "right"]
	assert classify_triangle(.375,0.5,.625) == ["scalene", "right"]
	
	assert classify_triangle(7,1,5) == ["invalid triangle"]
	assert classify_triangle(1,1,5) == ["invalid triangle"]
		
	with pytest.raises(TypeError):
		classify_triangle("10", 9, 2)
	with pytest.raises(TypeError):
		classify_triangle(3, 4, [5])
		
	with pytest.raises(ValueError):
		classify_triangle(3, -4, 5)
	with pytest.raises(ValueError):
		classify_triangle(-1, -1, 1)
	with pytest.raises(ValueError):
		classify_triangle(-1, -1, -1)
	with pytest.raises(ValueError):
		classify_triangle(-1, -1, -1)
	with pytest.raises(ValueError):
		classify_triangle(7, 0, 5)
		