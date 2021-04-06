{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Jacobi.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNhx5Kb7yhXPjf4fqg1cclF",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nataliapazin/Met_Num_2021/blob/main/Jacobi.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uXlV0PdJU1i0"
      },
      "source": [
        "import numpy as np\n",
        "import numpy.linalg as nl\n",
        "\n",
        "def jacobi(A,f,x,maxIter = 100, tol = 1.0e-4):\n",
        "    # inputs:\n",
        "    # A is a nxn matrix\n",
        "    # f is a right-hand-side vector of length n\n",
        "    # x is initial guess at the solution to A x = f\n",
        "    # maxIter (optional) is maximum iterations\n",
        "    # tol (optional) is desired accuracy in terms\n",
        "    # of the L2-norm of the residual (= f - Ax)\n",
        "    n = f.size\n",
        "    # Begin by checking for compatible sizes\n",
        "    if (A.shape[0] != n or A.shape[1] != n):\n",
        "        print(\"Error! Incompatible sizes.\")\n",
        "        return f\n",
        "    # Loop to iterate until we converge to solution\n",
        "    # or we reach the maximum number of iterations\n",
        "    xnew = np.copy(x)\n",
        "    for iter in range(maxIter):\n",
        "        # calculate residual\n",
        "        res = f - np.dot(A,x)\n",
        "        # check L2-norm for convergence\n",
        "        if (nl.norm(res,2) < tol):\n",
        "            #print(\"Converged after\", iter,\"iterations \")\n",
        "            return x, iter\n",
        "        # start of Jacobi iteration\n",
        "        for i in range(n):\n",
        "            sum=0.0\n",
        "            for j in range(n):\n",
        "                if(i != j):\n",
        "                    sum += A[i,j]*x[j]\n",
        "            xnew[i] = (f[i] - sum)/A[i,i]\n",
        "        x = np.copy(xnew)\n",
        "        #print('Failed to converge after', iter,'iterations')\n",
        "    return x,iter\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}