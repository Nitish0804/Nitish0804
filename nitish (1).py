{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9d388be9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a string: manju\n",
      "Number of vowels: 2\n",
      "Number of consonants: 3\n"
     ]
    }
   ],
   "source": [
    "def _count_(input_string):\n",
    "    vowels=set('aeiouAEIOU')\n",
    "    vowel=0\n",
    "    consonant=0\n",
    "    for char in input_string:   \n",
    "        if char.isalpha():\n",
    "            if char in vowels:\n",
    "                vowel += 1\n",
    "            else:\n",
    "                consonant += 1\n",
    "    return vowel, consonant\n",
    "def main():\n",
    "    input_string=input(\"Enter a string\")\n",
    "    vowels, consonants=_count_(input_string)\n",
    "    print(f\"Number of vowels: {vowels}\")\n",
    "    print(f\"Number of consonants:{consonants}\")\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c8dd5884",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Matrix Multiplication Program!\n",
      "How many rows does Matrix A have? 1\n",
      "How many columns does Matrix A have? 1\n",
      "How many rows does Matrix B have? 1\n",
      "How many columns does Matrix B have? 1\n",
      "\n",
      "You will now input the elements for each matrix.\n",
      "\n",
      "Matrix A:\n",
      "Please enter the elements for a 1x1 matrix.\n",
      "Enter row 1 elements, separated by spaces: 1\n",
      "\n",
      "Matrix B:\n",
      "Please enter the elements for a 1x1 matrix.\n",
      "Enter row 1 elements, separated by spaces: 1\n",
      "Here is the resulting matrix:\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def get_matrix(rows, cols):\n",
    "    matrix=[]\n",
    "    print(f\"Please enter the elements{rows}x{cols}matrix\")\n",
    "    for i in range(rows):\n",
    "        while True:\n",
    "            try:\n",
    "                row = list(map(int, input(f\"Enter row {i + 1} elements,separated by spaces\").split()))\n",
    "                if len(row) != cols:\n",
    "                    raise ValueError(f\"Error:Each row must have exactly{cols}elements\")\n",
    "                matrix.append(row)\n",
    "                break\n",
    "            except ValueError as ve:\n",
    "                print(ve)\n",
    "                print(\"Please try again\")\n",
    "    return matrix\n",
    "def multiply_matrices(A, B):\n",
    "    rows_A = len(A)\n",
    "    cols_A = len(A[0])\n",
    "    rows_B = len(B)\n",
    "    cols_B = len(B[0])\n",
    "    if cols_A != rows_B:\n",
    "        return \"Error: Matrix multiplication is not possible\"\n",
    "    result = [[0] * cols_B for _ in range(rows_A)]\n",
    "    for i in range(rows_A):\n",
    "        for j in range(cols_B):\n",
    "            for k in range(cols_A):\n",
    "                result[i][j] += A[i][k] * B[k][j]\n",
    "    return result\n",
    "def print_matrix(matrix):\n",
    "    print(\"Here is the resulting matrix\")\n",
    "    for row in matrix:\n",
    "        print(\" \".join(map(str, row)))\n",
    "def main():\n",
    "    print(\"Welcome to the Matrix Multiplication Program\")\n",
    "    rows_A = int(input(\"How many rows  Matrix A\"))\n",
    "    cols_A = int(input(\"How many columns  Matrix A\"))\n",
    "    rows_B = int(input(\"How many rows  Matrix B\"))\n",
    "    cols_B = int(input(\"How many columns  Matrix B\"))\n",
    "    print(\"You will now input the elements for each matrix\")\n",
    "    print(\"Matrix A\")\n",
    "    A = get_matrix(rows_A, cols_A)\n",
    "    print(\"Matrix B\")\n",
    "    B = get_matrix(rows_B, cols_B)\n",
    "    result = multiply_matrices(A, B)\n",
    "    if isinstance(result, str):\n",
    "        print(result)\n",
    "    else:\n",
    "        print_matrix(result)\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9b7edbf8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the elements  first list,separated by spaces1 2 3 4 \n",
      "enter the elements second list,separated by spaces3 4 5 6 \n",
      "The  common elements between the two lists:2\n"
     ]
    }
   ],
   "source": [
    "def find_common_elements(list1, list2):\n",
    "    return len(set(list1) & set(list2))\n",
    "def main():\n",
    "    list1 = list(map(int, input(\"enter the elements  first list,separated by spaces\").split()))\n",
    "    list2 = list(map(int, input(\"enter the elements second list,separated by spaces\").split()))\n",
    "    count = find_common_elements(list1, list2)\n",
    "    print(f\"The  common elements between the two lists:{count}\")\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "557e2b10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Matrix Transpose Program!\n",
      "How many rows does  matrix have? 2\n",
      "How many columns doe smatrix have? 2\n",
      "\n",
      "You will now input the elements the matrix.\n",
      "Please enter elements for 2x2 matrix.\n",
      "Enter row 1 elements,separated by spaces:1 2 \n",
      "Enter row 2 elements,separated by spaces:1 2\n",
      " transposed matrix is:\n",
      "Here is the resulting matrix:\n",
      "1 1\n",
      "2 2\n"
     ]
    }
   ],
   "source": [
    "def get_matrix(rows, cols):\n",
    "    matrix = []\n",
    "    print(f\"Please enter elements for {rows}x{cols} matrix\")\n",
    "    for i in range(rows):\n",
    "        while True:\n",
    "            try:\n",
    "                row = list(map(int, input(f\"Enter row {i + 1} elements,separated by spaces\").split()))\n",
    "                if len(row) != cols:\n",
    "                    raise ValueError(f\"Each row must exactly {cols} elements\")\n",
    "                matrix.append(row)\n",
    "                break\n",
    "            except ValueError as ve:\n",
    "                print(ve)\n",
    "                print(\"try again\")\n",
    "    return matrix\n",
    "def transpose_matrix(matrix):\n",
    "    return [list(row) for row in zip(*matrix)]\n",
    "def print_matrix(matrix):\n",
    "    print(\"Here is the resulting matrix\")\n",
    "    for row in matrix:\n",
    "        print(\" \".join(map(str, row)))\n",
    "def main():\n",
    "    print(\"Welcome to the Matrix Transpose Program\")\n",
    "    rows = int(input(\"How many rows does  matrix have\"))\n",
    "    cols = int(input(\"How many columns doe smatrix have\"))\n",
    "    print(\"You will now input the elements the matrix\")\n",
    "    matrix = get_matrix(rows, cols)\n",
    "    transposed_matrix = transpose_matrix(matrix)\n",
    "    print(\" transposed matrix is\")\n",
    "    print_matrix(transposed_matrix)\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d3d2272",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28a7b228",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65078815",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
