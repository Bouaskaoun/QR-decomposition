import Algorithme


matrix = Algorithme.loadMatrix()
if not Algorithme.isSymmetric(matrix):
	raise ValueError("Not a symmetric matrix.")
Q, R = Algorithme.QRdecompose(matrix)
eVectors, eValues = Algorithme.computeVV(Q, R)
Algorithme.outputResults(eVectors, eValues, Q, R)