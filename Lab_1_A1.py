{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tTnyAmowuSHe",
        "outputId": "c6d33e9b-a4d5-44f6-deb4-c89f75d0a61b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number52\n",
            "Enter a number1\n",
            "Enter a number163\n",
            "Enter a number25\n",
            "Enter a number12\n",
            "Enter a number11\n",
            "[52, 1, 163, 25, 12, 11]\n",
            "Element not found\n",
            "Even numbers are- [52, 12]\n",
            "Odd numbers are- [1, 163, 25, 11]\n",
            "Sum of the array is 264\n",
            "Lowest number is- 1\n"
          ]
        }
      ],
      "source": [
        "\n",
        "def linearSearch(arr,number):\n",
        "  m=len(arr)\n",
        "  for i in range(m):\n",
        "    if(number==arr[i]):\n",
        "      flag=i\n",
        "      break\n",
        "\n",
        "    else:\n",
        "      flag= -1\n",
        "  if(flag == -1):\n",
        "    print(\"Element not found\")\n",
        "  else:\n",
        "    print(\"Element found at index-\",flag)\n",
        "\n",
        "def findEvenOdd(arr):\n",
        "  evenArr=[]\n",
        "  oddArr=[]\n",
        "  for element in arr:\n",
        "    if(element%2==0):\n",
        "      evenArr.append(element)\n",
        "    else:\n",
        "      oddArr.append(element)\n",
        "  print(\"Even numbers are-\",evenArr)\n",
        "  print(\"Odd numbers are-\",oddArr)\n",
        "\n",
        "\n",
        "def findSum(arr):\n",
        "  sum=0\n",
        "  for element in arr:\n",
        "    sum=sum+element\n",
        "  return sum\n",
        "\n",
        "def findLowest(arr):\n",
        "  lowest=arr[0]\n",
        "  for element in arr:\n",
        "    if(element<lowest):\n",
        "      lowest=element\n",
        "  return lowest\n",
        "\n",
        "\n",
        "arr=[]\n",
        "n=6\n",
        "for i in range(n):\n",
        "  num=int(input(\"Enter a number\"))\n",
        "  arr.append(num)\n",
        "print(arr)\n",
        "\n",
        "number=13\n",
        "linearSearch(arr,number)\n",
        "findEvenOdd(arr)\n",
        "sum=findSum(arr)\n",
        "print(\"Sum of the array is\",sum)\n",
        "\n",
        "lowest=findLowest(arr)\n",
        "print(\"Lowest number is-\",lowest)\n",
        "\n"
      ]
    }
  ]
}