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
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "532zNbfumhP_",
        "outputId": "570452e1-93d6-478f-c9da-4525b816b8d8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number to check prime26\n",
            "not prime\n"
          ]
        }
      ],
      "source": [
        "\n",
        "def checkPalindrome(number):\n",
        "  temp=number\n",
        "  rev=0\n",
        "  while(number>0):\n",
        "    digit=int(number%10)\n",
        "    rev=int(rev*10)+digit\n",
        "    number=int(number/10)\n",
        "  if(rev==temp):\n",
        "    print(\"Its a palindrome number\")\n",
        "  else:\n",
        "    print(\"not palindrome\")\n",
        "\n",
        "def palindromeArr(arr):\n",
        "  palArr=[]\n",
        "  for number in arr:\n",
        "    temp=number\n",
        "    rev=0\n",
        "    while(number>0):\n",
        "      digit=int(number%10)\n",
        "      rev=int(rev*10)+digit\n",
        "      number=int(number/10)\n",
        "    if(rev==temp):\n",
        "      palArr.append(temp)\n",
        "  return palArr\n",
        "\n",
        "def checkPrime(number_2):\n",
        "  if(number_2==1):\n",
        "    print(\"neither a prime nor not prime\")\n",
        "  else:\n",
        "    for i in range(2,number_2):\n",
        "      if(int(number_2)%i==0):\n",
        "        flag=1\n",
        "        break\n",
        "      else:\n",
        "        flag= -1\n",
        "    if(flag==1):\n",
        "      print(\"not prime\")\n",
        "    elif(flag== -1):\n",
        "      print(\"its a prime number\")\n",
        "\n",
        "\n",
        "def findMin(arr):\n",
        "  min=arr[0]\n",
        "  for element in arr:\n",
        "    if(element<min):\n",
        "      min=element\n",
        "\n",
        "  return min\n",
        "\n",
        "\n",
        "number_2= int(input(\"Enter a number to check prime\"))\n",
        "checkPrime(number_2)\n",
        "\n",
        "number=int(input(\"Enter a number to check palindrome\"))\n",
        "checkPalindrome(number)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "arr=[]\n",
        "n=6\n",
        "for i in range(n):\n",
        "  num=int(input(\"Enter a number\"))\n",
        "  arr.append(num)\n",
        "print(arr)\n",
        "\n",
        "arrPalindrome=palindromeArr(arr)\n",
        "print(\"Palindrome numbers are \",arrPalindrome)\n",
        "\n",
        "min=findMin(arr)\n",
        "print(\"Minimum number is \", min)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "hmq73diOub8U"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}