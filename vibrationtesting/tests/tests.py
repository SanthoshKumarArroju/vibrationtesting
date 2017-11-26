import numpy as np
import vibrationtesting as vt
import numpy.testing as nt

M = np.array([[4, 0, 0],
              [0, 4, 0],
              [0, 0, 4]])
K = np.array([[8, -4, 0],
              [-4, 8, -4],
              [0, -4, 4]])
omega, Psi = vt.undamped_modes(M, K)


def test_serep():
    M = np.array([[4, 0, 0],
                  [0, 4, 0],
                  [0, 0, 4]])
    K = np.array([[8, -4, 0],
                  [-4, 8, -4],
                  [0, -4, 4]])
    retained = np.array([[1, 2]])
    Mred, Kred, T, truncated_dofs = vt.serep(M, K, retained)
    Mr_soln = np.array([[ 16.98791841, -16.19566936],
                         [-16.19566936,  24.19566936]])
    Kr_soln = np.array([[ 20.98791841, -12.98791841],
                        [-12.98791841,  10.21983253]])
    nt.assert_array_almost_equal(Mred, Mr_soln)
    nt.assert_array_almost_equal(Kred, Kr_soln)
